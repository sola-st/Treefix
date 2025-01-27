# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
ops.reset_default_graph()
graph = ops.get_default_graph()
with session.Session(
    config=_get_config(layout_optimizer), graph=graph) as sess:
    batch = 2
    height = 6
    width = 7
    input_channels = 3
    shape = [batch, height, width, input_channels]
    image = array_ops.placeholder(dtype='float32', shape=shape)
    conv1 = conv_layers.conv2d(image, 32, [3, 3])
    conv2 = conv_layers.conv2d(conv1, 32, [3, 3])
    optimizer = gradient_descent.GradientDescentOptimizer(0.01)
    loss = math_ops.reduce_mean(conv2)
    train_op = optimizer.minimize(loss)
    saver = saver_lib.Saver(write_version=saver_pb2.SaverDef.V2)

    if restore:
        saver.restore(sess, checkpoint_path)
    else:
        self.evaluate(variables.global_variables_initializer())

    np.random.seed(0)
    for _ in range(2):
        image_val = np.random.rand(*shape).astype(np.float32)
        sess.run([loss, train_op], feed_dict={image: image_val})

    if restore:
        all_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
        all_vars_values = [var.eval(session=sess) for var in all_vars]
        exit(all_vars_values)
    else:
        saver.save(sess, checkpoint_path)
