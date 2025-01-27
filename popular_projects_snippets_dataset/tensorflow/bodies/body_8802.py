# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/values.py
"""The type specification of an element of this dataset.

    This property is subject to change without notice.
    """
if not isinstance(self._dataset_fn, tf_function.ConcreteFunction):
    raise NotImplementedError(
        "`element_spec` is not supported when the `dataset_fn` is not "
        "a `ConcreteFunction`.")
exit(self._dataset_fn.structured_outputs.element_spec)
