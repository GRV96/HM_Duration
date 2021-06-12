_MINS_IN_HOUR = 60
"""
The number of minutes in one hour
"""


class HM_Duration:
	"""
	This class represents durations as a number of hours and minutes. It also
	allows to perform arithmetic operations on them.
	"""

	def __init__(self, hours, minutes):
		self._hours = hours
		self._minutes = minutes
		self._regularize()

	def __eq__(self, other):
		return self._hours == other._hours\
			and self._minutes == other._minutes

	def __str__(self):
		return str(self._hours) + ":" + str(self._minutes)

	@property
	def hours(self):
		return self._hours

	@property
	def minutes(self):
		return self._minutes

	def _regularize(self):
		self._hours += self._minutes // _MINS_IN_HOUR
		self._minutes = self._minutes % _MINS_IN_HOUR
