# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Tests that a single variable is properly converted to a constant."""

with ops.Graph().as_default():
    with variable_scope.variable_scope("", use_resource=False):
        _ = variable_scope.get_variable("x", initializer=1.0)
    with session_lib.Session() as sess:
        sess.run(variables.global_variables_initializer())
        variable_graph_def = sess.graph.as_graph_def()
        constant_graph_def = (
            convert_to_constants
            .convert_variables_to_constants_from_session_graph(
                sess, variable_graph_def, ["x/read"]))
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
              name: "x/read" op: "Identity" input: "x"
              attr { key: "T" value { type: DT_FLOAT } }
            }""")
