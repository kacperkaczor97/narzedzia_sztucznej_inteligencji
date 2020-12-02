'''
System alarmnowy
Twórcy: Karol Niemykin, Kacper Kaczor
Uruchomienie: Pobrać projekt do pyCharm pobrać bibloteki i uruchomić projekt.
System polega na ocenie zagrożenia i ustawieniu odpowiedniego poziomu alarmu na podstawie danych z trzech wskaźnikówk: Kamery, Miernika decybeli i lasera.
'''

'''
Importowanie bibliotek
'''

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
'''
Tworzenie funkcji
3 funkcje wejściowe z trzech wskaźników: kamera, laser, miernik decybeli
1 funkcja wyjściowa którą jest alarm
'''
camera = ctrl.Antecedent(np.arange(0, 11, 1), 'camera')
laser = ctrl.Antecedent(np.arange(0, 11, 1), 'laser')
decibel = ctrl.Antecedent(np.arange(0, 11, 1), 'decibel')
alarm = ctrl.Consequent(np.arange(0, 101, 1), 'alarm')


camera.automf(3)
laser.automf(3)
decibel.automf(3)

'''
Stworzenie przedziałów do każdego poziomu alarmu
'''
alarm['low'] = fuzz.trimf(alarm.universe, [0, 0, 50])
alarm['medium-low'] = fuzz.trimf(alarm.universe, [0, 25, 75])
alarm['medium-high'] = fuzz.trimf(alarm.universe, [25, 75, 100])
alarm['high'] = fuzz.trimf(alarm.universe, [50, 100, 100])

'''
Reguły
1. Każdy wskaźnik jest niski - poziom alarmu niski
2. Wskaźniki Kamery i Miernika decybeli średni - poziom alarmu średni-niski
3. Wskaźnik laseru i camery średni - poziom alarmu średni-wysoki
4. Wszystkie wskaźniki wysokie - poziom alarmu wysoki 
'''
rule1 = ctrl.Rule(decibel['poor'] | camera['poor'] | laser['poor'], alarm['low'])
rule2 = ctrl.Rule(camera['average'] | decibel['average'], alarm['medium-low'])
rule3 = ctrl.Rule(laser['average'] | camera['average'], alarm['medium-high'])
rule4 = ctrl.Rule(laser['good'] | camera['good'] | decibel['good'],  alarm['high'])


alarming_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])

alarming = ctrl.ControlSystemSimulation(alarming_ctrl)

'''
Wprowadzanie danych przez urzytkownika do konsoli
'''
print("System Alarmowy")
print("Podaj dane od 1 do 10 z poszczególnych wskaźników:")
camera = input("Kamera: ")
laser = input("Laser: ")
decibel = input("Miernik decybeli: ")

alarming.input['camera'] = int(camera)
alarming.input['laser'] = int(laser)
alarming.input['decibel'] = int(decibel)



alarming.compute()
'''Wyświetlenie końcowego wykresy z wynikiem'''
print(alarming.output['alarm'])
alarm.view(sim=alarming)