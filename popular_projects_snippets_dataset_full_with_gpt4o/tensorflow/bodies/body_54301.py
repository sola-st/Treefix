# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
# Operation cannot be converted to Tensor.
op = control_flow_ops.no_op()
with self.assertRaisesRegex(TypeError,
                            "can't convert Operation '.+' to Tensor"):
    ops.convert_to_tensor(op)
