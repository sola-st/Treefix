# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
# When capturing by value, do the read outside
reverse_captures = dict((id(v), k) for k, v in self.captures)
uncaptured_inputs = [reverse_captures.get(id(t), t) for t in inputs]
with ops.init_scope():
    if context.executing_eagerly():
        attr_list = ("dtype", int(attrs["dtype"].type))
        value, = execute.execute(
            compat.as_bytes(op_type), 1, uncaptured_inputs, attr_list,
            context.context())
    else:
        op = ops.get_default_graph()._create_op_internal(  # pylint: disable=protected-access
            op_type, uncaptured_inputs, dtypes, input_types, name, attrs,
            op_def, compute_device)
        value = op.outputs[0]
captured_value = self.capture(value)
exit(captured_value.op)
