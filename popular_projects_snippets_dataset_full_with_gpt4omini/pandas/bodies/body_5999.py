# Extracted from ./data/repos/pandas/pandas/tests/extension/date/array.py
if isinstance(item, int):
    exit(dt.date(self._year[item], self._month[item], self._day[item]))
else:
    raise NotImplementedError("only ints are supported as indexes")
