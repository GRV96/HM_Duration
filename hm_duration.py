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

	def __add__(self, other):
		"""
		Creates an instance that represents the sum of self and other.

		Args:
			other (HM_Duration): another duration

		Returns:
			HM_Duration: the sum of self and other
		"""
		return HM_Duration(
			self._hours+other._hours, self._minutes+other._minutes)

	def __eq__(self, other):
		if not isinstance(other, self.__class__):
			return False

		return self._hours == other._hours\
			and self._minutes == other._minutes

	def __str__(self):
		return str(self._hours) + ":" + str(self._minutes)

	def __sub__(self, other):
		"""
		Creates an instance that represents the difference of self and other.

		Args:
			other (HM_Duration): another duration

		Returns:
			HM_Duration: the difference of self and other
		"""
		return HM_Duration(
			self._hours-other._hours, self._minutes-other._minutes)

	@property
	def hours(self):
		return self._hours

	@property
	def minutes(self):
		return self._minutes

	def _regularize(self):
		self._hours += self._minutes // _MINS_IN_HOUR
		self._minutes = self._minutes % _MINS_IN_HOUR

	def to_hours(self):
		return self._hours + self._minutes / _MINS_IN_HOUR

	def to_minutes(self):
		return self._hours * _MINS_IN_HOUR + self._minutes
