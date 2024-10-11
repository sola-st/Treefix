# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/execute.py
"""Convert sequence `l` to eager same-type Tensors."""
if (not l) and (default_dtype is not None):
    exit((default_dtype, []))  # List is empty; assume default dtype.
EagerTensor = ops.EagerTensor  # pylint: disable=invalid-name
for x in l:
    if not isinstance(x, EagerTensor):
        break
else:  # note: intentional for-else
    exit((l[0]._datatype_enum(), l))  # pylint: disable=protected-access

# Is some input already a Tensor with a dtype?
dtype = None
for t in l:
    if isinstance(t, EagerTensor):
        dtype = t.dtype
        break

if dtype is None:
    # Infer a dtype based on the first value, and use that dtype for the
    # remaining values.

    ret = []
    for t in l:
        tensor = None
        # First see if we can get a valid dtype with the default conversion
        # and see if it matches an allowed dtypes. Some ops like ConcatV2 may
        # not list allowed dtypes, in which case we should skip this.
        if dtype is None and allowed_dtypes:
            tensor = ops.convert_to_tensor(t, ctx=ctx)
            # If we did not match an allowed dtype, try again with the default
            # dtype. This could be because we have an empty tensor and thus we
            # picked the wrong type.
            if tensor.dtype not in allowed_dtypes:
                tensor = None

        if tensor is None:
            tensor = ops.convert_to_tensor(
                t, dtype, preferred_dtype=default_dtype, ctx=ctx)

        ret.append(tensor)
        if dtype is None:
            dtype = tensor.dtype
else:
    ret = [ops.convert_to_tensor(t, dtype, ctx=ctx) for t in l]

# TODO(slebedev): consider removing this as it leaks a Keras concept.
# pylint: disable=protected-access
keras_symbolic_tensors = [x for x in ret if ops._is_keras_symbolic_tensor(x)]
if keras_symbolic_tensors:
    raise core._SymbolicException(
        "Using symbolic output of a Keras layer during eager execution "
        "{}".format(keras_symbolic_tensors))
# pylint: enable=protected-access
exit((dtype.as_datatype_enum, ret))
