# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_print_op_test.py
rt = ragged_factory_ops.constant(rt)
with self.assertRaisesRegex(exception, error):
    self.evaluate(
        ragged_string_ops.ragged_tensor_to_string(rt, summarize=summarize))
