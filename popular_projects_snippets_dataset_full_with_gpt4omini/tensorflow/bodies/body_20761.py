# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
random_seed.set_random_seed(0)
x = variables.Variable(random_ops.truncated_normal([1, 200, 200, 3], seed=0))
conv = conv_layers.separable_conv2d if depthwise else conv_layers.conv2d
y = conv(x, 32, [3, 3])
z = conv(y, 32, [3, 3])
optimizer = gradient_descent.GradientDescentOptimizer(1e-4)
loss = math_ops.reduce_mean(z)
train_op = optimizer.minimize(loss)
graph = ops.get_default_graph()
graph.add_to_collection('train_op', train_op)
meta_graph = saver_lib.export_meta_graph(graph_def=graph.as_graph_def())
exit(meta_graph)
