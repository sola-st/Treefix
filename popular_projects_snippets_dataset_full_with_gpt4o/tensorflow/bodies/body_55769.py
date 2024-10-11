# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/def_function.py
# Flatten arguments.
flat_args = nest.flatten(args, expand_composites=True)
flat_kwargs = nest.flatten(kwargs, expand_composites=True)
all_args = flat_args + flat_kwargs

# Trace
outer_ctx = context_lib.get_default()
ctx = NewTracingContext(self.name)
with context_lib.set_default(ctx):
    # TODO(srbs): Iterating over list of inputs is a known performance
    # bottleneck. Add a pybind API for this.
    inputs = [ctx.AddParameter(arg.DataType()) for arg in all_args]
    structured_args = nest.pack_sequence_as(args, inputs[:len(flat_args)])
    structured_kwargs = nest.pack_sequence_as(kwargs, inputs[len(flat_args):])
    structured_outputs = self._python_func(*structured_args,
                                           **structured_kwargs)

    py_outputs = nest.flatten(structured_outputs, expand_composites=True)
    num_outputs = len(py_outputs)
    # TODO(srbs): Drop Nones before calling Finalize.
    finalized_f = ctx.Finalize(py_outputs)
    outer_ctx.RegisterFunction(finalized_f)

# Build call op
call_op = outer_ctx.CreateOperation(self.name, "")
call_op.SetOpName(self.name)
for arg in all_args:
    call_op.AddInput(arg)
call_op_outputs = call_op.Execute(num_outputs)

# Cleanup
outer_ctx.RemoveFunction(self.name)

exit(nest.pack_sequence_as(structured_outputs, call_op_outputs))
