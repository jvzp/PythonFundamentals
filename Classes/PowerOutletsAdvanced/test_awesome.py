#!/usr/bin/env python
"""Auto generated test module for: awesome """

#pylint: disable=R0904
#pylint: disable=W0611

import unittest
from awesome import *
from writer import MockWriter

class TestAwesomeOutletBank(unittest.TestCase): 
    """
    Test class for AwesomeOutletBank
    """
    def setUp(self):
        self.writer = MockWriter()
        self.bank = AwesomeOutletBank(self.writer, 4)

    def test___init__(self):
        """ Tests __init__"""
        self.assertEqual(self.bank.num_outlets,4)
        self.assertEqual(self.bank.writer, self.writer)
        

    def test_get_outlets(self):
        """ Tests get_outlets"""
        self.assertEqual(len(self.bank.get_outlets()), 4)


    def test_set_outlet_state(self):
        """ Tests set_outlet_state"""
        self.writer.checker_func = lambda x : self.assertEqual(x, "%1=0;")
        self.bank.set_outlet_state(1, PowerOff)

        self.writer.checker_func = lambda x : self.assertEqual(x, "%2=1;")
        self.bank.set_outlet_state(2, PowerOn)

        self.assertRaises(AssertionError, self.bank.set_outlet_state, 0, PowerOn)
        self.assertRaises(AssertionError, self.bank.set_outlet_state, 5, PowerOn)
        self.assertRaises(AssertionError, self.bank.set_outlet_state, 0, 3)


unittest.main()
