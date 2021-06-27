from enum import Enum
from src import HM_Duration, duration_to_str, str_repr_duration


ACTUAL_STR = "Actual: "
EXPECTED_STR = "Expected: "
PERIOD = "."
S_QUOTE_PERIOD = "'."


class Operator(Enum):
	ADD = 0
	SUB = 1
	MUL = 2
	DIV = 3


def print_actual_and_expected_durations(
		actual_h, actual_m, expected_h, expected_m):
	print(ACTUAL_STR + duration_to_str(actual_h, actual_m))
	print(EXPECTED_STR + duration_to_str(expected_h, expected_m))


def print_actual_and_expected_values(actual_value, expected_value):
	print(ACTUAL_STR + str(actual_value))
	print(EXPECTED_STR + str(expected_value))


def test_arithmetic(operand1, operator, operand2, expected_result):
	if operator == Operator.ADD:
		actual_result = operand1 + operand2
		operator_str = " + "
	elif operator == Operator.SUB:
		actual_result = operand1 - operand2
		operator_str = " - "
	elif operator == Operator.MUL:
		actual_result = operand1 * operand2
		operator_str = " × "
	elif operator == Operator.DIV:
		actual_result = operand1 / operand2
		operator_str = " ÷ "

	try:
		assert actual_result == expected_result
	except AssertionError:
		print("Artihmetic test failed for "
			+ str(operand1) + operator_str + str(operand2))
		print_actual_and_expected_values(actual_result, expected_result)
		print()


def test_eq(h1, m1, h2, m2, expected_eq):
	d1 = HM_Duration(h1, m1)
	d2 = HM_Duration(h2, m2)
	actual_eq = d1 == d2

	try:
		assert actual_eq == expected_eq
	except AssertionError:
		print("Equality test failed for "
			+ str(d1) + " and " + str(d2) + PERIOD)
		print_actual_and_expected_values(actual_eq, expected_eq)
		print()


def test_from_str(dur_str, expected_h, expected_m):
	duration = HM_Duration.from_str(dur_str)
	actual_h = duration.hours
	actual_m = duration.minutes

	try:
		assert actual_h == expected_h and actual_m == expected_m
	except AssertionError:
		print("Instantiation from a string failed for '"
			+ dur_str + S_QUOTE_PERIOD)
		print_actual_and_expected_durations(
			actual_h, actual_m, expected_h, expected_m)
		print()


def test_instantiation(hours, minutes, expected_h, expected_m):
	duration = HM_Duration(hours, minutes)
	actual_h = duration.hours
	actual_m = duration.minutes

	try:
		assert actual_h == expected_h and actual_m == expected_m
	except AssertionError:
		print("Instantiation test failed for "
			+ duration_to_str(hours, minutes) + PERIOD)
		print_actual_and_expected_durations(
			actual_h, actual_m, expected_h, expected_m)
		print()


def test_opposite(hours, minutes, expected_minus_h, expected_minus_m):
	duration = HM_Duration(hours, minutes)
	opposite_dur = -duration
	actual_minus_h = opposite_dur.hours
	actual_minus_m = opposite_dur.minutes

	try:
		assert actual_minus_h == expected_minus_h\
			and actual_minus_m == expected_minus_m
	except AssertionError:
		expected_opposite = HM_Duration(expected_minus_h, expected_minus_m)
		print("Opposite test failed for "
			+ duration_to_str(hours, minutes) + PERIOD)
		print_actual_and_expected_values(
			repr(opposite_dur), repr(expected_opposite))
		print()


def test_repr(hours, minutes, expected_repr):
	duration = HM_Duration(hours, minutes)
	actual_repr = repr(duration)

	try:
		assert actual_repr == expected_repr
	except AssertionError:
		print("repr test failed.")
		print_actual_and_expected_values(actual_repr, expected_repr)
		print()


def test_sign(hours, minutes, expected_sign):
	duration = HM_Duration(hours, minutes)
	actual_sign = duration.sign

	try:
		assert actual_sign == expected_sign
	except AssertionError:
		print("Sign test failed for "
			+ duration_to_str(hours, minutes) + PERIOD)
		print_actual_and_expected_values(actual_sign, expected_sign)
		print()


def test_string_rep(hours, minutes, expected_str):
	duration = HM_Duration(hours, minutes)
	actual_str = str(duration)

	try:
		assert actual_str == expected_str
	except AssertionError:
		print("String representation test failed.")
		print_actual_and_expected_values(actual_str, expected_str)
		print()


def test_to_hours(hour_arg, minute_arg, expected_h_num):
	duration = HM_Duration(hour_arg, minute_arg)
	actual_h_num = duration.to_hours()

	try:
		assert actual_h_num == expected_h_num
	except AssertionError:
		print("Conversion to hours test failed for "
			+ duration_to_str(hour_arg, minute_arg) + PERIOD)
		print_actual_and_expected_values(actual_h_num, expected_h_num)
		print()


def test_to_minutes(hour_arg, minute_arg, expected_m_num):
	duration = HM_Duration(hour_arg, minute_arg)
	actual_m_num = duration.to_minutes()

	try:
		assert actual_m_num == expected_m_num
	except AssertionError:
		print("Conversion to minutes test failed for "
			+ duration_to_str(hour_arg, minute_arg) + PERIOD)
		print_actual_and_expected_values(actual_m_num, expected_m_num)
		print()


def test_whether_str_repr_dur(dur_str, expected_return):
	actual_return = str_repr_duration(dur_str)

	try:
		assert actual_return == expected_return
	except AssertionError:
		print("str_repr_duration test failed for '"
			+ dur_str + S_QUOTE_PERIOD)
		print_actual_and_expected_values(actual_return, expected_return)
		print()


test_instantiation(0, 0, 0, 0) # 00:00
test_instantiation(0, 7, 0, 7) # 00:07
test_instantiation(7, 0, 7, 0) # 07:00
test_instantiation(7, 7, 7, 7) # 07:07

test_instantiation(0, 77, 1, 17) # 00:77 -> 01:17
test_instantiation(7, 77, 8, 17) # 07:77 -> 08:17

test_instantiation(0, -7, 0, -7) # -00:07
test_instantiation(-7, 0, -7, 0) # -07:00
test_instantiation(-7, -7, -7, -7) # -07:07

test_instantiation(0, -77, -1, -17) # -00:77 -> -01:17
test_instantiation(-7, -77, -8, -17) # -07:77 -> -08:17

test_opposite(0, 0, 0, 0)
test_opposite(0, 13, 0, -13)
test_opposite(0, -13, 0, 13)
test_opposite(7, 0, -7, 0)
test_opposite(-7, 0, 7, 0)
test_opposite(7, 13, -7, -13)
test_opposite(-7, -13, 7, 13)

test_sign(0, 1, 1)
test_sign(1, 0, 1)
test_sign(1, 1, 1)
test_sign(0, 0, 0)
test_sign(0, -1, -1)
test_sign(-1, 0, -1)
test_sign(-1, -1, -1)

test_whether_str_repr_dur("7:19", True)
test_whether_str_repr_dur("07:19", True)
test_whether_str_repr_dur("-7:19", True)
test_whether_str_repr_dur("-07:19", True)
test_whether_str_repr_dur("13:23", True)

test_whether_str_repr_dur("x7:19", False)
test_whether_str_repr_dur("x07:19", False)
test_whether_str_repr_dur("7:19x", False)
test_whether_str_repr_dur("07:19x", False)
test_whether_str_repr_dur("x-7:19", False)
test_whether_str_repr_dur("x-07:19", False)
test_whether_str_repr_dur("-7:19x", False)
test_whether_str_repr_dur("-07:19x", False)

test_from_str("0:00", 0, 0)
test_from_str("00:00", 0, 0)
test_from_str("0:07", 0, 7)
test_from_str("00:07", 0, 7)
test_from_str("7:00", 7, 0)
test_from_str("07:00", 7, 0)
test_from_str("7:07", 7, 7)
test_from_str("07:07", 7, 7)
test_from_str("7:67", 8, 7)
test_from_str("07:67", 8, 7)
test_from_str("19:23", 19, 23)
test_from_str("99:00", 99, 0)
test_from_str("100:00", 100, 0)

test_from_str("-0:00", 0, 0)
test_from_str("-00:00", 0, 0)
test_from_str("-0:07", 0, -7)
test_from_str("-00:07", 0, -7)
test_from_str("-7:00", -7, 0)
test_from_str("-07:00", -7, 0)
test_from_str("-7:07", -7, -7)
test_from_str("-07:07", -7, -7)
test_from_str("-7:67", -8, -7)
test_from_str("-07:67", -8, -7)
test_from_str("-19:23", -19, -23)
test_from_str("-99:00", -99, 0)
test_from_str("-100:00", -100, 0)

test_repr(0, 7, "HM_Duration(0, 7)")
test_repr(10, 83, "HM_Duration(11, 23)")

test_repr(0, -7, "HM_Duration(0, -7)")
test_repr(-10, -83, "HM_Duration(-11, -23)")

test_string_rep(0, 0, "00:00")
test_string_rep(1, 1, "01:01")
test_string_rep(1, 59, "01:59")
test_string_rep(1, 60, "02:00")
test_string_rep(9, 0, "09:00")
test_string_rep(10, 0, "10:00")
test_string_rep(99, 0, "99:00")
test_string_rep(100, 0, "100:00")

test_string_rep(-1, -1, "-01:01")
test_string_rep(-1, -59, "-01:59")
test_string_rep(-1, -60, "-02:00")
test_string_rep(-9, 0, "-09:00")
test_string_rep(-10, 0, "-10:00")
test_string_rep(-99, 0, "-99:00")
test_string_rep(-100, 0, "-100:00")

test_eq(0, 0, 0, 0, True) # 00:00 == 00:00
test_eq(0, 7, 0, 7, True) # 00:07 == 00:07
test_eq(7, 1, 7, 0, False) # 07:01 != 07:00
test_eq(8, 7, 7, 7, False) # 08:07 != 07:07

test_eq(-7, -1, 7, 1, False) # -07:01 != 07:01

test_eq(0, -7, 0, -7, True) # -00:07 == -00:07
test_eq(-7, -1, -7, 0, False) # -07:01 != -07:00
test_eq(-8, -7, -7, -7, False) # -08:07 != -07:07

test_to_hours(0, 0, 0.0)
test_to_hours(0, 15, 0.25)
test_to_hours(0, 17, 0.28333333333333333333333333333333)
test_to_hours(2, 0, 2.0)
test_to_hours(2, 30, 2.50)

test_to_hours(0, -15, -0.25)
test_to_hours(0, -17, -0.28333333333333333333333333333333)
test_to_hours(-2, 0, -2.0)
test_to_hours(-2, -30, -2.50)

test_to_minutes(0, 0, 0)
test_to_minutes(0, 17, 17)
test_to_minutes(1, 17, 77)
test_to_minutes(2, 17, 137)

test_to_minutes(0, -17, -17)
test_to_minutes(-1, -17, -77)
test_to_minutes(-2, -17, -137)

test_arithmetic(HM_Duration(12, 17),
	Operator.ADD, HM_Duration(0, 0), HM_Duration(12, 17))
test_arithmetic(HM_Duration(12, 17),
	Operator.ADD, HM_Duration(3, 55), HM_Duration(16, 12))
test_arithmetic(HM_Duration(12, 17),
	Operator.ADD, HM_Duration(-3, -55), HM_Duration(8, 22))
test_arithmetic(HM_Duration(3, 55),
	Operator.ADD, HM_Duration(-12, -17), HM_Duration(-8, -22))

test_arithmetic(HM_Duration(16, 12),
	Operator.SUB, HM_Duration(0, 0), HM_Duration(16, 12))
test_arithmetic(HM_Duration(16, 12),
	Operator.SUB, HM_Duration(14, 57), HM_Duration(1, 15))
test_arithmetic(HM_Duration(14, 57),
	Operator.SUB, HM_Duration(16, 12), HM_Duration(-1, -15))
test_arithmetic(HM_Duration(14, 57),
	Operator.SUB, HM_Duration(-1, -15), HM_Duration(16, 12))

test_arithmetic(0, Operator.MUL, HM_Duration(2, 2), HM_Duration(0, 0))

test_arithmetic(HM_Duration(2, 2), Operator.MUL, 3, HM_Duration(6, 6))
test_arithmetic(HM_Duration(2, 2), Operator.MUL, 2.5, HM_Duration(5, 5))
test_arithmetic(HM_Duration(2, 2), Operator.MUL, 2.7, HM_Duration(5, 29))

test_arithmetic(-3, Operator.MUL, HM_Duration(2, 2), HM_Duration(-6, -6))
test_arithmetic(-2.5, Operator.MUL, HM_Duration(2, 2), HM_Duration(-5, -5))
test_arithmetic(-2.7, Operator.MUL, HM_Duration(2, 2), HM_Duration(-5, -29))

test_arithmetic(HM_Duration(-2, -2), Operator.MUL, 3, HM_Duration(-6, -6))
test_arithmetic(HM_Duration(-2, -2), Operator.MUL, 2.5, HM_Duration(-5, -5))
test_arithmetic(HM_Duration(-2, -2), Operator.MUL, 2.7, HM_Duration(-5, -29))

test_arithmetic(-3, Operator.MUL, HM_Duration(-2, -2), HM_Duration(6, 6))
test_arithmetic(-2.5, Operator.MUL, HM_Duration(-2, -2), HM_Duration(5, 5))
test_arithmetic(-2.7, Operator.MUL, HM_Duration(-2, -2), HM_Duration(5, 29))

test_arithmetic(HM_Duration(6, 6), Operator.DIV, 3, HM_Duration(2, 2))
test_arithmetic(HM_Duration(7, 7), Operator.DIV, 2, HM_Duration(3, 34))
test_arithmetic(HM_Duration(8, 8), Operator.DIV, 0.8, HM_Duration(10, 10))
test_arithmetic(HM_Duration(11, 11), Operator.DIV, 5.7, HM_Duration(1, 58))

test_arithmetic(HM_Duration(6, 6), Operator.DIV, -3, HM_Duration(-2, -2))
test_arithmetic(HM_Duration(7, 7), Operator.DIV, -2, HM_Duration(-3, -33))
test_arithmetic(HM_Duration(8, 8), Operator.DIV, -0.8, HM_Duration(-10, -10))
test_arithmetic(HM_Duration(11, 11), Operator.DIV, -5.7, HM_Duration(-1, -58))

test_arithmetic(HM_Duration(-6, -6), Operator.DIV, 3, HM_Duration(-2, -2))
test_arithmetic(HM_Duration(-7, -7), Operator.DIV, 2, HM_Duration(-3, -33))
test_arithmetic(HM_Duration(-8, -8), Operator.DIV, 0.8, HM_Duration(-10, -10))
test_arithmetic(HM_Duration(-11, -11), Operator.DIV, 5.7, HM_Duration(-1, -58))

test_arithmetic(HM_Duration(-6, -6), Operator.DIV, -3, HM_Duration(2, 2))
test_arithmetic(HM_Duration(-7, -7), Operator.DIV, -2, HM_Duration(3, 34))
test_arithmetic(HM_Duration(-8, -8), Operator.DIV, -0.8, HM_Duration(10, 10))
test_arithmetic(HM_Duration(-11, -11), Operator.DIV, -5.7, HM_Duration(1, 58))

print("HM_Duration tests done")
