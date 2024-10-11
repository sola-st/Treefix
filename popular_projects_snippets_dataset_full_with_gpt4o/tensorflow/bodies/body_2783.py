# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/examples/mnist/ops_defs.py
ksize = [1, filter_width, filter_height, 1]
strides = [1, stride_w, stride_h, 1]
exit(tf.raw_ops.MaxPool(
    input=input_, ksize=ksize, strides=strides, padding=padding))
