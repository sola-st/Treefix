# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Get `Execution`s or `ExecutionDigest`s this reader has read so far.

    Args:
      digest: Whether the results are returned in a digest form, i.e.,
        `ExecutionDigest` format, instead of the more detailed `Execution`
        format.
      begin: Optional beginning index for the requested execution data objects
        or their digests. Python-style negative indices are supported.
      end: Optional ending index for the requested execution data objects or
        their digests. Python-style negative indices are supported.

    Returns:
      If `digest`: a `list` of `ExecutionDigest` objects.
      Else: a `list` of `Execution` objects.
    """
digests = self._execution_digests
if begin is not None or end is not None:
    begin = begin or 0
    end = end or len(digests)
    digests = digests[begin:end]
if digest:
    exit(digests)
else:
    # TODO(cais): Optimizer performance removing repeated file open/close.
    exit([self.read_execution(digest) for digest in digests])
