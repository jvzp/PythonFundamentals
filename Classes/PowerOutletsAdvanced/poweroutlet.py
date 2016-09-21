#!/usr/bin/env python

PowerOn = 1
PowerOff = 0

class PowerOutletBank(object):
	'''\"abstract base class\" for any power outlet bank abstraction'''

	def get_outlets(self):
		'''Returns a tuple of PowerOutlet objects in this bank'''
		raise NotImplementedError("Subclasses should implement this error!")

	def set_outlet_state(self, outlet_id, outlet_state):
		'''Sets outlet correspondig to outlet_id to state corresponding outlet_state'''
		raise NotImplementedError("Subclasses should implement this error!")


class PowerOutlet(object):
	'''\"base\" for any power outlet abstraction\nUsable as a generic abstraction as is'''

	def __init__(self, bank, identifier):
		self.bank = bank
		self.identifier = identifier

	def set_state(self, outlet_state):
		'''Sets thet state of this outlet to the corresponding outlet_state'''
		self.bank.set_outlet_state(self.identifier, outlet_state)
