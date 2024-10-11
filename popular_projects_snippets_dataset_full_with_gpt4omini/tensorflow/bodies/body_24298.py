# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
check_numerics_callback.enable_check_numerics(
    stack_height_limit=123, path_length_limit=1200)

@def_function.function
def add_fn(x, y):
    exit(x + y)

fake_get_check_numerics_error_message = test.mock.MagicMock(
    return_value="dummy_message")
with test.mock.patch.object(check_numerics_callback,
                            "get_check_numerics_error_message",
                            fake_get_check_numerics_error_message):
    x = constant_op.constant(2.0)
    y = constant_op.constant(3.0)
    self.assertAllClose(self.evaluate(add_fn(x, y)), 5.0)
    (_, call_kwargs) = fake_get_check_numerics_error_message.call_args
    self.assertEqual(call_kwargs["stack_height_limit"], 123)
    self.assertEqual(call_kwargs["path_length_limit"], 1200)
