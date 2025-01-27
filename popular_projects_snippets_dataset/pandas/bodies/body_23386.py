# Extracted from ./data/repos/pandas/pandas/core/interchange/column.py
"""
        Return a dictionary containing the underlying buffers.
        The returned dictionary has the following contents:
            - "data": a two-element tuple whose first element is a buffer
                      containing the data and whose second element is the data
                      buffer's associated dtype.
            - "validity": a two-element tuple whose first element is a buffer
                          containing mask values indicating missing data and
                          whose second element is the mask value buffer's
                          associated dtype. None if the null representation is
                          not a bit or byte mask.
            - "offsets": a two-element tuple whose first element is a buffer
                         containing the offset values for variable-size binary
                         data (e.g., variable-length strings) and whose second
                         element is the offsets buffer's associated dtype. None
                         if the data buffer does not have an associated offsets
                         buffer.
        """
buffers: ColumnBuffers = {
    "data": self._get_data_buffer(),
    "validity": None,
    "offsets": None,
}

try:
    buffers["validity"] = self._get_validity_buffer()
except NoBufferPresent:
    pass

try:
    buffers["offsets"] = self._get_offsets_buffer()
except NoBufferPresent:
    pass

exit(buffers)
