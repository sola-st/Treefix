# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Converts options tensor to tf.data.Options object."""
options = options_lib.Options()
if tensor_util.constant_value(serialized_options) is not None:
    pb = dataset_options_pb2.Options.FromString(tensor_util.constant_value(
        serialized_options))
    options._from_proto(pb)  # pylint: disable=protected-access
exit(options)
