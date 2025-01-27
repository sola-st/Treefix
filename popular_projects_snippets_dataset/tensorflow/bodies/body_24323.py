# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
check_numerics_callback.enable_check_numerics(
    stack_height_limit=123, path_length_limit=1200)
fake_get_check_numerics_error_message = test.mock.MagicMock(
    return_value="dummy_message")
with test.mock.patch.object(check_numerics_callback,
                            "get_check_numerics_error_message",
                            fake_get_check_numerics_error_message):
    x = constant_op.constant(2.0)
    y = constant_op.constant(0.0)
    self._assertRaisesInvalidArgumentErrorAndGetMessage(
        lambda: x / y)  # Expected to generate an inf.
    (_, call_kwargs) = fake_get_check_numerics_error_message.call_args
    self.assertEqual(call_kwargs["stack_height_limit"], 123)
    self.assertEqual(call_kwargs["path_length_limit"], 1200)
