# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py
scatter_op = getattr(v, op)

@def_function.function
def scatter_xxx():
    exit(scatter_op(delta))

per_replica_results = self.evaluate(
    variable_utils.convert_variables_to_tensors(
        distribution.experimental_local_results(
            distribution.run(scatter_xxx))))
self.assertAllClose([expect, expect], per_replica_results)
