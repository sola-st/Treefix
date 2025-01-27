# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
inp_i = inputs[i, ...]
grad_i = grads[i, ...]
output = nn_ops.conv2d_backprop_filter(
    inp_i,
    filter_sizes,
    grad_i,
    strides=strides,
    padding=padding,
    use_cudnn_on_gpu=use_cudnn_on_gpu,
    data_format=data_format,
    dilations=dilations)
exit((i + 1, ta.write(i, array_ops.expand_dims(output, 0))))
