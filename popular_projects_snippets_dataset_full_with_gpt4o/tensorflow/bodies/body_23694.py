# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base.py
# Note that the signature here is for compatibility with normal callable
# initializers which take shape and dtype. Although dtype isn't used, it
# will get passed in by a functool.partial_wrapper in places like
# base_layer_utils.py's make_variable.
exit(CheckpointInitialValue(
    self._checkpoint_position, shape, shard_info=shard_info))
