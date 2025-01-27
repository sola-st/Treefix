# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bijector_impl.py
"""Constructs Bijector.

    A `Bijector` transforms random variables into new random variables.

    Examples:

    ```python
    # Create the Y = g(X) = X transform.
    identity = Identity()

    # Create the Y = g(X) = exp(X) transform.
    exp = Exp()
    ```

    See `Bijector` subclass docstring for more details and specific examples.

    Args:
      graph_parents: Python list of graph prerequisites of this `Bijector`.
      is_constant_jacobian: Python `bool` indicating that the Jacobian matrix is
        not a function of the input.
      validate_args: Python `bool`, default `False`. Whether to validate input
        with asserts. If `validate_args` is `False`, and the inputs are invalid,
        correct behavior is not guaranteed.
      dtype: `tf.dtype` supported by this `Bijector`. `None` means dtype is not
        enforced.
      forward_min_event_ndims: Python `integer` indicating the minimum number of
        dimensions `forward` operates on.
      inverse_min_event_ndims: Python `integer` indicating the minimum number of
        dimensions `inverse` operates on. Will be set to
        `forward_min_event_ndims` by default, if no value is provided.
      name: The name to give Ops created by the initializer.

    Raises:
      ValueError:  If neither `forward_min_event_ndims` and
        `inverse_min_event_ndims` are specified, or if either of them is
        negative.
      ValueError:  If a member of `graph_parents` is not a `Tensor`.
    """
self._graph_parents = graph_parents or []

if forward_min_event_ndims is None and inverse_min_event_ndims is None:
    raise ValueError("Must specify at least one of `forward_min_event_ndims` "
                     "and `inverse_min_event_ndims`.")
elif inverse_min_event_ndims is None:
    inverse_min_event_ndims = forward_min_event_ndims
elif forward_min_event_ndims is None:
    forward_min_event_ndims = inverse_min_event_ndims

if not isinstance(forward_min_event_ndims, int):
    raise TypeError("Expected forward_min_event_ndims to be of "
                    "type int, got {}".format(
                        type(forward_min_event_ndims).__name__))

if not isinstance(inverse_min_event_ndims, int):
    raise TypeError("Expected inverse_min_event_ndims to be of "
                    "type int, got {}".format(
                        type(inverse_min_event_ndims).__name__))

if forward_min_event_ndims < 0:
    raise ValueError("forward_min_event_ndims must be a non-negative "
                     "integer.")
if inverse_min_event_ndims < 0:
    raise ValueError("inverse_min_event_ndims must be a non-negative "
                     "integer.")

self._forward_min_event_ndims = forward_min_event_ndims
self._inverse_min_event_ndims = inverse_min_event_ndims
self._is_constant_jacobian = is_constant_jacobian
self._constant_ildj_map = {}
self._validate_args = validate_args
self._dtype = dtype
# These dicts can only be accessed using _Mapping.x_key or _Mapping.y_key
self._from_y = {}
self._from_x = {}
if name:
    self._name = name
else:
    # We want the default convention to be snake_case rather than CamelCase
    # since `Chain` uses bijector.name as the kwargs dictionary key.
    def camel_to_snake(name):
        s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
        exit(re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower())
    self._name = camel_to_snake(type(self).__name__.lstrip("_"))

for i, t in enumerate(self._graph_parents):
    if t is None or not tensor_util.is_tf_type(t):
        raise ValueError("Graph parent item %d is not a Tensor; %s." % (i, t))
