# System alarmnowy
# Twórcy: Karol Niemykin, Kacper Kaczor
# Uruchomienie: Pobrać projekt do pyCharm pobrać bibloteki i uruchomić projekt.
# System polega na ocenie zagrożenia i ustawieniu odpowiedniego poziomu alarmu na podstawie danych z trzech wskaźnikówk: Kamery, Miernika decybeli i lasera.


import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
#Functions
camera = ctrl.Antecedent(np.arange(0, 11, 1), 'camera')
laser = ctrl.Antecedent(np.arange(0, 11, 1), 'laser')
decibel = ctrl.Antecedent(np.arange(0, 11, 1), 'decibel')
alarm = ctrl.Consequent(np.arange(0, 101, 1), 'alarm')


camera.automf(3)
laser.automf(3)
decibel.automf(3)

#Stworzenie przedziałów do danej funkcji
alarm['low'] = fuzz.trimf(alarm.universe, [0, 0, 50])
alarm['medium'] = fuzz.trimf(alarm.universe, [0, 50, 100])
alarm['high'] = fuzz.trimf(alarm.universe, [50, 100, 100])
#rysowanie wykresów
camera.view()
laser.view()
decibel.view()

alarm.view()
#tworzenie regul
rule1 = ctrl.Rule(decibel['poor'] | camera['poor'] | laser['poor'], alarm['low'])
rule2 = ctrl.Rule(laser['average'], alarm['medium'])
rule3 = ctrl.Rule(laser['good'] | camera['good'] | decibel['good'],  alarm['high'])

# rule1.view()

alarming_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

alarming = ctrl.ControlSystemSimulation(alarming_ctrl)

#wprowadzenie danych
print("System Alarmowy")
print("Podaj dane od 1 do 10 ze wskaźników poszczegolnych alarmów:")
camera = input("Kamera: ")
laser = input("Laser: ")
decibel = input("Miernik decybeli: ")

alarming.input['camera'] = int(camera)
alarming.input['laser'] = int(laser)
alarming.input['decibel'] = int(decibel)



alarming.compute()
#wykres koncowy
print(alarming.output['alarm'])
alarm.view(sim=alarming)