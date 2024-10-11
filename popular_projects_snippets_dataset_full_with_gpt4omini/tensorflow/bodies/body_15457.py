# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_to_tensor_op_test.py

rt = ragged_factory_ops.constant(rt_input, ragged_rank=ragged_rank)
with self.assertRaisesRegex(error_type, error):
    self.evaluate(rt.to_tensor(default_value=default, shape=shape))
rt_placeholder = nest.map_structure(
    make_placeholder, rt, expand_composites=True)
with self.assertRaisesRegex(error_type, error):
    self.evaluate(
        rt_placeholder.to_tensor(default_value=default, shape=shape))
