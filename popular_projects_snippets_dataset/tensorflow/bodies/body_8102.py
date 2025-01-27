# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable.py
"""Treats `variables` as shards of a larger Variable.


    Example:

    ```
    variables = [
      tf.Variable(..., shape=(10, 100), dtype=tf.float32),
      tf.Variable(..., shape=(15, 100), dtype=tf.float32),
      tf.Variable(..., shape=(5, 100), dtype=tf.float32)
    ]
    sharded_variable = ShardedVariableMixin(variables)
    assert sharded_variable.shape.as_list() == [30, 100]
    ```

    Args:
      variables: A list of `ResourceVariable`s that comprise this sharded
        variable. Variables should not be shared between different
        `ShardedVariableMixin` objects.
      name: String. Name of this container. Defaults to "ShardedVariable".
    """
super(ShardedVariableMixin, self).__init__()
self._variables = variables
self._name = name

if not isinstance(variables, Sequence) or not variables or any(
    not isinstance(v, variables_lib.Variable) for v in variables):
    raise TypeError('Argument `variables` should be a non-empty list of '
                    f'`variables.Variable`s. Received {variables}')

var_dtypes = {v.dtype for v in variables}
if len(var_dtypes) > 1:
    raise ValueError(
        'All elements in argument `variables` must have the same dtype. '
        f'Received dtypes: {[v.dtype for v in variables]}')

first_var = variables[0]
self._dtype = first_var.dtype

# All variables must have the same shape for axes > 0.
higher_dim_shapes = {tuple(v.shape.as_list()[1:]) for v in variables}
if len(higher_dim_shapes) > 1:
    raise ValueError(
        'All elements in argument `variables` must have the same shapes '
        'except for the first axis. '
        f'Received shapes: {[v.shape for v in variables]}')
first_dim = sum(int(v.shape.as_list()[0]) for v in variables)
self._shape = tensor_shape.TensorShape([first_dim] +
                                       first_var.shape.as_list()[1:])

for v in variables:
    v._sharded_container = weakref.ref(self)

self._var_offsets = [
    [0 for _ in range(len(first_var.shape))] for _ in range(len(variables))
]
for i in range(1, len(variables)):
    # Always partition on the first axis. Offsets on other axes are 0.
    self._var_offsets[i][0] += (
        self._var_offsets[i - 1][0] + variables[i - 1].shape.as_list()[0])

save_slice_info = [v._get_save_slice_info() for v in variables]  # pylint: disable=protected-access
if any(slice_info is not None for slice_info in save_slice_info):
    raise ValueError(
        '`SaveSliceInfo` should not be set for all elements in argument '
        '`variables`. `ShardedVariable` will infer `SaveSliceInfo` according '
        'to the order of the elements `variables`. '
        f'Received save slice info {save_slice_info}')

# We create an uninitialized saving_variable with the full shape, which can
# be later captured in signatures so that the signatures can treat this
# ShardedVariable as one single variable.
self._saving_variable = resource_variable_ops.UninitializedVariable(
    shape=self._shape, dtype=self._dtype, name=self._name,
    trainable=self._variables[0].trainable,
    synchronization=variables_lib.VariableSynchronization.NONE,
    aggregation=variables_lib.VariableAggregation.NONE)
