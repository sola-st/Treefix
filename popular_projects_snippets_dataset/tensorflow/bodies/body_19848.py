# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Generates a func that flushes the cache to a file."""
def _print_cache():
    """Flushes the cache to a file."""
    replica_str = ('%d' % file_index)
    if self._parameters.trace_dir:
        output_path = (os.path.join(self._parameters.trace_dir,
                                    _COMPACT_TRACE_FILE_PREFIX)
                       + replica_str + self._get_outfile_suffix())
        output_stream = _OUTPUT_STREAM_ESCAPE + output_path
    else:
        output_stream = sys.stderr

    new_step_line = _REPLICA_ID_TAG + replica_str
    print_ops = []
    if self._parameters.inspect_trace:
        if self._num_signature_dimensions() > 1:
            raise ValueError('Inspecting multi signatures are not supported.')
        if self._parameters.trace_mode in (
            tensor_tracer_flags.TRACE_MODE_HISTORY):
            print_ops.append(
                self._inspect_history_cache(
                    cache=cache,
                    replica_id=replica_id,
                    step_num=step_num,
                    tensor_trace_order=tensor_trace_order))
        else:
            print_ops.append(
                self._inspect_summary_cache(
                    cache=cache,
                    replica_id=replica_id,
                    step_num=step_num,
                    output_stream=output_stream,
                    tensor_trace_order=tensor_trace_order))
    else:
        for i in range(self._num_signature_dimensions()):
            print_ops.append(logging_ops.print_v2(
                new_step_line, '\n',
                cache[:, i], '\n',
                summarize=-1,
                output_stream=output_stream))
    with ops.control_dependencies(print_ops):
        exit(constant_op.constant(0).op)
exit(_print_cache)
