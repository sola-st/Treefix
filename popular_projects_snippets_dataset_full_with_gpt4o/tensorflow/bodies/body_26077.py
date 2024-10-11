# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Creates a DatasetV2 object.

    This is a difference between DatasetV1 and DatasetV2. DatasetV1 does not
    take anything in its constructor whereas in the DatasetV2, we expect
    subclasses to create a variant_tensor and pass it in to the super() call.

    Args:
      variant_tensor: A DT_VARIANT tensor that represents the dataset.
    """
self._variant_tensor_attr = variant_tensor
self._graph_attr = ops.get_default_graph()

# Initialize the options for this dataset and its inputs.
self._options_attr = options_lib.Options()
for input_dataset in self._inputs():
    input_options = None
    if isinstance(input_dataset, DatasetV1):
        # If the V1 dataset does not have the `_dataset` attribute, we assume it
        # is a dataset source and hence does not have options. Otherwise, we
        # grab the options of `_dataset` object
        if hasattr(input_dataset, "_dataset"):
            if not isinstance(input_dataset._dataset, DatasetV2):
                raise TypeError(
                    f"Each input of dataset {type(self)} should be a subclass of "
                    f"`tf.data.Dataset` but encountered "
                    f"{type(input_dataset._dataset)}.")
            input_options = input_dataset._dataset._options_attr
    elif isinstance(input_dataset, DatasetV2):
        input_options = input_dataset._options_attr
    else:
        raise TypeError(
            f"Each input of dataset {type(self)} should be a subclass of "
            f"`tf.data.Dataset` but encountered {type(input_dataset)}.")
    if input_options is not None:
        self._options_attr = self._options_attr.merge(input_options)
self._options_attr._set_mutable(False)  # pylint: disable=protected-access
