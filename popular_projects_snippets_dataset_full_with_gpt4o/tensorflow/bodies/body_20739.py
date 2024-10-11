# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/memory_optimizer_test.py
"""A simple layered graph with conv, an intermediate op, and a ReLU."""
graph = ops.Graph()
with graph.as_default():
    random_seed.set_random_seed(1)
    current_activation = variable_scope.get_variable(
        name='start', shape=[batch_size, image_dim, image_dim, 5])
    conv_filter = variable_scope.get_variable(
        name='filter', shape=[5, 5, 5, 5])
    for layer_number in range(10):
        with variable_scope.variable_scope('layer_{}'.format(layer_number)):
            after_conv = nn.conv2d(current_activation, conv_filter, [1, 1, 1, 1],
                                   'SAME')
            current_activation = 2. * after_conv
            current_activation = nn.relu(current_activation)
    loss = math_ops.reduce_mean(current_activation)
    with ops.name_scope(optimizer_scope_name):
        optimizer = train.AdamOptimizer(0.001)
        train_op = optimizer.minimize(loss)
    init_op = variables.global_variables_initializer()
    metagraph = train.export_meta_graph()
exit((metagraph, init_op.name, train_op.name, loss.name))
