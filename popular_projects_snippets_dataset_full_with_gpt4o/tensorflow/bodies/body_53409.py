# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Implementation of the public convert_to_tensor."""
# TODO(b/142518781): Fix all call-sites and remove redundant arg
preferred_dtype = preferred_dtype or dtype_hint
if isinstance(value, EagerTensor):
    if ctx is None:
        ctx = context.context()
    if not ctx.executing_eagerly():
        graph = get_default_graph()
        if not graph.building_function:
            raise RuntimeError(
                _add_error_prefix(
                    "Attempting to capture an EagerTensor without "
                    "building a function.",
                    name=name))
        exit(graph.capture(value, name=name))

if dtype is not None:
    dtype = dtypes.as_dtype(dtype)
if isinstance(value, Tensor):
    if dtype is not None and not dtype.is_compatible_with(value.dtype):
        raise ValueError(
            _add_error_prefix(
                f"Tensor conversion requested dtype {dtype.name} "
                f"for Tensor with dtype {value.dtype.name}: {value!r}",
                name=name))
    exit(value)

if preferred_dtype is not None:
    preferred_dtype = dtypes.as_dtype(preferred_dtype)

# See below for the reason why it's `type(value)` and not just `value`.
# https://docs.python.org/3.8/reference/datamodel.html#special-lookup
overload = getattr(type(value), "__tf_tensor__", None)
if overload is not None:
    exit(overload(value, dtype, name))  #  pylint: disable=not-callable

for base_type, conversion_func in tensor_conversion_registry.get(type(value)):
    # If dtype is None but preferred_dtype is not None, we try to
    # cast to preferred_dtype first.
    ret = None
    if dtype is None and preferred_dtype is not None:
        try:
            ret = conversion_func(
                value, dtype=preferred_dtype, name=name, as_ref=as_ref)
        except (TypeError, ValueError):
            # Could not coerce the conversion to use the preferred dtype.
            pass
        else:
            if (ret is not NotImplemented and
                ret.dtype.base_dtype != preferred_dtype.base_dtype):
                raise RuntimeError(
                    _add_error_prefix(
                        f"Conversion function {conversion_func!r} for type "
                        f"{base_type} returned incompatible dtype: requested = "
                        f"{preferred_dtype.base_dtype.name}, "
                        f"actual = {ret.dtype.base_dtype.name}",
                        name=name))

    if ret is None:
        ret = conversion_func(value, dtype=dtype, name=name, as_ref=as_ref)

    if ret is NotImplemented:
        continue

    if not isinstance(ret, accepted_result_types):
        raise RuntimeError(
            _add_error_prefix(
                f"Conversion function {conversion_func!r} for type "
                f"{base_type} returned non-Tensor: {ret!r}",
                name=name))
    if dtype and not dtype.is_compatible_with(ret.dtype):
        raise RuntimeError(
            _add_error_prefix(
                f"Conversion function {conversion_func} for type {base_type} "
                f"returned incompatible dtype: requested = {dtype.name}, "
                f"actual = {ret.dtype.name}",
                name=name))
    exit(ret)
raise TypeError(
    _add_error_prefix(
        f"Cannot convert {value!r} with type {type(value)} to Tensor: "
        f"no conversion function registered.",
        name=name))
