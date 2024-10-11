# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
# Test that we can import a meta graph into a namescope.
test_dir = self._get_test_dir("import_into_namescope")
filename = os.path.join(test_dir, "ckpt")
# train.Saver is V1 only API.
with ops_lib.Graph().as_default():
    image = array_ops.placeholder(dtypes.float32, [None, 784], name="image")
    label = array_ops.placeholder(dtypes.float32, [None, 10], name="label")
    with session.Session() as sess:
        weights = variables.VariableV1(
            random_ops.random_uniform([784, 10]), name="weights")
        bias = variables.VariableV1(array_ops.zeros([10]), name="bias")
        logit = nn_ops.relu(
            math_ops.matmul(image, weights) + bias, name="logits")
        nn_ops.softmax(logit, name="prediction")
        cost = nn_ops.softmax_cross_entropy_with_logits(
            labels=label, logits=logit, name="cost")
        adam.AdamOptimizer().minimize(cost, name="optimize")
        saver = saver_module.Saver()
        self.evaluate(variables.global_variables_initializer())
        saver.save(sess, filename)

graph = ops_lib.Graph()
with session.Session(graph=graph) as sess:
    new_saver = saver_module.import_meta_graph(
        filename + ".meta", graph=graph, import_scope="new_model")
    new_saver.restore(sess, filename)
    sess.run(["new_model/optimize"], {
        "new_model/image:0": np.random.random([1, 784]),
        "new_model/label:0": np.random.randint(
            10, size=[1, 10])
    })
