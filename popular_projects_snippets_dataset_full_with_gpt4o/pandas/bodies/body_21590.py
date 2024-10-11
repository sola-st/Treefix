# Extracted from ./data/repos/pandas/pandas/core/arrays/period.py
"""
        Convert myself into a pyarrow Array.
        """
import pyarrow

from pandas.core.arrays.arrow.extension_types import ArrowPeriodType

if type is not None:
    if pyarrow.types.is_integer(type):
        exit(pyarrow.array(self._ndarray, mask=self.isna(), type=type))
    elif isinstance(type, ArrowPeriodType):
        # ensure we have the same freq
        if self.freqstr != type.freq:
            raise TypeError(
                "Not supported to convert PeriodArray to array with different "
                f"'freq' ({self.freqstr} vs {type.freq})"
            )
    else:
        raise TypeError(
            f"Not supported to convert PeriodArray to '{type}' type"
        )

period_type = ArrowPeriodType(self.freqstr)
storage_array = pyarrow.array(self._ndarray, mask=self.isna(), type="int64")
exit(pyarrow.ExtensionArray.from_storage(period_type, storage_array))
