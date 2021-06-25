"""
This module makes string representations of durations in hours and minutes
conform to the format "xx:xx", where each x is a digit.
"""


from re import fullmatch


_COLON = ":"
_HYPHEN = "-"
_ZERO_STR = "0"

DUR_STR_PATTERN = "-?\d{2,}:\d{2}"
"""
All duration strings must match this pattern.
"""


def duration_from_str(dur_str):
	if not fullmatch(DUR_STR_PATTERN, dur_str):
		raise ValueError("Argument '" + dur_str\
			+ "' does not match regex '" + DUR_STR_PATTERN + "'.")

	if dur_str[0] == _HYPHEN:
		postive = False
		offset = 1
	else:
		postive = True
		offset = 0

	colon_index = dur_str.index(_COLON)

	hour_str = dur_str[offset: colon_index]
	if len(hour_str) == 2 and hour_str[0] == _ZERO_STR:
		hour_str = hour_str[1]
	hours = int(hour_str)

	min_str = dur_str[colon_index+1:]
	if min_str[0] == _ZERO_STR:
		min_str = min_str[1]
	minutes = int(min_str)

	if not postive:
		hours *= -1
		minutes *= -1

	return hours, minutes


def duration_to_str(hours, minutes):
	"""
	Makes a formatted string representation of a duration in hours and
	minutes. This string's format is "xx:xx", where each x is a digit.
	However, the number of hours is written with more than two digits if its
	absolute value is greater than or equal to 100. If the number of hours or
	the number of minutes is negative, a minus sign is added at the beginning.

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
	representation of durations. If the given integer contains one digit, a 0
	is added to the string's beginning. The returned string always represents
	the absolute value.

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
