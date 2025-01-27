# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
test_dir = self._get_test_dir("scoped_copy")
saver0_ckpt = os.path.join(test_dir, "saver0.ckpt")
graph1 = ops_lib.Graph()
with graph1.as_default():
    with ops_lib.name_scope("hidden1"):
        images = constant_op.constant(
            1.0, dtypes.float32, shape=[3, 2], name="images")
        weights1 = variables.VariableV1(
            [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], name="weights")
        biases1 = variables.VariableV1([0.1] * 3, name="biases")
        nn_ops.relu(math_ops.matmul(images, weights1) + biases1, name="relu")

    # Run the graph and save scoped checkpoint.
with graph1.as_default(), self.session(graph=graph1) as sess:
    self.evaluate(variables.global_variables_initializer())
    _, var_list_1 = meta_graph.export_scoped_meta_graph(
        export_scope="hidden1")
    saver = saver_module.Saver(var_list=var_list_1, max_to_keep=1)
    saver.save(sess, saver0_ckpt, write_state=False)

expected = np.reshape([[5.0999999, 7.0999999, 9.10000038] * 3], (3, 3))

# Verifies copy to the same graph with the same name fails.
with graph1.as_default():
    with self.assertRaisesWithPredicateMatch(
        ValueError, lambda e: "need to be different" in str(e)):
        meta_graph.copy_scoped_meta_graph(
            from_scope="hidden1", to_scope="hidden1")

    # Verifies copy to the same graph.
with graph1.as_default():
    var_list_2 = meta_graph.copy_scoped_meta_graph(
        from_scope="hidden1", to_scope="hidden2")

with graph1.as_default(), self.session(graph=graph1) as sess:
    saver1 = saver_module.Saver(var_list=var_list_1, max_to_keep=1)
    saver1.restore(sess, saver0_ckpt)
    saver2 = saver_module.Saver(var_list=var_list_2, max_to_keep=1)
    saver2.restore(sess, saver0_ckpt)
    self.assertAllClose(expected, sess.run("hidden1/relu:0"))
    self.assertAllClose(expected, sess.run("hidden2/relu:0"))

# Verifies copy to different graph.
graph2 = ops_lib.Graph()
with graph2.as_default():
    new_var_list_1 = meta_graph.copy_scoped_meta_graph(
        from_scope="hidden1",
        to_scope="new_hidden1",
        from_graph=graph1,
        to_graph=graph2)

    with self.session() as sess:
        saver3 = saver_module.Saver(var_list=new_var_list_1, max_to_keep=1)
        saver3.restore(sess, saver0_ckpt)
        self.assertAllClose(expected, sess.run("new_hidden1/relu:0"))
