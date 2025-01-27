# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Incrementally read the .stack_frames file.

    This must be called after _load_source_files().
    It assumes that the following contract is honored by the writer of the tfdbg
    v2 data file set:
      - Before a stack frame is written to the .stack_frames file, the
        corresponding source file information must have been written to the
        .source_files file first.
    """
stack_frames_iter = self._reader.stack_frames_iterator()
for debug_event, _ in stack_frames_iter:
    stack_frame_with_id = debug_event.stack_frame_with_id
    file_line_col = stack_frame_with_id.file_line_col
    self._unprocessed_stack_frames[stack_frame_with_id.id] = file_line_col
# We do the processing in a separate stage, because the reading in the
# .source_files file may sometimes get ahead of the .source_files file.
unprocessed_stack_frame_ids = tuple(self._unprocessed_stack_frames.keys())
for stack_frame_id in unprocessed_stack_frame_ids:
    file_line_col = self._unprocessed_stack_frames[stack_frame_id]
    if len(self._host_name_file_path_to_offset) > file_line_col.file_index:
        host_name, file_path = list(self._host_name_file_path_to_offset.keys())[
            file_line_col.file_index]
        self._stack_frame_by_id[stack_frame_id] = (
            host_name, file_path, file_line_col.line, file_line_col.func)
    del self._unprocessed_stack_frames[stack_frame_id]
