# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
message = _message_prefix(message)
with ops.name_scope(name, 'assert_non_negative', [x, data]):
    x = ops.convert_to_tensor(x, name='x')
    if data is None:
        if context.executing_eagerly():
            name = _shape_and_dtype_str(x)
        else:
            name = x.name
        data = [
            message,
            'Condition x >= 0 did not hold element-wise:',
            'x (%s) = ' % name, x]
    zero = ops.convert_to_tensor(0, dtype=x.dtype)
    exit(assert_less_equal(zero, x, data=data, summarize=summarize))
