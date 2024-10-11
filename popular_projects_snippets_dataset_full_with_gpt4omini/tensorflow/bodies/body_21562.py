# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
# Test that we import a graph without its devices and run successfully.
with ops_lib.Graph().as_default():
    with ops_lib.device("/job:ps/replica:0/task:0/device:GPU:0"):
        image = array_ops.placeholder(dtypes.float32, [None, 784], name="image")
        label = array_ops.placeholder(dtypes.float32, [None, 10], name="label")
        weights = variables.VariableV1(
            random_ops.random_uniform([784, 10]), name="weights")
        bias = variables.VariableV1(array_ops.zeros([10]), name="bias")
        logit = nn_ops.relu(math_ops.matmul(image, weights) + bias)
        nn_ops.softmax(logit, name="prediction")
        cost = nn_ops.softmax_cross_entropy_with_logits(labels=label,
                                                        logits=logit)
        adam.AdamOptimizer().minimize(cost, name="optimize")
    meta_graph_def = saver_module.export_meta_graph()

with session.Session(graph=ops_lib.Graph()) as sess:
    saver_module.import_meta_graph(
        meta_graph_def, clear_devices=False, import_scope="new_model")
    # Device refers to GPU, which is not available here.
    with self.assertRaises(errors_impl.InvalidArgumentError):
        self.evaluate(variables.global_variables_initializer())

with session.Session(graph=ops_lib.Graph()) as sess:
    saver_module.import_meta_graph(
        meta_graph_def, clear_devices=True, import_scope="new_model")
    self.evaluate(variables.global_variables_initializer())
    sess.run(["new_model/optimize"], {
        "new_model/image:0": np.random.random([1, 784]),
        "new_model/label:0": np.random.randint(
            10, size=[1, 10])
    })
