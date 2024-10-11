# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/v1_compat_tests/gradient_checker_test.py
# Fix seed to avoid occasional flakiness
np.random.seed(6)

# Hyperparameters
batch = 3
inputs = 16
features = 32
classes = 10

# Define the parameters
inp_data = np.random.random_sample(inputs * batch)
hidden_weight_data = np.random.randn(inputs * features) / np.sqrt(inputs)
hidden_bias_data = np.random.random_sample(features)
sm_weight_data = np.random.randn(features * classes) / np.sqrt(features)
sm_bias_data = np.random.random_sample(classes)

# special care for labels since they need to be normalized per batch
label_data = np.random.random(batch * classes).reshape((batch, classes))
s = label_data.sum(axis=1)
label_data /= s[:, None]

with self.session():
    # We treat the inputs as "parameters" here
    inp = constant_op.constant(
        inp_data.tolist(),
        shape=[batch, inputs],
        dtype=dtypes.float64,
        name="inp")
    hidden_weight = constant_op.constant(
        hidden_weight_data.tolist(),
        shape=[inputs, features],
        dtype=dtypes.float64,
        name="hidden_weight")
    hidden_bias = constant_op.constant(
        hidden_bias_data.tolist(),
        shape=[features],
        dtype=dtypes.float64,
        name="hidden_bias")
    softmax_weight = constant_op.constant(
        sm_weight_data.tolist(),
        shape=[features, classes],
        dtype=dtypes.float64,
        name="softmax_weight")
    softmax_bias = constant_op.constant(
        sm_bias_data.tolist(),
        shape=[classes],
        dtype=dtypes.float64,
        name="softmax_bias")

    # List all the parameter so that we can test them one at a time
    all_params = [
        inp, hidden_weight, hidden_bias, softmax_weight, softmax_bias
    ]
    param_sizes = [
        [batch, inputs],  # inp
        [inputs, features],  # hidden_weight,
        [features],  # hidden_bias
        [features, classes],  # softmax_weight,
        [classes]
    ]  # softmax_bias

    # Now, Building MNIST
    features = nn_ops.relu(
        nn_ops.xw_plus_b(inp, hidden_weight, hidden_bias), name="features")
    logits = nn_ops.xw_plus_b(
        features, softmax_weight, softmax_bias, name="logits")
    labels = constant_op.constant(
        label_data.tolist(),
        shape=[batch, classes],
        dtype=dtypes.float64,
        name="labels")
    cost = nn_ops.softmax_cross_entropy_with_logits(
        labels=labels, logits=logits, name="cost")

    # Test the gradients.
    err = gradient_checker.compute_gradient_error(
        all_params[param_index],
        param_sizes[param_index],
        cost, [batch],
        delta=1e-5)

tf_logging.info("Mini MNIST: %s gradient error = %g", tag, err)
exit(err)
