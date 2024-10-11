# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py

if verify_integrity:
    # Assertion disabled for performance
    # assert all(isinstance(x, Index) for x in axes)

    for block in blocks:
        if self.ndim != block.ndim:
            raise AssertionError(
                f"Number of Block dimensions ({block.ndim}) must equal "
                f"number of axes ({self.ndim})"
            )
        # As of 2.0, the caller is responsible for ensuring that
        #  DatetimeTZBlock with block.ndim == 2 has block.values.ndim ==2;
        #  previously there was a special check for fastparquet compat.

    self._verify_integrity()
