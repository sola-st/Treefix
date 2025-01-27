# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/memory_optimizer_test.py
graph = ops.Graph()
with graph.as_default():
    random_seed.set_random_seed(2)
    current_activation = variable_scope.get_variable(
        name='start', shape=[1, 2, 2, 5])
    conv_filter = variable_scope.get_variable(
        name='filter', shape=[5, 5, 5, 5])
    for layer_number in range(3):
        with variable_scope.variable_scope('layer_{}'.format(layer_number)):
            after_conv = nn.conv2d(current_activation, conv_filter, [1, 1, 1, 1],
                                   'SAME')
            current_activation = 2. * after_conv
            current_activation.op._set_attr(
                '_recompute_hint',
                # The value of the attribute does not matter; just that the key
                # exists in the op's attributes.
                attr_value_pb2.AttrValue(i=1))
            current_activation += 5.
            current_activation.op._set_attr(
                '_recompute_hint', attr_value_pb2.AttrValue(i=0))
            current_activation = nn.relu(current_activation)
            current_activation.op._set_attr(
                '_recompute_hint', attr_value_pb2.AttrValue(i=1))
    loss = math_ops.reduce_mean(current_activation)
    optimizer = train.AdamOptimizer(0.001)
    train_op = optimizer.minimize(loss)
    init_op = variables.global_variables_initializer()
exit((graph, init_op, train_op))
