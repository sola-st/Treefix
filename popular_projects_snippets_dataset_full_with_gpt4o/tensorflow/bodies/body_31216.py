# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
# REMARKS: factory(scope) is a function accepting a scope
#          as an argument, such scope can be None, a string
#          or a VariableScope instance.
with self.session(graph=ops.Graph()):
    if use_outer_scope:
        with variable_scope.variable_scope(prefix) as scope:
            factory(scope)
    else:
        factory(prefix)

    # check that all the variables names starts
    # with the proper scope.
    variables_lib.global_variables_initializer()
    all_vars = variables_lib.global_variables()
    prefix = prefix or "bidirectional_rnn"
    scope_vars = [v for v in all_vars if v.name.startswith(prefix + "/")]
    tf_logging.info("BiRNN with scope: %s (%s)" %
                    (prefix, "scope" if use_outer_scope else "str"))
    for v in scope_vars:
        tf_logging.info(v.name)
    self.assertEqual(len(scope_vars), len(all_vars))
