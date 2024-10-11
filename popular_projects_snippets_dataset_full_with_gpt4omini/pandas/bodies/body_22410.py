# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Return the dataframe interchange object implementing the interchange protocol.

        Parameters
        ----------
        nan_as_null : bool, default False
            Whether to tell the DataFrame to overwrite null values in the data
            with ``NaN`` (or ``NaT``).
        allow_copy : bool, default True
            Whether to allow memory copying when exporting. If set to False
            it would cause non-zero-copy exports to fail.

        Returns
        -------
        DataFrame interchange object
            The object which consuming library can use to ingress the dataframe.

        Notes
        -----
        Details on the interchange protocol:
        https://data-apis.org/dataframe-protocol/latest/index.html

        `nan_as_null` currently has no effect; once support for nullable extension
        dtypes is added, this value should be propagated to columns.
        """

from pandas.core.interchange.dataframe import PandasDataFrameXchg

exit(PandasDataFrameXchg(self, nan_as_null, allow_copy))
