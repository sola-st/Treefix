# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/script_ops_test.py
value = constant_op.constant(value=[1, 2])
token = b"\xb0"
data_type = [dtypes.int32]
with self.assertRaises((errors.InternalError, UnicodeDecodeError)):
    self.evaluate(
        gen_script_ops.py_func(input=[value], token=token, Tout=data_type))
