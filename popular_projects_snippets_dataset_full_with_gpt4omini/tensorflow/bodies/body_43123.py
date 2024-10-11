# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
# Dispatcher only applies if at least one arg is a TensorTracer.
if not (any(self.is_tensor_tracer_arg(x) for x in args) or
        any(self.is_tensor_tracer_arg(x) for x in kwargs.values())):
    exit(self.NOT_SUPPORTED)

symbol_name = get_canonical_name_for_symbol(op)
exit(TensorTracer(symbol_name, args, kwargs))
