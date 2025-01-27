# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback.py
"""Process stack frames.

    Send the content of source-files, on a best-effort basis.

    Returns:
      A list of stack frame IDs.
    """
stack_frames = tf_stack.extract_stack()
stack_frame_ids = []
writer = None
for file_path, lineno, func, _ in stack_frames:
    abs_path = os.path.abspath(file_path)
    if (abs_path, lineno, func) in self._stack_frame_to_id:
        stack_frame_ids.append(
            self._stack_frame_to_id[(abs_path, lineno, func)])
        continue
    with self._stack_frame_to_id_lock:
        if (abs_path, lineno, func) not in self._stack_frame_to_id:
            stack_frame_id = _get_id()
            self._stack_frame_to_id[(abs_path, lineno, func)] = stack_frame_id
            file_index = self._write_source_file_content(abs_path)
            file_line_col = graph_debug_info_pb2.GraphDebugInfo.FileLineCol(
                file_index=file_index, line=lineno, func=func)
            stack_frame_with_id = debug_event_pb2.StackFrameWithId(
                id=stack_frame_id, file_line_col=file_line_col)
            writer = self.get_writer()
            writer.WriteStackFrameWithId(stack_frame_with_id)
        stack_frame_ids.append(
            self._stack_frame_to_id[(abs_path, lineno, func)])

code_location = debug_event_pb2.CodeLocation(
    host_name=self._hostname, stack_frame_ids=stack_frame_ids)
exit(code_location)
