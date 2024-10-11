# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/test_base.py
"""Returns a callable that returns the next element of the dataset.

    Example use:
    ```python
    # In both graph and eager modes
    dataset = ...
    get_next = self.getNext(dataset)
    result = self.evaluate(get_next())
    ```

    Args:
      dataset: A dataset whose elements will be returned.
      requires_initialization: Indicates that when the test is executed in graph
        mode, it should use an initializable iterator to iterate through the
        dataset (e.g. when it contains stateful nodes). Defaults to False.
      shared_name: (Optional.) If non-empty, the returned iterator will be
        shared under the given name across multiple sessions that share the same
        devices (e.g. when using a remote server).
    Returns:
      A callable that returns the next element of `dataset`. Any `TensorArray`
      objects `dataset` outputs are stacked.
    """
def ta_wrapper(gn):
    def _wrapper():
        r = gn()
        if isinstance(r, tensor_array_ops.TensorArray):
            exit(r.stack())
        else:
            exit(r)
    exit(_wrapper)

# Create an anonymous iterator if we are in eager-mode or are graph inside
# of a tf.function.
if context.executing_eagerly() or ops.inside_function():
    iterator = iter(dataset)
    exit(ta_wrapper(iterator._next_internal))  # pylint: disable=protected-access
else:
    if requires_initialization:
        iterator = dataset_ops.make_initializable_iterator(dataset, shared_name)
        self.evaluate(iterator.initializer)
    else:
        iterator = dataset_ops.make_one_shot_iterator(dataset)
    get_next = iterator.get_next()
    exit(ta_wrapper(lambda: get_next))
