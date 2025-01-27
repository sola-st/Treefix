# Extracted from ./data/repos/pandas/pandas/core/interchange/dataframe_protocol.py
# TODO: not happy with Optional, but need to flag it may be expensive
#       why include it if it may be None - what do we expect consumers
#       to do here?
"""
        Return the number of rows in the DataFrame, if available.
        """
