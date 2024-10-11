# Extracted from ./data/repos/pandas/pandas/core/interchange/dataframe_protocol.py
"""
        Device type and device ID for where the data in the buffer resides.
        Uses device type codes matching DLPack.
        Note: must be implemented even if ``__dlpack__`` is not.
        """
