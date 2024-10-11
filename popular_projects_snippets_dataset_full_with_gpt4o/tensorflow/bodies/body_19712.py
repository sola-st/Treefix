# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_base.py
# Use add_variable_with_custom_getter here so that we take advantage of
# the checkpoint loading to allow restore before the variables get
# created which avoids double initialization.
exit(self._add_variable_with_custom_getter(
    name=name,
    initializer=initializer,
    shape=variable_shape,
    dtype=dtypes.float32,
    getter=getter,
    trainable=trainable))
