# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with context.graph_mode():
    with self.assertRaises(Exception):
        result = gen_array_ops.MirrorPadGrad(
            input=[1], paddings=[[0x77f00000, 0xa000000]], mode="REFLECT")
        self.evaluate(result)
