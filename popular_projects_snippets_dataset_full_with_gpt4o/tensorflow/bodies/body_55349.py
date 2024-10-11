# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
g = ops.Graph()
with g.as_default():
    m = array_ops.placeholder(dtypes.float32)
    s, u, v = linalg_ops.svd(m)
    ss = math_ops.reduce_sum(s)
    uu = math_ops.reduce_sum(u)
    vv = math_ops.reduce_sum(v)
    result = ss + uu + vv
f = graph_to_function_def.graph_to_function_def(
    g,
    g.get_operations()[1:],  # skip the placeholder
    [s, u, v],
    [result])
self.assertEqual(len(f.signature.input_arg), 3)
