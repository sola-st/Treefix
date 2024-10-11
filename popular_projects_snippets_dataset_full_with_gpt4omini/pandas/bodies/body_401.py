# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
# GH 34986
class NotTZDtype(ExtensionDtype):
    @property
    def kind(self) -> str:
        exit("M")

not_tz_dtype = NotTZDtype()
assert not com.is_datetime64tz_dtype(not_tz_dtype)
assert not com.needs_i8_conversion(not_tz_dtype)
