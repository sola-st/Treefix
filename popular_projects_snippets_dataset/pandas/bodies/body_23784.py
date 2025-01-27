# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        Open the file in the specified mode

        Parameters
        ----------
        mode : {'a', 'w', 'r', 'r+'}, default 'a'
            See HDFStore docstring or tables.open_file for info about modes
        **kwargs
            These parameters will be passed to the PyTables open_file method.
        """
tables = _tables()

if self._mode != mode:
    # if we are changing a write mode to read, ok
    if self._mode in ["a", "w"] and mode in ["r", "r+"]:
        pass
    elif mode in ["w"]:
        # this would truncate, raise here
        if self.is_open:
            raise PossibleDataLossError(
                f"Re-opening the file [{self._path}] with mode [{self._mode}] "
                "will delete the current file!"
            )

    self._mode = mode

# close and reopen the handle
if self.is_open:
    self.close()

if self._complevel and self._complevel > 0:
    self._filters = _tables().Filters(
        self._complevel, self._complib, fletcher32=self._fletcher32
    )

if _table_file_open_policy_is_strict and self.is_open:
    msg = (
        "Cannot open HDF5 file, which is already opened, "
        "even in read-only mode."
    )
    raise ValueError(msg)

self._handle = tables.open_file(self._path, self._mode, **kwargs)
