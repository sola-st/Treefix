# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
filename = os.path.join(test_dir, "metafile")
train_filename = os.path.join(test_dir, "train_metafile")
saver0_ckpt = os.path.join(test_dir, "saver0.ckpt")
with self.session(graph=ops_lib.Graph()) as sess:
    # Restores from MetaGraphDef.
    new_saver = saver_module.import_meta_graph(filename)
    # Generates a new MetaGraphDef.
    new_saver.export_meta_graph()
    # Restores from checkpoint.
    new_saver.restore(sess, saver0_ckpt)
    # Adds loss and train.
    labels = constant_op.constant(0, dtypes.int32, shape=[100], name="labels")
    batch_size = array_ops.size(labels)
    labels = array_ops.expand_dims(labels, 1)
    indices = array_ops.expand_dims(math_ops.range(0, batch_size), 1)
    concated = array_ops.concat([indices, labels], 1)
    onehot_labels = sparse_ops.sparse_to_dense(
        concated, array_ops.stack([batch_size, 10]), 1.0, 0.0)
    logits = ops_lib.get_collection("logits")[0]
    cross_entropy = nn_ops.softmax_cross_entropy_with_logits(
        labels=onehot_labels, logits=logits, name="xentropy")
    loss = math_ops.reduce_mean(cross_entropy, name="xentropy_mean")

    summary.scalar("loss", loss)
    # Creates the gradient descent optimizer with the given learning rate.
    optimizer = gradient_descent.GradientDescentOptimizer(0.01)

    # Runs train_op.
    train_op = optimizer.minimize(loss)
    ops_lib.add_to_collection("train_op", train_op)

    # Runs train_op.
    self.evaluate(train_op)

    # Generates MetaGraphDef.
    saver_module.export_meta_graph(train_filename)
