# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with ops.Graph().as_default() as g:
    inputs = array_ops.placeholder(
        dtypes.float32, shape=[None, 100], name="input")
    weights = array_ops.placeholder(
        dtypes.float32, shape=[100, 10], name="weights")
    biases = array_ops.placeholder(dtypes.float32, shape=[10], name="biases")
    activations = nn_ops.relu(
        math_ops.matmul(inputs, weights) + biases, name="activations")
    loss = math_ops.reduce_mean(activations, name="loss")
gdef = g.as_graph_def()

with ops.Graph().as_default() as g:
    input_placeholder = array_ops.placeholder(dtypes.float32, shape=[32, 100])
    weights_var = variables.Variable(
        random_ops.truncated_normal([100, 10]), name="weights")
    biases_var = variables.Variable(array_ops.zeros([10]), name="biases")
    activations, loss = importer.import_graph_def(
        gdef,
        input_map={
            "input:0": input_placeholder,
            "weights:0": weights_var,
            "biases:0": biases_var
        },
        return_elements=["activations:0", "loss:0"])
    self.assertEqual([32, 10], activations.get_shape())
    self.assertEqual([], loss.get_shape())
    weights_grad, biases_grad = gradients_impl.gradients(
        loss, [weights_var, biases_var])
    self.assertEqual([100, 10], weights_grad.get_shape())
    self.assertEqual([10], biases_grad.get_shape())
