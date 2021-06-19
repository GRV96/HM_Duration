from .duration_string import duration_to_str
from math import floor


_MINS_IN_HOUR = 60
"""
The number of minutes in one hour
"""


class HM_Duration:
	"""
	This class represents durations as a number of hours and a number of
	minutes. It also allows to perform arithmetic operations on them.
	"""

	def __init__(self, hours, minutes):
		"""
		The constructor needs the number of hours and the number of minutes
		that make a duration.

		Args:
			hours (int): a number of hours
			minutes (int): a number of minutes
		"""
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

	def __mul__(self, number):
		"""
		Creates an instance that represents the product of self by a number.
		The result is approximated to the nearest minute.

		Args:
			number (int or float): any integral or real number

		Returns:
			HM_Duration: the product of self by a number
		"""
		dur_in_mins = _round_half_up(self.to_minutes() * number)
		return HM_Duration(0, dur_in_mins)

	def __rmul__(self, number):
		return self.__mul__(number)

	def __repr__(self):
		return self.__class__.__name__ +\
			"(" + str(self._hours) + ", " + str(self._minutes) + ")"

	def __str__(self):
		return duration_to_str(self._hours, self._minutes)

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

	def __truediv__(self, number):
		"""
		Creates an instance that represents the quotient of self by a number.
		The result is approximated to the nearest minute.

		Args:
			number (int or float): any integral or real number

		Returns:
			HM_Duration: the quotient of self by a number
		"""
		dur_in_mins = _round_half_up(self.to_minutes() / number)
		return HM_Duration(0, dur_in_mins)

	@property
	def hours(self):
		"""
		Read-only property. This duration's number of hours.
		"""
		return self._hours

	@property
	def minutes(self):
		"""
		Read-only property. This duration's number of minutes.
		"""
		return self._minutes

	def _regularize(self):
		"""
		Makes sure that the number of minutes is less than 60.
		"""
		self._hours += self._minutes // _MINS_IN_HOUR
		self._minutes = self._minutes % _MINS_IN_HOUR

	def to_hours(self):
		"""
		Converts this duration to a real number of hours.

		Returns:
			float: a real number of hours equal to this duration
		"""
		return self._hours + self._minutes / _MINS_IN_HOUR

	def to_minutes(self):
		"""
		Converts this duration to an integral number of minutes.

		Returns:
			int: an integral number of minutes equal to this duration
		"""
		return self._hours * _MINS_IN_HOUR + self._minutes


def _round_half_up(n, decimals=0):
	# Source: https://realpython.com/python-rounding/#rounding-half-up
    multiplier = 10 ** decimals
    return int(floor(n*multiplier + 0.5) / multiplier)
