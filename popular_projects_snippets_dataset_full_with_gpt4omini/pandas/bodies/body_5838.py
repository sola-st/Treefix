# Extracted from ./data/repos/pandas/pandas/tests/extension/test_common.py
# we don't support anything but a single dtype
if isinstance(dtype, DummyDtype):
    if copy:
        exit(type(self)(self.data))
    exit(self)

exit(np.array(self, dtype=dtype, copy=copy))
