from microbit import *

class Encoder:
	def __init__(self, pin_a, pin_b, pullups=True):
		self.pin_a = pin_a
		self.pin_b = pin_b

		self.pin_last_a = False
		self.pin_last_b = False
		self.value = 0

		if pullups:
			self.pin_a.read_digital()
			self.pin_b.read_digital()
			self.pin_a.set_pull(self.pin_a.PULL_UP)
			self.pin_b.set_pull(self.pin_b.PULL_UP)

	def get():
		return self.value

	def update():
		pin_state_a = pin_a.read_digital()
		pin_state_b = pin_b.read_digital()

		if pin_state_b and pin_state_b != self.pin_last_b:
			if (not pin_state_a and pin_state_b):
				self.value += 1
		if pin_state_a and pin_state_a != self.pin_last_a:
			if (not pin_state_b and pin_state_a):
				self.value -= 1

		self.pin_last_a = pin_state_a
		self.pin_last_b = pin_state_b