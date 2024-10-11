# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/unique_op.py
"""See `tf.data.Dataset.unique` for details."""
self._input_dataset = input_dataset
for ty in nest.flatten(dataset_ops.get_legacy_output_types(input_dataset)):
    if ty not in (dtypes.int32, dtypes.int64, dtypes.string):
        raise TypeError(
            f"`tf.data.Dataset.unique` does not support type {ty} -- only "
            f"`tf.int32`, `tf.int64`, and `tf.string` are supported.")
self._name = name
variant_tensor = gen_experimental_dataset_ops.unique_dataset(
    self._input_dataset._variant_tensor,  # pylint: disable=protected-access
    **self._common_args)
super().__init__(input_dataset, variant_tensor)
