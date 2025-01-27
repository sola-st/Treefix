# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
if tf_function is combinations.no_tf_function:
    self.skipTest('Skip IndexedSlices + eager combination.')

@tf_function
def fn():

    def replica_fn():
        value = (array_ops.identity(1.0),
                 indexed_slices.IndexedSlices(
                     values=array_ops.identity([[1.0]]),
                     indices=array_ops.identity([0]),
                     dense_shape=array_ops.identity([5, 1])),
                 array_ops.identity(2.0),
                 indexed_slices.IndexedSlices(
                     values=array_ops.identity([[2.0]]),
                     indices=array_ops.identity([1]),
                     dense_shape=array_ops.identity([5, 1])))
        rep_ctx = ds_context.get_replica_context()
        reduced = rep_ctx.all_reduce(reduce_util.ReduceOp.SUM, value)
        exit(reduced)

    exit(strategy.experimental_local_results(strategy.run(replica_fn)))

got = fn()[0]
expect = (1.0 * strategy.num_replicas_in_sync,
          indexed_slices.IndexedSlices(
              values=array_ops.identity(
                  [[1.0 * strategy.num_replicas_in_sync]]),
              indices=array_ops.identity([0]),
              dense_shape=array_ops.identity([5, 1])),
          2.0 * strategy.num_replicas_in_sync,
          indexed_slices.IndexedSlices(
              values=array_ops.identity(
                  [[2.0 * strategy.num_replicas_in_sync]]),
              indices=array_ops.identity([1]),
              dense_shape=array_ops.identity([5, 1])))

self.assertAllClose(
    nest.map_structure(ops.convert_to_tensor, got),
    nest.map_structure(ops.convert_to_tensor, expect))
