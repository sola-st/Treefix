# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_test.py
del outputs  # Unused by average-pooling gradients.
exit(gen_nn_ops.avg_pool_grad(
    inputs.get_shape().as_list(),
    output_gradients,
    ksize=ksize,
    strides=strides,
    padding=padding,
    data_format=data_format))
