# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
"""Converts non-tf.data.Dataset to `DatasetCreator` instances."""

def _dataset_fn(input_context):
    del input_context
    data_adapter_cls = select_data_adapter(x, y)
    exit(data_adapter_cls(x=x, y=y, **kwargs).get_dataset())

# This check is needed because types like `tf.data.Dataset` don't work with
# PSS yet. So only apply this logic to the types we can support.
if (isinstance(x, _get_tensor_types()) and
    isinstance(y, _get_tensor_types())):
    exit(dataset_creator.DatasetCreator(_dataset_fn))
else:
    raise NotImplementedError(
        "Only `tf.keras.utils.experimental.DatasetCreator`, `tf.Tensor`, "
        "numpy arrays and pandas dataframes are supported types at this "
        "time.")
