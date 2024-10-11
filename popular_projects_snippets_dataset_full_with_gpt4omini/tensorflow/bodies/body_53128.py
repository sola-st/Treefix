# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Tests that a v2 case() converts properly."""
with ops.Graph().as_default():
    with variable_scope.variable_scope("", use_resource=False):
        control_flow_v2_toggles.enable_control_flow_v2()
        a = variable_scope.get_variable("a", initializer=2.0)
        x = variable_scope.get_variable("x", initializer=1.0)
        y = variable_scope.get_variable("y", initializer=2.0)
        _ = control_flow_ops.case([(gen_math_ops.less(x, y), lambda: a)],
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
            node {
              name: "case/cond" op: "StatelessIf"
              input: "Less" input: "a/read" input: "y/read"
              attr {key: "Tcond" value {type: DT_BOOL}}
              attr {key: "Tin" value {list {type: DT_FLOAT type: DT_FLOAT}}}
              attr {key: "Tout" value {list {type: DT_FLOAT}}}
            }
            library {
              function {
                signature {
                  name: "case_cond_false_frozen_0"
                  input_arg {name: "placeholder" type: DT_FLOAT}
                  input_arg {name: "y_read_0" type: DT_FLOAT}
                  output_arg {name: "y_read" type: DT_FLOAT}
                }
              }
              function {
                signature {
                  name: "case_cond_true_frozen_0"
                  input_arg {name: "a_read_0" type: DT_FLOAT}
                  input_arg {name: "placeholder" type: DT_FLOAT}
                  output_arg {name: "a_read" type: DT_FLOAT}
                }
              }
            }""")
