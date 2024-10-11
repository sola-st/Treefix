# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_fiscal.py
offset_lom_aug_sat = makeFY5253LastOfMonth(startingMonth=8, weekday=WeekDay.SAT)
offset_lom_aug_sat_1 = makeFY5253LastOfMonth(
    n=1, startingMonth=8, weekday=WeekDay.SAT
)

date_seq_lom_aug_sat = [
    datetime(2006, 8, 26),
    datetime(2007, 8, 25),
    datetime(2008, 8, 30),
    datetime(2009, 8, 29),
    datetime(2010, 8, 28),
    datetime(2011, 8, 27),
    datetime(2012, 8, 25),
    datetime(2013, 8, 31),
    datetime(2014, 8, 30),
    datetime(2015, 8, 29),
    datetime(2016, 8, 27),
]

tests = [
    (offset_lom_aug_sat, date_seq_lom_aug_sat),
    (offset_lom_aug_sat_1, date_seq_lom_aug_sat),
    (offset_lom_aug_sat, [datetime(2006, 8, 25)] + date_seq_lom_aug_sat),
    (offset_lom_aug_sat_1, [datetime(2006, 8, 27)] + date_seq_lom_aug_sat[1:]),
    (
        makeFY5253LastOfMonth(n=-1, startingMonth=8, weekday=WeekDay.SAT),
        list(reversed(date_seq_lom_aug_sat)),
    ),
]
for test in tests:
    offset, data = test
    current = data[0]
    for datum in data[1:]:
        current = current + offset
        assert current == datum
