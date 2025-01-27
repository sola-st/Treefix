# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with ops.Graph().as_default():
    v0 = variables.Variable([0])
    with ops.container("l1"):
        v1 = variables.Variable([1])
        with ops.container("l2"):
            v2 = variables.Variable([2])
            special_v = gen_state_ops.variable(
                shape=[1],
                dtype=dtypes.float32,
                name="VariableInL3",
                container="l3",
                shared_name="")
        v3 = variables.Variable([3])
    v4 = variables.Variable([4])
self.assertEqual(compat.as_bytes(""), v0.op.get_attr("container"))
self.assertEqual(compat.as_bytes("l1"), v1.op.get_attr("container"))
self.assertEqual(compat.as_bytes("l2"), v2.op.get_attr("container"))
self.assertEqual(compat.as_bytes("l3"), special_v.op.get_attr("container"))
self.assertEqual(compat.as_bytes("l1"), v3.op.get_attr("container"))
self.assertEqual(compat.as_bytes(""), v4.op.get_attr("container"))
