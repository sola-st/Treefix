# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
"""Test that the TensorFlow implementation of
    total_variation(x_np) calculates the values in y_np.

    Note that these may be float-numbers so we only test
    for approximate equality within some narrow error-bound.
    """

# Create a TensorFlow session.
with self.cached_session():
    # Add a constant to the TensorFlow graph that holds the input.
    x_tf = constant_op.constant(x_np, shape=x_np.shape)

    # Add ops for calculating the total variation using TensorFlow.
    y = image_ops.total_variation(images=x_tf)

    # Run the TensorFlow session to calculate the result.
    y_tf = self.evaluate(y)

    # Assert that the results are as expected within
    # some small error-bound in case they are float-values.
    self.assertAllClose(y_tf, y_np)
