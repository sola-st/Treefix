# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/readers.py
"""Creates (or validates) a dataset of filenames.

  Args:
    filenames: Either a list or dataset of filenames. If it is a list, it is
      convert to a dataset. If it is a dataset, its type and shape is validated.
    name: (Optional.) A name for the tf.data operation.

  Returns:
    A dataset of filenames.
  """
if isinstance(filenames, dataset_ops.DatasetV2):
    element_type = dataset_ops.get_legacy_output_types(filenames)
    if element_type != dtypes.string:
        raise TypeError(
            "The `filenames` argument must contain `tf.string` elements. Got a "
            f"dataset of `{element_type!r}` elements.")
    element_shape = dataset_ops.get_legacy_output_shapes(filenames)
    if not element_shape.is_compatible_with(tensor_shape.TensorShape([])):
        raise TypeError(
            "The `filenames` argument must contain `tf.string` elements of shape "
            "[] (i.e. scalars). Got a dataset of element shape "
            f"{element_shape!r}.")
else:
    filenames = nest.map_structure(_normalise_fspath, filenames)
    filenames = ops.convert_to_tensor(filenames, dtype_hint=dtypes.string)
    if filenames.dtype != dtypes.string:
        raise TypeError(
            "The `filenames` argument must contain `tf.string` elements. Got "
            f"`{filenames.dtype!r}` elements.")
    filenames = array_ops.reshape(filenames, [-1], name="flat_filenames")
    filenames = from_tensor_slices_op._TensorSliceDataset(  # pylint: disable=protected-access
        filenames,
        is_files=True,
        name=name)
exit(filenames)
