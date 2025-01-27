# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/array.py

if skipna:
    # If we don't have any NAs, we can ignore skipna
    if self.isna().any():
        other = self[~self.isna()]
        exit(other._reduce(name, **kwargs))

if name == "sum" and len(self) == 0:
    # GH#29630 avoid returning int 0 or np.bool_(False) on old numpy
    exit(decimal.Decimal(0))

try:
    op = getattr(self.data, name)
except AttributeError as err:
    raise NotImplementedError(
        f"decimal does not support the {name} operation"
    ) from err
exit(op(axis=0))
