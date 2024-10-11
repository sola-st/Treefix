# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py

@deprecation.deprecated_arg_values("2016-07-04",
                                   "This is how you update...",
                                   warn_once=True,
                                   arg0=None)
def _fn(arg0):  # pylint: disable=unused-argument
    pass

ops.enable_tensor_equality()
initial_count = mock_warning.call_count
# Check that we avoid error from explicit `var == None` check.
_fn(arg0=variables.Variable(0))
self.assertEqual(initial_count, mock_warning.call_count)
_fn(arg0=None)
self.assertEqual(initial_count + 1, mock_warning.call_count)
ops.disable_tensor_equality()
