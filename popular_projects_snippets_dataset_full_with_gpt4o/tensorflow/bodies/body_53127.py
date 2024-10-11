# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Tests that a v1 case() construction converts properly."""
with ops.Graph().as_default():
    with variable_scope.variable_scope("", use_resource=False):
        control_flow_v2_toggles.disable_control_flow_v2()
        x = variable_scope.get_variable("x", initializer=1.0)
        y = variable_scope.get_variable("y", initializer=2.0)
        _ = control_flow_ops.case([(gen_math_ops.less(x, y), lambda: x)],
                                  default=lambda: y)
    with session_lib.Session() as sess:
        sess.run(variables.global_variables_initializer())
        variable_graph_def = sess.graph.as_graph_def()
        constant_graph_def = (
            convert_to_constants
            .convert_variables_to_constants_from_session_graph(
                sess, variable_graph_def, ["case/cond/Merge"]))
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
              name: "y" op: "Const"
              attr { key: "dtype" value { type: DT_FLOAT } }
              attr {
                key: "value"
                value { tensor { dtype: DT_FLOAT tensor_shape{} float_val: 2 }}}
            }
            node {name: "x/read" op: "Identity" input: "x"}
            node {name: "y/read" op: "Identity" input: "y"}
            node {name: "Less" op: "Less" input: "x/read" input: "y/read"}
            node {name: "case/cond/pred_id" op: "Identity" input: "Less"}
            node {
              name: "case/cond/Switch_1" op: "Switch"
              input: "case/cond/pred_id" input: "x/read"
            }
            node {
              name: "case/cond/Switch_2" op: "Switch"
              input: "case/cond/pred_id" input: "y/read"
            }
            node {
              name: "case/cond/Merge" op: "Merge"
              input: "case/cond/Switch_2" input: "case/cond/Switch_1:1"
              attr {key: "T" value {type: DT_FLOAT}}
            }""")
