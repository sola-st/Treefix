# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_def_to_graph_test.py
with ops.Graph().as_default() as g:
    # Inputs:    x    y    z
    #            |\   |   /
    #            | \  |  /
    #            |  foo_1     list_output
    #            |   / \       /       \
    #            | d_1 e_1  a:1        a:0
    #            |  \   |   /           |
    #            |   \  |  /            |
    #            |    foo_2             |
    #            |     / \              |
    # Outputs:   x   d_2 e_2           a:0

    x = array_ops.placeholder(dtypes.float32, name="x")
    y = array_ops.placeholder(dtypes.int32, name="y")
    z = array_ops.placeholder(dtypes.int32, name="z")

    d_1, e_1 = op_def_library.apply_op("Foo1", name="foo_1", a=x, b=y, c=z)

    list_output0, list_output1 = test_ops.list_output(
        T=[dtypes.int32, dtypes.int32], name="list_output")

    d_2, e_2 = test_ops.foo1(a=d_1, b=e_1, c=list_output1, name="foo_2")

fdef = graph_to_function_def.graph_to_function_def(
    g,
    g.get_operations(),
    [x, y, z],  # Inputs
    [x, d_2, e_2, list_output0])  # Outputs.

# Assert that the FunctionDef was correctly built.
assert len(fdef.node_def) == 3  # 2 Foo1 nodes and 1 ListOutput node.
assert fdef.node_def[0].op == "Foo1"
assert fdef.node_def[0].input == ["x", "y", "z"]
assert fdef.node_def[1].op == "ListOutput"
assert not fdef.node_def[1].input
assert fdef.node_def[2].op == "Foo1"
assert fdef.node_def[2].input == [
    "foo_1:d:0", "foo_1:e:0", "list_output:a:1"
]
exit(fdef)
