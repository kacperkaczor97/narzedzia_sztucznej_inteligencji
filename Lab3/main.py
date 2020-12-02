import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

camera = ctrl.Antecedent(np.arange(0, 40, 1), 'camera')
laser = ctrl.Antecedent(np.arange(0, 40, 1), 'laser')
decible = ctrl.Consequent(np.arange(0, 40, 1), 'decible')
alarm = ctrl.Consequent(np.arange(0, 101, 1), 'alarm')


camera.automf(3)
laser.automf(3)
decible.automf(3)


alarm['low'] = fuzz.trimf(alarm.universe, [0, 0, 50])
alarm['medium-low'] = fuzz.trimf(alarm.universe, [0, 25, 100])
alarm['medium-high'] = fuzz.trimf(alarm.universe, [25, 75, 100])
alarm['high'] = fuzz.trimf(alarm.universe, [50, 100, 100])

camera.view()
laser.view()
decible.view()

alarm.view()

rule1 = ctrl.Rule(camera['poor'] | laser['poor'] | decible['poor'], alarm['low'])
rule2 = ctrl.Rule(camera['average'], alarm['medium-low'])
rule3 = ctrl.Rule(laser['average'], alarm['medium-high'])
rule4 = ctrl.Rule(laser['good'] | decible['good'] | camera['good'],  alarm['high'])

rule1.view()

alarming_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])

alarming = ctrl.ControlSystemSimulation(alarming_ctrl)


alarming.input['camera'] = 6.5
alarming.input['laser'] = 9.8
alarming.input['decibel'] = 3.2


alarming.compute()

print(alarming.output['alarm'])
alarm.view(sim=alarming)