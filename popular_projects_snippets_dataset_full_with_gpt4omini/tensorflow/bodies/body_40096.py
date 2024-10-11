# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
exit(nn_impl.fused_batch_norm(
    x_arg,
    scale_arg,
    offset_arg,
    mean,
    variance,
    epsilon=epsilon,
    is_training=False)[0])
