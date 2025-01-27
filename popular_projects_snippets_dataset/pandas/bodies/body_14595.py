# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
import pandas.plotting._matplotlib.converter as conv

assert conv.get_finder(to_offset("B")) == conv._daily_finder
assert conv.get_finder(to_offset("D")) == conv._daily_finder
assert conv.get_finder(to_offset("M")) == conv._monthly_finder
assert conv.get_finder(to_offset("Q")) == conv._quarterly_finder
assert conv.get_finder(to_offset("A")) == conv._annual_finder
assert conv.get_finder(to_offset("W")) == conv._daily_finder
