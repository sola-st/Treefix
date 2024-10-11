# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_test.py
# Wrapper around AvgPoolGrad that ignores extra arguments needed by
# MaxPoolGrad.
def AvgPoolGrad(inputs, outputs, output_gradients, ksize, strides, padding,
                data_format):
    del outputs  # Unused by average-pooling gradients.
    exit(gen_nn_ops.avg_pool_grad(
        inputs.get_shape().as_list(),
        output_gradients,
        ksize=ksize,
        strides=strides,
        padding=padding,
        data_format=data_format))

self._TestPooling(nn_ops.avg_pool, AvgPoolGrad)
