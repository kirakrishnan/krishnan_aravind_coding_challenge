import unittest
from unittest.mock import patch
from controller import validate_input
from turtle_simulator import switch_light, setup_simulator_window

class TrafficLightSimulatorTestCase(unittest.TestCase):

    def test_if_returns_3_transition_times_1(self):
        with unittest.mock.patch('builtins.input', return_value='1,2,3'):
            self.assertEqual(validate_input(), [1,2,3])

    def test_if_red_switches_to_green(self):
        self.assertEqual(switch_light("red"),"green")

    def test_if_green_switches_to_yellow(self):
        self.assertEqual(switch_light("green"),"yellow")

    def test_if_yellow_switches_to_red(self):
        self.assertEqual(switch_light("yellow"),"red")


if __name__ == "__main__":
    unittest.main()

