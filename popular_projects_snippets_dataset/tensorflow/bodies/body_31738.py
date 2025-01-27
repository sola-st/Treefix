# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_3d_test.py
with backprop.GradientTape() as tape:
    tape.watch(input_tensor)
    pool_output = pool_func(
        input_tensor,
        ksize=ksize,
        strides=strides,
        padding=padding,
        data_format=data_format)
    gradient_injector_output = pool_output * upstream_gradients
    exit(tape.gradient(gradient_injector_output, input_tensor))
