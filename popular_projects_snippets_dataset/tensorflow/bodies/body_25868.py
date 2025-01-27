# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/window_op.py
"""See `window()` for more details."""
self._input_dataset = input_dataset
self._size = ops.convert_to_tensor(size, dtype=dtypes.int64, name="size")
self._shift = ops.convert_to_tensor(shift, dtype=dtypes.int64, name="shift")
self._stride = ops.convert_to_tensor(
    stride, dtype=dtypes.int64, name="stride")
self._drop_remainder = ops.convert_to_tensor(
    drop_remainder, dtype=dtypes.bool, name="drop_remainder")
self._structure = nest.pack_sequence_as(
    dataset_ops.get_legacy_output_classes(input_dataset),
    [
        dataset_ops.DatasetSpec(  # pylint: disable=g-complex-comprehension
            structure.convert_legacy_structure(output_type, output_shape,
                                               output_class))
        for output_class, output_shape, output_type in zip(
            nest.flatten(
                dataset_ops.get_legacy_output_classes(input_dataset)),
            nest.flatten(
                dataset_ops.get_legacy_output_shapes(input_dataset)),
            nest.flatten(
                dataset_ops.get_legacy_output_types(input_dataset)))
    ])
self._name = name
variant_tensor = gen_dataset_ops.window_dataset(
    input_dataset._variant_tensor,  # pylint: disable=protected-access
    size=self._size,
    shift=self._shift,
    stride=self._stride,
    drop_remainder=self._drop_remainder,
    **self._common_args)
super().__init__(input_dataset, variant_tensor)
