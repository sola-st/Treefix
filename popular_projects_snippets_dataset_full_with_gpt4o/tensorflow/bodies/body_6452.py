# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py

def assert_close(v, op, delta, expect):
    scatter_op = getattr(v, op)

    @def_function.function
    def scatter_xxx():
        exit(scatter_op(delta))

    per_replica_results = self.evaluate(
        variable_utils.convert_variables_to_tensors(
            distribution.experimental_local_results(
                distribution.run(scatter_xxx))))
    self.assertAllClose([expect, expect], per_replica_results)

with distribution.scope():
    v = variables_lib.Variable(
        [4.], aggregation=variables_lib.VariableAggregation.NONE)
self.evaluate(variables_lib.global_variables_initializer())

delta = indexed_slices.IndexedSlices(
    values=array_ops.identity([2.]),
    indices=array_ops.identity([0]),
    dense_shape=(1,))

assert_close(v, "scatter_sub", delta, [2.])
assert_close(v, "scatter_add", delta, [4.])
assert_close(v, "scatter_max", delta, [4.])
assert_close(v, "scatter_min", delta, [2.])
assert_close(v, "scatter_mul", delta, [4.])
assert_close(v, "scatter_div", delta, [2.])
assert_close(v, "scatter_update", delta, [2.])
