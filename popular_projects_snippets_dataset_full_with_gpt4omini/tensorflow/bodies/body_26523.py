# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/writers.py
"""Writes a dataset to a TFRecord file.

    An operation that writes the content of the specified dataset to the file
    specified in the constructor.

    If the file exists, it will be overwritten.

    Args:
      dataset: a `tf.data.Dataset` whose elements are to be written to a file

    Returns:
      In graph mode, this returns an operation which when executed performs the
      write. In eager mode, the write is performed by the method itself and
      there is no return value.

    Raises
      TypeError: if `dataset` is not a `tf.data.Dataset`.
      TypeError: if the elements produced by the dataset are not scalar strings.
    """
if not isinstance(dataset, dataset_ops.DatasetV2):
    raise TypeError(
        f"Invalid `dataset.` Expected a `tf.data.Dataset` object but got "
        f"{type(dataset)}."
    )
if not dataset_ops.get_structure(dataset).is_compatible_with(
    tensor_spec.TensorSpec([], dtypes.string)):
    raise TypeError(
        f"Invalid `dataset`. Expected a`dataset` that produces scalar "
        f"`tf.string` elements, but got a dataset which produces elements "
        f"with shapes {dataset_ops.get_legacy_output_shapes(dataset)} and "
        f"types {dataset_ops.get_legacy_output_types(dataset)}.")
# pylint: disable=protected-access
dataset = dataset._apply_debug_options()
exit(gen_experimental_dataset_ops.dataset_to_tf_record(
    dataset._variant_tensor, self._filename, self._compression_type))
