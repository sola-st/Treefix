# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_fiscal.py
date_seq_nem_8_sat = [
    datetime(2006, 9, 2),
    datetime(2007, 9, 1),
    datetime(2008, 8, 30),
    datetime(2009, 8, 29),
    datetime(2010, 8, 28),
    datetime(2011, 9, 3),
]

JNJ = [
    datetime(2005, 1, 2),
    datetime(2006, 1, 1),
    datetime(2006, 12, 31),
    datetime(2007, 12, 30),
    datetime(2008, 12, 28),
    datetime(2010, 1, 3),
    datetime(2011, 1, 2),
    datetime(2012, 1, 1),
    datetime(2012, 12, 30),
]

DEC_SAT = FY5253(n=-1, startingMonth=12, weekday=5, variation="nearest")

tests = [
    (
        makeFY5253NearestEndMonth(startingMonth=8, weekday=WeekDay.SAT),
        date_seq_nem_8_sat,
    ),
    (
        makeFY5253NearestEndMonth(n=1, startingMonth=8, weekday=WeekDay.SAT),
        date_seq_nem_8_sat,
    ),
    (
        makeFY5253NearestEndMonth(startingMonth=8, weekday=WeekDay.SAT),
        [datetime(2006, 9, 1)] + date_seq_nem_8_sat,
    ),
    (
        makeFY5253NearestEndMonth(n=1, startingMonth=8, weekday=WeekDay.SAT),
        [datetime(2006, 9, 3)] + date_seq_nem_8_sat[1:],
    ),
    (
        makeFY5253NearestEndMonth(n=-1, startingMonth=8, weekday=WeekDay.SAT),
        list(reversed(date_seq_nem_8_sat)),
    ),
    (
        makeFY5253NearestEndMonth(n=1, startingMonth=12, weekday=WeekDay.SUN),
        JNJ,
    ),
    (
        makeFY5253NearestEndMonth(n=-1, startingMonth=12, weekday=WeekDay.SUN),
        list(reversed(JNJ)),
    ),
    (
        makeFY5253NearestEndMonth(n=1, startingMonth=12, weekday=WeekDay.SUN),
        [datetime(2005, 1, 2), datetime(2006, 1, 1)],
    ),
    (
        makeFY5253NearestEndMonth(n=1, startingMonth=12, weekday=WeekDay.SUN),
        [datetime(2006, 1, 2), datetime(2006, 12, 31)],
    ),
    (DEC_SAT, [datetime(2013, 1, 15), datetime(2012, 12, 29)]),
]
for test in tests:
    offset, data = test
    current = data[0]
    for datum in data[1:]:
        current = current + offset
        assert current == datum
