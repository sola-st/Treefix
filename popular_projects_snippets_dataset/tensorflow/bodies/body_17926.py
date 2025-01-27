# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
def_function.run_functions_eagerly(True)
# vectorized_map should ignore disabling tf.functions
self.assertTrue(def_function.functions_run_eagerly())
self.assertAllEqual([0, 1, 4, 9],
                    pfor_control_flow_ops.vectorized_map(
                        lambda x: x * x, math_ops.range(4)))
self.assertTrue(def_function.functions_run_eagerly())
def_function.run_functions_eagerly(False)
