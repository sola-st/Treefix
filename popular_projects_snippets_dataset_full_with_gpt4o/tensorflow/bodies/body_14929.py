# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/raw_ops_test.py
if context.executing_eagerly():
    with self.assertRaisesRegex(
        errors.FailedPreconditionError,
        "GetSessionHandle called on null session state"):
        gen_data_flow_ops.GetSessionHandle(value=[1])
