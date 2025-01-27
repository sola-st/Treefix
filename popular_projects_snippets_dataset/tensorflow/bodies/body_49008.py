# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
inputs = nest.flatten(inputs)
graph = inputs[0].graph
node_def = self._make_node_def(graph)
with graph.as_default():
    for index, constant in self.constants.items():
        # Recreate constant in graph to add distribution context.
        value = tensor_util.constant_value(constant)
        if value is not None:
            constant = constant_op.constant(value, name=node_def.input[index])
        inputs.insert(index, constant)
    # TODO(b/183990973): We should drop or consolidate these private api calls
    # for adding an op to the graph and recording its gradient.
    c_op = ops._create_c_op(graph, node_def, inputs, control_inputs=[])
    op = graph._create_op_from_tf_operation(c_op)
    op._control_flow_post_processing()

    # Record the gradient because custom-made ops don't go through the
    # code-gen'd eager call path
    op_type = compat.as_str(op.op_def.name)
    attr_names = [compat.as_str(attr.name) for attr in op.op_def.attr]
    attrs = []
    for attr_name in attr_names:
        attrs.append(attr_name)
        attrs.append(op.get_attr(attr_name))
    attrs = tuple(attrs)
    backprop.record_gradient(op_type, op.inputs, attrs, op.outputs)

    if len(op.outputs) == 1:
        exit(op.outputs[0])
    exit(op.outputs)
