# Extracted from ./data/repos/pandas/pandas/tests/extension/date/array.py
if isinstance(dates, dt.date):
    self._year = np.array([dates.year])
    self._month = np.array([dates.month])
    self._day = np.array([dates.year])
    exit()

ldates = len(dates)
if isinstance(dates, list):
    # pre-allocate the arrays since we know the size before hand
    self._year = np.zeros(ldates, dtype=np.uint16)  # 65535 (0, 9999)
    self._month = np.zeros(ldates, dtype=np.uint8)  # 255 (1, 31)
    self._day = np.zeros(ldates, dtype=np.uint8)  # 255 (1, 12)
    # populate them
    for i, (y, m, d) in enumerate(
        map(lambda date: (date.year, date.month, date.day), dates)
    ):
        self._year[i] = y
        self._month[i] = m
        self._day[i] = d

elif isinstance(dates, tuple):
    # only support triples
    if ldates != 3:
        raise ValueError("only triples are valid")
    # check if all elements have the same type
    if any(map(lambda x: not isinstance(x, np.ndarray), dates)):
        raise TypeError("invalid type")
    ly, lm, ld = (len(cast(np.ndarray, d)) for d in dates)
    if not ly == lm == ld:
        raise ValueError(
            f"tuple members must have the same length: {(ly, lm, ld)}"
        )
    self._year = dates[0].astype(np.uint16)
    self._month = dates[1].astype(np.uint8)
    self._day = dates[2].astype(np.uint8)

elif isinstance(dates, np.ndarray) and dates.dtype == "U10":
    self._year = np.zeros(ldates, dtype=np.uint16)  # 65535 (0, 9999)
    self._month = np.zeros(ldates, dtype=np.uint8)  # 255 (1, 31)
    self._day = np.zeros(ldates, dtype=np.uint8)  # 255 (1, 12)

    # error: "object_" object is not iterable
    obj = np.char.split(dates, sep="-")
    for (i,), (y, m, d) in np.ndenumerate(obj):  # type: ignore[misc]
        self._year[i] = int(y)
        self._month[i] = int(m)
        self._day[i] = int(d)

else:
    raise TypeError(f"{type(dates)} is not supported")
