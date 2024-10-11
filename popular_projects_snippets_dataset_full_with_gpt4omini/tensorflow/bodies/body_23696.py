# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base.py
if shard_info:
    full_shape_str = " ".join("%d" % d for d in shape) + " "
    slice_spec = ":".join(
        "%d,%d" % (o, s) for o, s in zip(shard_info.offset, shard_info.shape))
    shape_and_slice = full_shape_str + slice_spec
else:
    shape_and_slice = ""
self.wrapped_value = checkpoint_position.value_tensors(
    {VARIABLE_VALUE_KEY: shape_and_slice})[VARIABLE_VALUE_KEY]
self._checkpoint_position = checkpoint_position
