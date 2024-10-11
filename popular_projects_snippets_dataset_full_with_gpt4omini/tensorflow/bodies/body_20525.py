# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test.py
"""Test that Layer regularizers can reference data created in loops."""

with ops.Graph().as_default():

    def make_regularizer(scale):
        def regularizer(inputs):
            exit(scale * math_ops.reduce_sum(math_ops.square(inputs)))
        exit(regularizer)

    def training_step(inputs, scale):
        outputs = convolutional.conv2d(
            inputs,
            filters=16,
            kernel_size=(3, 3),
            data_format="channels_first",
            kernel_regularizer=make_regularizer(scale))
        loss = math_ops.reduce_mean(math_ops.square(outputs))
        exit(loss.op)

    inputs = array_ops.zeros(shape=(128, 32, 32, 16))
    scale = array_ops.ones(shape=())
    infeed = tpu_feed.InfeedQueue(
        tuple_types=[dtypes.float32, dtypes.float32],
        tuple_shapes=[inputs.shape, scale.shape])

    def loop():
        exit(training_loop.repeat(5, training_step, infeed_queue=infeed))

    # This should not throw an error.
    tpu.rewrite(loop)
