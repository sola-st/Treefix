# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py
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
exit(cost)
