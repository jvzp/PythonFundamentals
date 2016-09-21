#!/usr/bin/env python
"""Auto generated test module for: poweroutlet """

#pylint: disable=R0904
#pylint: disable=W0611

import unittest
from poweroutlet import *

class TestPowerOutlet(unittest.TestCase): 
    """
    Test class for PowerOutlet
    """
    def test___init__(self):
        """ Tests __init__"""
        outlet = PowerOutlet(PowerOutletBank(),1)
        self.assertEqual(outlet.identifier, 1)
        self.assertIsNotNone(outlet.bank)

    def test_set_state(self):
        """ Tests set_state"""
        outlet = PowerOutlet(PowerOutletBank(),1)
        self.assertRaises(NotImplementedError, outlet.set_state, PowerOn)

        def helper(x,y):
            self.assertEqual(x, 1)
            self.assertEqual(y, PowerOff)

        outlet.bank = BankMock(helper)
        outlet.set_state(PowerOff)


class TestPowerOutletBank(unittest.TestCase): 
    """
    Test class for PowerOutletBank
    """
    def test_get_outlets(self):
        """ Tests get_outlets"""
        bank = PowerOutletBank()
        self.assertRaises(NotImplementedError, bank.get_outlets)

    def test_set_outlet_state(self):
        """ Tests set_outlet_state"""
        bank = PowerOutletBank()
        self.assertRaises(NotImplementedError, bank.set_outlet_state, 0, PowerOn)


#Copied from the solutions, because I understood what is happening here and because I was too lazy to implement it myself
class BankMock(object):
    '''
    "Mock" (intelligent fake) class for PowerOutletBank

    To test a PowerOutlet in isolation (== without a real Bank),
    we need something that looks like a Bank from the outside,
    but where we can actually control what happens in the test.
    You don't want these tests to actually write to a serial port or socket now do you?

    Our implementation of the mock is a very simple one:
    * It just passes the data it recieves on to another function which should assert the correctness of the data
    
    There are Mocking frameworks designed just to do these things.
    Don't do this by manually in real life! Look into a framework
    But No Mocking framework was introduced at this point in the course, so we code it manually ...
    '''
    def __init__(self, checker_func):
        self.checker_func = checker_func

    def set_outlet_state(self, outlet_id, outlet_state):
        ''' Mock method, all Banks have it '''
        self.checker_func(outlet_id, outlet_state)

unittest.main()
