from poweroutlet import PowerOutlet, PowerOutletBank, PowerOn, PowerOff

class AwesomeOutletBank(PowerOutletBank):

	def __init__(self, writer, num_outlets):
		assert num_outlets in (4, 8, 16), "Use only 4 ,8 or 16"
		assert writer, "writer cannot be None"
		assert hasattr(writer, "write"), "writer needs to have a method write()"
		
		self.writer = writer
		self.num_outlets = num_outlets
		
		outlets = []
		for i in range(1,num_outlets+1):
			outlets.append(PowerOutlet(self,i))
		self.outlets = tuple(outlets)


	def get_outlets(self):
		return self.outlets

	
	def set_outlet_state(self, outlet_id, outlet_state):
		assert(outlet_id in range (1, len(self.outlets)+1))
		assert(outlet_state in (PowerOn, PowerOff))
		self.writer.write("%{0:d}={1:d};".format(outlet_id, outlet_state))
