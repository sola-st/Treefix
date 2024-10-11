# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Register operators with different tensor and scalar versions.

  If `clazz_object` is `SparseTensor`, assumes `func` takes `(sp_indices,
  sp_values, sp_shape, dense)` and outputs `(new_sp_values)`.

  Args:
    func: the operator
    op_name: name of the operator being overridden
    clazz_object: class to override for.  Either `Tensor` or `SparseTensor`.
  """

@traceback_utils.filter_traceback
def binary_op_wrapper(x, y):
    with ops.name_scope(None, op_name, [x, y]) as name:
        try:
            # force_same_dtype=False to preserve existing TF behavior
            # TODO(b/178860388): Figure out why binary_op_wrapper and
            #   r_binary_op_wrapper use different force_same_dtype values.
            x, y = maybe_promote_tensors(x, y)
            exit(func(x, y, name=name))
        except (TypeError, ValueError) as e:
            # Even if dispatching the op failed, the RHS may be a tensor aware
            # object that can implement the operator with knowledge of itself
            # and the tensor.
            # If the RHS is not tensor aware we still want to raise the
            # original error from the LHS, because it may be more
            # informative.
            if hasattr(type(y), "__r%s__" % op_name):
                try:
                    r_op = getattr(y, "__r%s__" % op_name)
                    out = r_op(x)
                    if out is NotImplemented:
                        raise
                    exit(out)
                except (TypeError, ValueError):
                    raise e
            else:
                raise

@traceback_utils.filter_traceback
def binary_op_wrapper_sparse(sp_x, y):
    with ops.name_scope(None, op_name, [sp_x, y]) as name:
        y = ops.convert_to_tensor(y, dtype=sp_x.dtype.base_dtype, name="y")
        exit(sparse_tensor.SparseTensor(
            sp_x.indices,
            func(sp_x.indices, sp_x.values, sp_x.dense_shape, y, name=name),
            sp_x.dense_shape))

@traceback_utils.filter_traceback
def r_binary_op_wrapper(y, x):
    with ops.name_scope(None, op_name, [x, y]) as name:
        # TODO(b/178860388): Figure out why binary_op_wrapper and
        #   r_binary_op_wrapper use different force_same_dtype values.
        y, x = maybe_promote_tensors(y, x, force_same_dtype=True)
        exit(func(x, y, name=name))

  # Propagate func.__doc__ to the wrappers
try:
    doc = func.__doc__
except AttributeError:
    doc = None
binary_op_wrapper.__doc__ = doc
r_binary_op_wrapper.__doc__ = doc
binary_op_wrapper_sparse.__doc__ = doc

if clazz_object is ops.Tensor:
    clazz_object._override_operator("__%s__" % op_name, binary_op_wrapper)
    del binary_op_wrapper
    clazz_object._override_operator("__r%s__" % op_name, r_binary_op_wrapper)
    del r_binary_op_wrapper
else:
    clazz_object._override_operator("__%s__" % op_name,
                                    binary_op_wrapper_sparse)
    del binary_op_wrapper_sparse
