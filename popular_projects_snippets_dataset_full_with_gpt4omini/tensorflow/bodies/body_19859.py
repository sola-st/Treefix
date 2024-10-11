# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Writes the given caches as tensor summary.

      Args:
        step: Step tensor with dimension [num_cores].
        event_file_suffix: Event filename suffix tensor.
        **kwargs: The dictionary of tensors that needs to be written as
          summaries. Key and value pairs within kwargs correspond to the tag
          name, and tensor content that will be written using summary.write.
          The trace_modes that use this function are:
            - summary: In summary mode, kwargs includes a single (tag, content)
            pair which are, _TT_SUMMARY_TAG and a tf.float32 signature_cache
            variable. The dimension of the signature_cache is:
              num_cores x num_traced_tensors x num_signatures.
            - full_tensor_summary: kwargs will include all traced tensors. Tag
            and content correspond to the name of the tensor, and its actual
            content.
      Returns:
        A tf.Operation that needs to be executed for the host call dependencies.
      """
file_suffix = _TT_EVENT_FILE_SUFFIX
if event_file_suffix is not None:
    file_suffix = string_ops.string_join([file_suffix, event_file_suffix],
                                         separator='.')
# TODO(deveci): Parametrize max_queue, so that flushing op can be called
# less frequently.
# Setting max_queue to 100 appears to be safe even when the number of
# iterations are much lower, as the destructor of the writer flushes it.
summary_write_ops = []
summary_writer = summary.create_file_writer_v2(
    self._parameters.trace_dir,
    filename_suffix=file_suffix,
    max_queue=_TT_SUMMARY_MAX_QUEUE)
graph.add_to_collection(
    TENSOR_TRACER_SUMMARY_COLLECTION, summary_writer)

step_value = step[0]
dt = step_value.dtype

# The step parameter to a summary write call must be 64-bit.
if dt.__ne__(dtypes.int64) and dt.__ne__(
    dtypes.uint64) and dt.__ne__(dtypes.float64):
    step_value = math_ops.cast(step_value, dtypes.int64)

with summary_writer.as_default():
    summary_metadata = summary_pb2.SummaryMetadata(
        plugin_data=summary_pb2.SummaryMetadata.PluginData(
            plugin_name=_TT_TENSORBOARD_PLUGIN_NAME))
    for key, value in kwargs.items():
        # Check whether we need to compute aggregated statistics that merge
        # all cores statistics.
        if not self._parameters.collect_summary_per_core:
            # Merge only statistics tensor, if it is any other tensor we simply,
            # concatenate them.
            # Also, if there is only a single core (first dim. is 0), then skip
            # aggregation.
            if key == _TT_SUMMARY_TAG and value.shape.as_list()[0] != 1:
                value = self.aggregate_global_cache(value)
        with ops.control_dependencies([summary_writer.init()]):
            summary_write_ops.append(summary.write(
                _TT_SUMMARY_TAG + '/' + key + '.' + graph_summary_tag,
                value, metadata=summary_metadata,
                step=step_value))
exit(control_flow_ops.group(summary_write_ops))
