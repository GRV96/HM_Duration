"""
This module deals with the string representation of durations in hours and
minutes. Duration strings must conform to the pattern "xx:xx", where each x is
a digit. However, the number of hours contains more than two digits if its
absolute value is greater than or equal to 100. If a duration is negative,
there is a minus sign at the beginning of its string representation.
"""


from re import fullmatch


_COLON = ":"
_HYPHEN = "-"
_ZERO_STR = "0"

DURATION_STR_PATTERN = "-?\d{1,}:\d{2}"
"""
The string representation of durations must match this regular expression.
"""


def duration_from_str(dur_str):
	"""
	Extracts the number of hours and the number of minutes from a duration's
	string representation. Function str_repr_duration must return True for the
	given string.

	Args:
		dur_str (str): a duration's string representation

	Returns:
		tuple:
			[0]: (int) the number of hours
			[1]: (int) the number of minutes

	Raises:
		ValueError: if str_repr_duration(dur_str) returns False
	"""
	if not str_repr_duration(dur_str):
		raise ValueError("Argument '" + dur_str\
			+ "' does not match regex '" + DURATION_STR_PATTERN + "'.")

	if dur_str[0] == _HYPHEN:
		postive = False
		hour_index = 1
	else:
		postive = True
		hour_index = 0

	colon_index = dur_str.index(_COLON)

	hour_str = dur_str[hour_index: colon_index]
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
	minutes. The generated string matches regular expression
	DURATION_STR_PATTERN.

	Args:
		hours (int): the number of hours
		minutes (int): the number of minutes

	Returns:
		str: the string representation of a duration
	"""
	dur_str = _int_to_formatted_str(hours)\
		+ _COLON + _int_to_formatted_str(minutes)

	if hours < 0 or minutes < 0:
		dur_str = _HYPHEN + dur_str

	return dur_str


def _int_to_formatted_str(an_int):
	"""
	Makes a formatted string representation of integers that is part of the
	string representation of durations. If the given integer contains one
	digit, a 0 is added to the string's beginning. The returned string always
	represents the absolute value.

	Args:
		an_int (int): any integral number

	Returns:
		str: the string representation of the absolute value of an_int
	"""
	abs_int = abs(an_int)
	int_str = str(abs_int)

	if 0 <= abs_int and abs_int <= 9:
		int_str = _ZERO_STR + int_str

	return int_str


def str_repr_duration(a_str):
	"""
	Determines whether the given string represents a duration in hours and
	minutes. It does if and only if it matches regular expression
	DURATION_STR_PATTERN. The match is verified by re.fullmatch.

	Args:
		a_str (str): a string that should represent a duration

	Returns:
		bool: True if a_str represents a duration, False otherwise
	"""
	return fullmatch(DURATION_STR_PATTERN, a_str) is not None
