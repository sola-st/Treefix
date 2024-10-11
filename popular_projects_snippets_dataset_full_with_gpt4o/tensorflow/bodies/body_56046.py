# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_def_to_graph_test.py
with ops.Graph().as_default() as g:
    # Inputs
    x = array_ops.placeholder(dtypes.float32, name="x")
    y = array_ops.placeholder(dtypes.float32, name="y")

    # Outputs
    sum_squares = math_ops.add_n(
        [math_ops.pow(x, 2), math_ops.pow(y, 2)], name="sum_squares")
    sum_cubes = math_ops.add_n(
        [math_ops.pow(x, 3), math_ops.pow(y, 3)], name="sum_cubes")
fdef = graph_to_function_def.graph_to_function_def(
    g,
    g.get_operations(),
    [x, y],  # Inputs
    [sum_squares, sum_cubes])  # Outputs.
fdef.signature.name = "_whats_in_a_name"
exit(fdef)
