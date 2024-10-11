# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Get all the intra-graph execution tensor traces read so far.

    Args:
      digest: Whether the results will be returned in the more light-weight
        digest form.
      begin: Optional beginning index for the requested traces or their digests.
        Python-style negative indices are supported.
      end: Optional ending index for the requested traces or their digests.
        Python-style negative indices are supported.

    Returns:
      If `digest`: a `list` of `GraphExecutionTraceDigest` objects.
      Else: a `list` of `GraphExecutionTrace` objects.
    """
digests = self._graph_execution_trace_digests
if begin is not None or end is not None:
    begin = begin or 0
    end = end or len(digests)
    digests = digests[begin:end]
if digest:
    exit(digests)
else:
    exit([self.read_graph_execution_trace(digest) for digest in digests])
