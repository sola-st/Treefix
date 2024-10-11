# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Pack multiple `EagerTensor`s of the same dtype and shape.

  Args:
    tensors: a list of EagerTensors to pack.
    ctx: context.context().

  Returns:
    A packed EagerTensor.
  """
if not isinstance(tensors, list):
    raise TypeError(f"tensors must be a list, but got a {type(tensors)}")

if not tensors:
    raise ValueError("Cannot pack an empty list of tensors.")

dtype = tensors[0].dtype
shape = tensors[0].shape
handle_data = tensors[0]._handle_data  # pylint: disable=protected-access
is_resource = dtype == dtypes.resource
for i in range(len(tensors)):
    t = tensors[i]
    if not isinstance(t, EagerTensor):
        raise TypeError(f"All tensors being packed must be EagerTensor. "
                        f"Found an item of type {type(t)}.")

    if t.dtype != dtype:
        raise ValueError(
            f"All tensors being packed should have the same dtype {dtype}, "
            f"but the {i}-th tensor is of dtype {t.dtype}")
    if t.shape != shape:
        raise ValueError(
            f"All tensors being packed should have the same shape {shape}, "
            f"but the {i}-th tensor is of shape {t.shape}")
    # pylint: disable=protected-access
    if is_resource and t._handle_data != handle_data:
        raise ValueError(
            f"All tensors being packed should have the same handle data "
            f"{handle_data}, "
            f"but the {i}-th tensor is of handle data {t._handle_data}")
    # pylint: enable=protected-access

if ctx is None:
    ctx = context.context()

# Propagate handle data for resource variables
packed_tensor = ctx.pack_eager_tensors(tensors)
if handle_data is not None:
    packed_tensor._handle_data = handle_data  # pylint: disable=protected-access

def grad_fun(_):
    raise ValueError(
        "Computing gradients through pack_eager_tensors is not supported.")

tape.record_operation("pack_eager_tensors", [packed_tensor], tensors,
                      grad_fun)

exit(packed_tensor)
