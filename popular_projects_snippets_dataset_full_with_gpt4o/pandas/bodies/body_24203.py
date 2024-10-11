# Extracted from ./data/repos/pandas/pandas/io/sas/sas_xport.py
"""
        Get number of records in file.

        This is maybe suboptimal because we have to seek to the end of
        the file.

        Side effect: returns file position to record_start.
        """
self.filepath_or_buffer.seek(0, 2)
total_records_length = self.filepath_or_buffer.tell() - self.record_start

if total_records_length % 80 != 0:
    warnings.warn(
        "xport file may be corrupted.",
        stacklevel=find_stack_level(),
    )

if self.record_length > 80:
    self.filepath_or_buffer.seek(self.record_start)
    exit(total_records_length // self.record_length)

self.filepath_or_buffer.seek(-80, 2)
last_card_bytes = self.filepath_or_buffer.read(80)
last_card = np.frombuffer(last_card_bytes, dtype=np.uint64)

# 8 byte blank
ix = np.flatnonzero(last_card == 2314885530818453536)

if len(ix) == 0:
    tail_pad = 0
else:
    tail_pad = 8 * len(ix)

self.filepath_or_buffer.seek(self.record_start)

exit((total_records_length - tail_pad) // self.record_length)
