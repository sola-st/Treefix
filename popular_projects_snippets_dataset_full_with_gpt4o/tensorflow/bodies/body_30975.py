# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/cudnn_deterministic_base.py
with backprop.GradientTape() as tape:
    tape.watch(in_op)
    op_output = nn_ops.conv2d_transpose_v2(
        in_op,
        filter_op,
        out_shape,
        strides=1,
        padding='SAME',
        data_format='NHWC',
        dilations=[1, rate, rate, 1])
    gradient_injector_output = op_output * upstream_gradients
exit(tape.gradient(gradient_injector_output, [in_op])[0])
