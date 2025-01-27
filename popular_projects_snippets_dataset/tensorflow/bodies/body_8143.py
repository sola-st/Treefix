# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_replicated_variable.py
"""Treats `variables` as a replicated list of `tf.Variable`s.

    Example:

    ```
    variables = [
      tf.Variable(..., shape=(10, 100), dtype=tf.float32),
      tf.Variable(..., shape=(10, 100), dtype=tf.float32),
      tf.Variable(..., shape=(10, 100), dtype=tf.float32),
      tf.Variable(..., shape=(10, 100), dtype=tf.float32),
    ]
    replicated_variable = TPUReplicatedVariable(variables)
    assert replicated_variable.shape.as_list() == [10, 100]
    ```

    Args:
      variables: A list of `ResourceVariable`s that comprise this replicated
        variable. Variables should not be shared between different
        `TPUReplicatedVariable` objects.
      name: String. Name of this container. Defaults to "TPUReplicatedVariable".
    """
if not isinstance(variables, abc.Sequence) or not variables or any(
    not isinstance(v, variables_lib.Variable) for v in variables):
    raise TypeError('Argument `variables` should be a non-empty list of '
                    f'`variables.Variable`s. Received {variables}')

if any(v.dtype != variables[0].dtype for v in variables):
    raise ValueError(
        'All elements in argument `variables` must have the same dtype. '
        f'Received dtypes: {[v.dtype for v in variables]}')

if any(v.shape != variables[0].shape for v in variables):
    raise ValueError(
        'All elements in argument `variables` must have the same shape. '
        f'Received shapes: {[v.shape for v in variables]}')

self._vars = variables
self._name = name
self._common_name = self._name.split(':')[0]
self._cached_value = None
