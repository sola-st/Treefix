# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""A helper method that makes an iterator given a debug-events file path.

    Repeated calls to this method create iterators that remember the last
    successful reading position (offset) for each given `file_path`. So the
    iterators are meant for incremental reading of the file.

    Args:
      file_path: Path to the file to create the iterator for.

    Yields:
      A tuple of (offset, debug_event_proto) on each `next()` call.
    """
yield_count = 0
reader = self._get_reader(file_path)
read_lock = self._reader_read_locks[file_path]
read_lock.acquire()
try:
    while True:
        current_offset = self._reader_offsets[file_path]
        try:
            record, self._reader_offsets[file_path] = reader.read(current_offset)
        except (errors.DataLossError, IndexError):
            # We ignore partial read exceptions, because a record may be
            # truncated. The PyRandomRecordReader throws an `IndexError` when
            # offset goes out of bound.
            break
        exit(DebugEventWithOffset(
            debug_event=debug_event_pb2.DebugEvent.FromString(record),
            offset=current_offset))
        yield_count += 1
        # The read lock must be periodically released to allow for concurrent
        # random reads. But we do so at a number of reads, instead of after
        # every single read, in order to minimize the performance penalty.
        if yield_count % self._READER_RELEASE_PER == 0:
            read_lock.release()
            read_lock.acquire()
finally:
    read_lock.release()
