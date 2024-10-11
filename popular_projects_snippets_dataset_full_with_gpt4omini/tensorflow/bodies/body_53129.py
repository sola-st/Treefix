# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Tests that a v2 case() with resource variables converts properly."""
with ops.Graph().as_default():
    with variable_scope.variable_scope("", use_resource=True):
        control_flow_v2_toggles.enable_control_flow_v2()
        x = variable_scope.get_variable("x", initializer=1.0)
        y = variable_scope.get_variable("y", initializer=2.0)
        _ = control_flow_ops.case([(gen_math_ops.less(x, y), lambda: x)],
                                  default=lambda: y)
        control_flow_v2_toggles.disable_control_flow_v2()
    with session_lib.Session() as sess:
        sess.run(variables.global_variables_initializer())
        variable_graph_def = sess.graph.as_graph_def()
        constant_graph_def = (
            convert_to_constants
            .convert_variables_to_constants_from_session_graph(
                sess, variable_graph_def, ["case/cond"]))
        self._assertGraphContains(
            constant_graph_def, """
            node {name: "x" op: "Const"}
            node {name: "y" op: "Const"}
            node {
              name: "case/cond" op: "If" input: "Less" input: "x" input: "y"
              attr {key: "Tcond" value {type: DT_BOOL}}
              attr {key: "Tin" value {list {type: DT_FLOAT type: DT_FLOAT}}}
              attr {key: "Tout" value {list {type: DT_FLOAT}}}
            }
            library {
              function {
                signature {
                  name: "case_cond_false_frozen_0"
                  input_arg {name: "placeholder" type: DT_FLOAT}
                  input_arg {name: "readvariableop_y" type: DT_FLOAT}
                  output_arg {name: "readvariableop" type: DT_FLOAT}
                }
              }
              function {
                signature {
                  name: "case_cond_true_frozen_0"
                  input_arg {name: "placeholder" type: DT_FLOAT}
                  input_arg {name: "readvariableop_x" type: DT_FLOAT}
                  output_arg {name: "readvariableop" type: DT_FLOAT}
                }
              }
            }""")
