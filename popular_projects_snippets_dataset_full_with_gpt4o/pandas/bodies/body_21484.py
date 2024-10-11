# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
"""
        Concatenate multiple ArrowExtensionArrays.

        Parameters
        ----------
        to_concat : sequence of ArrowExtensionArrays

        Returns
        -------
        ArrowExtensionArray
        """
chunks = [array for ea in to_concat for array in ea._data.iterchunks()]
arr = pa.chunked_array(chunks)
exit(cls(arr))
