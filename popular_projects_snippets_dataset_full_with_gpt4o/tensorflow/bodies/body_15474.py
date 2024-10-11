# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_to_tensor_op_test.py
"""Run a benchmark with the specified configuration parameters.

    Args:
      shape: Bounding box for the input ragged tensor.
      ragged_rank: Ragged rank for the input ragged tensor.  Defaults to
        `len(shape)-1`.
      dtype: Data type for the input ragged tensor.
      fill: How full each dimension should be (0-1).  Corresponds 1:1 with
        `shape`.  Defaults to 0.8 for each dimension.
      default_shape: Shape for the default (padding) value.
      output_shape: Output shape -- ragged tensor will be padded or cropped to
        this shape.
      min_iters: Minimum iterations for benchmark.
    """
if ragged_rank is None:
    ragged_rank = len(shape) - 1
if fill is None:
    fill = [0.8 for _ in shape]

# Build the inputs for the op.
rt_input = self._generateRaggedTensor(shape, ragged_rank, dtype, fill)
default_value = constant_op.constant(
    self._generateRaggedTensor(default_shape, 0, dtype), dtype=dtype)

mbs = np.prod(shape) / (2**20)
with session.Session(config=benchmark.benchmark_config()) as sess:
    extras = {
        'shape': shape,
        'ragged_rank': ragged_rank,
        'dtype': dtype,
        'fill': fill,
        'default_shape': default_shape
    }
    rt = ragged_factory_ops.constant(rt_input, dtype, ragged_rank=ragged_rank)

    # Inputs for with_splits:
    splits_rt_placeholder = ragged_factory_ops.placeholder(
        dtype, ragged_rank, shape[ragged_rank + 1:])
    splits_feed_dict = {splits_rt_placeholder: sess.run(rt)}

    # Inputs for with_rowids:
    rowids_feed_dict = {}
    rowids_rt_placeholder = rebuild_ragged_tensor_with_value_rowids(
        rt, rowids_feed_dict, sess)

    # Common arguments for benchmarks:
    run_op_benchmark_kwargs = dict(
        sess=sess,
        store_memory_usage=True,
        min_iters=min_iters,
        burn_iters=max(5, min_iters // 10),
        mbs=mbs,
        extras=extras)

    ragged_to_tensor_with_splits = splits_rt_placeholder.to_tensor(
        default_value=default_value)
    self.run_op_benchmark(
        op_or_tensor=ragged_to_tensor_with_splits.op,
        name='ragged_to_tensor_with_splits',
        feed_dict=splits_feed_dict,
        **run_op_benchmark_kwargs)

    ragged_to_tensor_with_rowids = rowids_rt_placeholder.to_tensor(
        default_value=default_value)
    self.run_op_benchmark(
        op_or_tensor=ragged_to_tensor_with_rowids.op,
        name='ragged_to_tensor_with_rowids',
        feed_dict=rowids_feed_dict,
        **run_op_benchmark_kwargs)
