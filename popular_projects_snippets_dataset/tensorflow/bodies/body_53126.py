# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Tests that a chain of Identity ops is converted properly."""
with ops.Graph().as_default():
    with variable_scope.variable_scope("", use_resource=True):
        x = variable_scope.get_variable("x", initializer=1.0)
        y = array_ops.identity(x, name="y")
        _ = array_ops.identity(y, name="z")
    with session_lib.Session() as sess:
        sess.run(variables.global_variables_initializer())
        variable_graph_def = sess.graph.as_graph_def()
        constant_graph_def = (
            convert_to_constants
            .convert_variables_to_constants_from_session_graph(
                sess, variable_graph_def, ["z"]))
        self._assertGraphContains(
            constant_graph_def, """
            node {
              name: "x" op: "Const"
              attr { key: "dtype" value { type: DT_FLOAT } }
              attr {
                key: "value"
                value { tensor { dtype: DT_FLOAT tensor_shape{} float_val: 1 }}}
            }
            node {
              name: "y/ReadVariableOp" op: "Identity" input: "x"
              attr { key: "T" value { type: DT_FLOAT } }
            }
            node {
              name: "y" op: "Identity" input: "y/ReadVariableOp"
              attr { key: "T" value { type: DT_FLOAT } }
            }
            node {
              name: "z" op: "Identity" input: "y"
              attr { key: "T" value { type: DT_FLOAT } }
            }""")
