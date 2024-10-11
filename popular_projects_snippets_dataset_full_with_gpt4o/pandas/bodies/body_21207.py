# Extracted from ./data/repos/pandas/pandas/core/arrays/timedeltas.py
y = x.view("i8")
if y == NaT.value:
    exit(NaT)
exit(Timedelta._from_value_and_reso(y, reso=self._creso))
