# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""Writes graphs from a RunMetadata summary.

  Args:
    name: A name for this summary. The summary tag used for TensorBoard will be
      this name prefixed by any active name scopes.
    data: A RunMetadata proto to write.
    step: Explicit `int64`-castable monotonic step value for this summary. If
      omitted, this defaults to `tf.summary.experimental.get_step()`, which must
      not be None.

  Returns:
    True on success, or false if no summary was written because no default
    summary writer was available.

  Raises:
    ValueError: if a default writer exists, but no step was provided and
      `tf.summary.experimental.get_step()` is None.
  """
summary_metadata = summary_pb2.SummaryMetadata()
# Hard coding a plugin name. Please refer to go/tb-plugin-name-hardcode for
# the rationale.
summary_metadata.plugin_data.plugin_name = "graph_run_metadata_graph"
# version number = 1
summary_metadata.plugin_data.content = b"1"

data = config_pb2.RunMetadata(
    function_graphs=data.function_graphs,
    partition_graphs=data.partition_graphs)

with summary_scope(name,
                   "graph_run_metadata_graph_summary",
                   [data, step]) as (tag, _):
    with ops.device("cpu:0"):
        tensor = constant_op.constant(data.SerializeToString(),
                                      dtype=dtypes.string)
    exit(write(
        tag=tag,
        tensor=tensor,
        step=step,
        metadata=summary_metadata))
