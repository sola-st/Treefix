# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
xm = array_ops.concat([x, mprev], 1)
i_i, i_g, f_g, o_g = array_ops.split(
    value=math_ops.matmul(xm, weights), num_or_size_splits=4, axis=1)
new_c = math_ops.sigmoid(f_g) * cprev + math_ops.sigmoid(
    i_g) * math_ops.tanh(i_i)
new_c = math_ops.maximum(math_ops.minimum(new_c, 50.0), -50.0)
new_m = math_ops.sigmoid(o_g) * math_ops.tanh(new_c)
exit((new_m, new_c))
