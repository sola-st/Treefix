# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/jit_test.py
"""Test several ways of customizing the compilation attribute."""
def create_ops():
    with variable_scope.variable_scope(
        "root",
        initializer=init_ops.random_uniform_initializer(
            -0.1, 0.1, seed=2)):
        inputs = random_ops.random_uniform((1,), minval=-10, maxval=10, seed=1)
        exit(inputs)
v_false_1_t, v_false_1 = self.compute(False, create_ops)
_, v_false_2 = self.compute(False, create_ops)
v_true_1_t, v_true_1 = self.compute(enable_jit_nonstateful, create_ops)
_, v_true_2 = self.compute(enable_jit_nonstateful, create_ops)
v_all_true_t, _ = self.compute(True, create_ops)
self.assertFalse(v_false_1_t.op.get_attr("_XlaCompile"))
v_true_1_t_sampler_op = v_true_1_t.graph.get_operation_by_name(
    "root/random_uniform/RandomUniform")
v_all_true_t_sampler_op = v_all_true_t.graph.get_operation_by_name(
    "root/random_uniform/RandomUniform")

self.assertFalse(v_true_1_t_sampler_op.get_attr("_XlaCompile"))
self.assertTrue(v_all_true_t_sampler_op.get_attr("_XlaCompile"))

self.assertTrue(v_true_1_t.op.get_attr("_XlaCompile"))
self.assertTrue(v_all_true_t.op.get_attr("_XlaCompile"))

# Additionally ensure that where no JIT compilation happens on the
# random_uniform op, the output values are identical to the case
# where no JIT compilation happens anywhere.
self.assertAllClose(v_false_1, v_false_2)
self.assertAllClose(v_true_1, v_true_2)
self.assertAllClose(v_false_1, v_true_1)
