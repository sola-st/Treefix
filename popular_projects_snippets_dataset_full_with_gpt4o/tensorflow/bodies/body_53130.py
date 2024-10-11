# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Tests unconverted variable propagation through nested functions."""
with ops.Graph().as_default():
    with variable_scope.variable_scope("", use_resource=True):
        control_flow_v2_toggles.enable_control_flow_v2()
        x = variable_scope.get_variable("x", initializer=1.0)
        y = variable_scope.get_variable("y", initializer=2.0)
        z = variable_scope.get_variable("z", initializer=3.0)
        # pylint: disable=g-long-lambda
        _ = control_flow_ops.case(
            [(gen_math_ops.less(x, y), lambda: x)],
            default=lambda: control_flow_ops.case(
                [(gen_math_ops.less(z, y), lambda: z)], default=lambda: y))
        # pylint: enable=g-long-lambda
        control_flow_v2_toggles.disable_control_flow_v2()
    with session_lib.Session() as sess:
        sess.run(variables.global_variables_initializer())
        variable_graph_def = sess.graph.as_graph_def()
        constant_graph_def = (
            convert_to_constants
            .convert_variables_to_constants_from_session_graph(
                sess,
                variable_graph_def, ["case/cond"],
                variable_names_denylist=["y"]))
        self._assertGraphContains(
            constant_graph_def, """
            node {name: "x" op: "Const"}
            node {name: "y" op: "VarHandleOp"}
            node {name: "z" op: "Const"}

            node {name: "Less/ReadVariableOp" op: "Identity" input: "x"}
            node {name: "Less/ReadVariableOp_1" op: "ReadVariableOp" input: "y"}

            node {
              name: "case/cond" op: "If"
              input: "x" input: "z" input: "y"
              attr {
                key: "Tin"
                value {list
                  {type: DT_FLOAT type: DT_FLOAT type: DT_RESOURCE}}}
              attr {
                key: "_read_only_resource_inputs"
                value {list {i: 1 i: 2 i: 3}}}
              attr {key: "then_branch"
                    value {func {name: "case_cond_true_frozen_0"}}}
              attr {key: "else_branch"
                    value {func {name: "case_cond_false_frozen_0"}}}
              attr {key: "output_shapes" value {list {shape {}}}}
            }
            library {
              function {
                signature {
                  name: "case_cond_true_frozen_0"
                  input_arg {name: "placeholder" type: DT_FLOAT}
                  input_arg {name: "placeholder_1" type: DT_RESOURCE}
                  input_arg {name: "readvariableop_x" type: DT_FLOAT}
                  output_arg {name: "readvariableop" type: DT_FLOAT}
                  is_stateful: true
                }

                node_def {name: "ReadVariableOp" op: "Identity"
                  input: "readvariableop_x"}}

              function {
                signature {
                  name: "case_cond_false_frozen_0"
                  input_arg {name: "placeholder" type: DT_FLOAT}
                  input_arg {name: "less_readvariableop_1_y" type: DT_RESOURCE}
                  input_arg {name: "less_readvariableop_z" type: DT_FLOAT}
                  output_arg {name: "case_cond_identity" type: DT_FLOAT}
                  is_stateful: true
                }

                node_def {name: "Less/ReadVariableOp_1" op: "ReadVariableOp"
                  input: "less_readvariableop_1_y"}

                node_def {name: "Less/ReadVariableOp" op: "Identity"
                  input: "less_readvariableop_z"}

                node_def {name: "case/cond" op: "If"
                  input: "less_readvariableop_z"
                  input: "less_readvariableop_1_y"
                  attr {
                    key: "Tin"
                    value {list {type: DT_FLOAT type: DT_RESOURCE}}}
                  attr {key: "then_branch"
                        value {func {name: "case_cond_true_frozen_1"}}}
                  attr {key: "else_branch"
                        value {func {name: "case_cond_false_frozen_1"}}}
                  attr {
                    key: "_read_only_resource_inputs"
                    value {list {i: 1 i: 2}}}}}

              function {
                signature {
                  name: "case_cond_false_frozen_1"
                  input_arg {name: "placeholder" type: DT_FLOAT}
                  input_arg {name: "readvariableop_y" type: DT_RESOURCE}
                  output_arg {name: "readvariableop" type: DT_FLOAT}
                  is_stateful: true
                }

                node_def {name: "ReadVariableOp" op: "ReadVariableOp"
                  input: "readvariableop_y"}}

              function {
                signature {
                  name: "case_cond_true_frozen_1"
                  input_arg {name: "placeholder" type: DT_RESOURCE}
                  input_arg {name: "readvariableop_z" type: DT_FLOAT}
                  output_arg {name: "readvariableop" type: DT_FLOAT}
                  is_stateful: true
                }

                node_def {name: "ReadVariableOp" op: "Identity"
                  input: "readvariableop_z"}}}""")
