# Extracted from ./data/repos/pandas/pandas/core/interchange/dataframe_protocol.py
"""
        Return an iterator yielding the chunks.

        By default (None), yields the chunks that the data is stored as by the
        producer. If given, ``n_chunks`` must be a multiple of
        ``self.num_chunks()``, meaning the producer must subdivide each chunk
        before yielding it.
        """
