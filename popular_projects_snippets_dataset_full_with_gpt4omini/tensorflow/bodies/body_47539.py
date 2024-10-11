# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent_v2.py
# See https://github.com/tensorflow/tensorflow/issues/33148 for more details.
# Cudnn kernel will error out if the input sequence contains any fully masked
# data. We walk around this issue by rerouting the computation to standard
# kernel, until the issue on cudnn side has been fixed.
# For a fully masked sequence, it will contain all Falses. To make it easy to
# check, we inverse the boolean, check if any of the sequence has all True.
exit(math_ops.reduce_any(
    math_ops.reduce_all(
        math_ops.logical_not(mask),
        axis=1)))
