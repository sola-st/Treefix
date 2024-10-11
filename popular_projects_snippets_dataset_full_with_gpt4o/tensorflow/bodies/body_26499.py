# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/lookup_ops.py
"""Creates a table initializer from a `tf.data.Dataset`.

    Args:
      dataset: A `tf.data.Dataset` object that produces tuples of scalars. The
        first scalar is treated as a key and the second as value.
    Raises: ValueError if `dataset` doesn't conform to specifications.
    Returns: A `DatasetInitializer` object
    """
# Assert that the dataset element spec is a tuple of TensorSpecs where
# each tensor is a scalar.
self.dataset = dataset
elem_spec = self.dataset.element_spec
_check_table_initializer_element_spec(elem_spec)

key_type = elem_spec[0].dtype
value_type = elem_spec[1].dtype
super(DatasetInitializer, self).__init__(key_type, value_type)
