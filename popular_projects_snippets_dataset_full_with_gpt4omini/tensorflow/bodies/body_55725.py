# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/graph_building_test.py
with func_graph.FuncGraph("add").as_default():
    a = gen_array_ops.placeholder(dtypes.float32)
    b = gen_array_ops.placeholder(dtypes.float32)
    for _ in range(num_ops):
        gen_math_ops.add(a, b)
