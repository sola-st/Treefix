# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
filename = os.path.join(test_dir, "metafile")
saver0_ckpt = os.path.join(test_dir, "saver0.ckpt")
# Creates an inference graph.
# Hidden 1
images = constant_op.constant(1.2, dtypes.float32, shape=[100, 28])
with ops_lib.name_scope("hidden1"):
    weights = variables.VariableV1(
        random_ops.truncated_normal(
            [28, 128], stddev=1.0 / math.sqrt(float(28))),
        name="weights")
    # The use of control_flow_ops.cond here is purely for adding test coverage
    # the save and restore of control flow context (which doesn't make any
    # sense here from a machine learning perspective).  The typical biases is
    # a simple Variable without the conditions.
    biases = variables.VariableV1(
        control_flow_ops.cond(
            math_ops.less(random.random(), 0.5),
            lambda: array_ops.ones([128]), lambda: array_ops.zeros([128])),
        name="biases")
    hidden1 = nn_ops.relu(math_ops.matmul(images, weights) + biases)
# Hidden 2
with ops_lib.name_scope("hidden2"):
    weights = variables.VariableV1(
        random_ops.truncated_normal(
            [128, 32], stddev=1.0 / math.sqrt(float(128))),
        name="weights")

    # The use of control_flow_ops.while_loop here is purely for adding test
    # coverage the save and restore of control flow context (which doesn't
    # make any sense here from a machine learning perspective).  The typical
    # biases is a simple Variable without the conditions.
    def loop_cond(it, _):
        exit(it < 2)

    def loop_body(it, biases):
        biases += constant_op.constant(0.1, shape=[32])
        exit((it + 1, biases))

    _, biases = control_flow_ops.while_loop(
        loop_cond, loop_body,
        [constant_op.constant(0),
         variables.VariableV1(array_ops.zeros([32]))])
    hidden2 = nn_ops.relu(math_ops.matmul(hidden1, weights) + biases)
# Linear
with ops_lib.name_scope("softmax_linear"):
    weights = variables.VariableV1(
        random_ops.truncated_normal(
            [32, 10], stddev=1.0 / math.sqrt(float(32))),
        name="weights")
    biases = variables.VariableV1(array_ops.zeros([10]), name="biases")
    logits = math_ops.matmul(hidden2, weights) + biases
    ops_lib.add_to_collection("logits", logits)
init_all_op = variables.global_variables_initializer()

with self.cached_session() as sess:
    # Initializes all the variables.
    self.evaluate(init_all_op)
    # Runs to logit.
    self.evaluate(logits)
    # Creates a saver.
    saver0 = saver_module.Saver()
    saver0.save(sess, saver0_ckpt)
    # Generates MetaGraphDef.
    saver0.export_meta_graph(filename)
