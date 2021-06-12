"""
This module makes string representations of durations in hours and minutes in
the format "xx:xx", where each x is a digit.
"""


_COLON = ":"
_HYPHEN = "-"
_ZERO_STR = "0"


def duration_to_str(hours, minutes):
	"""
	Makes a formatted string representation of a duration in hours and
	minutes. The string's format is "xx:xx", where each x is a digit. If the
	number of hours and the number of minutes are negative, a minus sign is
	added at the beginning.

	Args:
		hours (int): the number of hours
		minutes (int): the number of minutes

	Returns:
		str: the string representation of a duration
	"""
	dur_str = _format_duration_int_str(hours)\
		+ _COLON + _format_duration_int_str(minutes)

	if hours < 0 or minutes < 0:
		dur_str = _HYPHEN + dur_str

	return dur_str


def _format_duration_int_str(an_int):
	"""
	Formats the string representation of integers that is part of the string
	representation of durations. If the integer contains one digit, a 0 is
	added to the string's beginning. The returned string always represents the
	absolue value.

	Args:
		an_int (int): any integral number

	Returns:
		str: a formatted string representation of an_int
	"""
	abs_int = abs(an_int)
	int_str = str(abs_int)

	if 0 <= abs_int and abs_int <= 9:
		int_str = _ZERO_STR + int_str

	return int_str
