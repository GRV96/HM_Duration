from hm_duration import HM_Duration


COLON = ":"


def print_actual_and_expected(actual_h, actual_m, expected_h, expected_m):
	print("Actual: " + str(actual_h) + COLON + str(actual_m))
	print("Expected: " + str(expected_h) + COLON + str(expected_m))


def test_instantiation(hours, minutes, expected_h, expected_m):
	duration = HM_Duration(hours, minutes)
	actual_h = duration.hours
	actual_m = duration.minutes

	try:
		assert actual_h == expected_h and actual_m == expected_m
	except:
		print("Instantiation test failed for input "
			+ str(hours) + COLON + str(minutes))
		print_actual_and_expected(actual_h, actual_m, expected_h, expected_m)
		print()


test_instantiation(0, 0, 0, 0) # 00:00
test_instantiation(0, 7, 0, 7) # 00:07
test_instantiation(7, 0, 7, 0) # 07:00
test_instantiation(7, 7, 7, 7) # 07:07

test_instantiation(0, 77, 1, 17) # 00:77
test_instantiation(7, 77, 8, 17) # 07:77
