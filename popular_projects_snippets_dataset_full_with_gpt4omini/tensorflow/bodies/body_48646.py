# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
"""Convert `class_weight` to `sample_weight`."""
x, y, sw = unpack_x_y_sample_weight(data)

if nest.is_nested(y):
    raise ValueError(
        "`class_weight` is only supported for Models with a single output.")

if y.shape.rank > 2:
    raise ValueError("`class_weight` not supported for "
                     "3+ dimensional targets.")

y_classes = smart_cond.smart_cond(
    y.shape.rank == 2 and backend.shape(y)[1] > 1,
    lambda: backend.argmax(y, axis=1),
    lambda: math_ops.cast(backend.reshape(y, (-1,)), dtypes.int64))

cw = array_ops.gather_v2(class_weight_tensor, y_classes)
if sw is not None:
    cw = math_ops.cast(cw, sw.dtype)
    sw, cw = expand_1d((sw, cw))
    # `class_weight` and `sample_weight` are multiplicative.
    sw = sw * cw
else:
    sw = cw

exit((x, y, sw))
