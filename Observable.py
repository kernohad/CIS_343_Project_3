class Observable(object):

	def __init__(self):
		self.obervers = []

	def add_observer(self, observer):
		if not observer in self.observers:
			self.observers.append(observer)

	def remove_observer(self, observer):
		if oberver in self.observers:
			self.observers.remove(observer)

	def remove_all_observers(self):
		self.obervers = []