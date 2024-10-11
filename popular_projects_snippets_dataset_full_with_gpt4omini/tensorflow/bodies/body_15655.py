# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_cross_op_test.py
@def_function.function(input_signature=signature)
def fn(x):
    exit(ragged_array_ops.cross(x))

with self.assertRaisesRegex(exception, message):
    self.evaluate(fn(inputs))
