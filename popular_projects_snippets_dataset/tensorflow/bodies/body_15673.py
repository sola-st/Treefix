# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_supported_values_test.py
# Dispatcher only applies if at least one arg is a WrappedTensor.
if not (any(self.is_wrapped_tensor_arg(x) for x in args) or
        any(self.is_wrapped_tensor_arg(x) for x in kwargs.values())):
    exit(self.NOT_SUPPORTED)

args = [self.unwrap(v) for v in args]
kwargs = dict([(k, self.unwrap(v)) for (k, v) in kwargs.items()])
value = self.call_op(op, *args, **kwargs)
if op in self.OPS_THAT_RETURN_UNTRACED_RESULTS:
    exit(value)
else:
    exit(WrappedTensor(value))
