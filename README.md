# hm_duration

Package hm_duration helps working with durations in hours and minutes. Among
other functionalities, it offers arithmetic operations, comparison, string
representation and instantiation from a string representation.

### Package content

**HM_Duration**

This class represents durations as a number of hours and a number of minutes.

**DURATION_STR_PATTERN**

This constant stores regular expression "-?\d{1,}:\d{2}". Strings that match
it represent durations, and static method HM_Duration.from_str can use them to
instantiate HM_Duration.

**str_repr_duration**

This function determines whether a string matches DURATION_STR_PATTERN. If it
does, the string can be used to instantiate HM_Duration.
