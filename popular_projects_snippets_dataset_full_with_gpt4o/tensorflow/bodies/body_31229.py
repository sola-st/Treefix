# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
num_units = 3
batch_size = 2
state_saver = TestStateSaver(batch_size, 2 * num_units)

with self.session(graph=ops.Graph()):
    if use_outer_scope:
        with variable_scope.variable_scope(prefix) as scope:
            self._factory(scope=scope, state_saver=state_saver)
    else:
        self._factory(scope=prefix, state_saver=state_saver)
        variables_lib.global_variables_initializer()

    # check that all the variables names starts
    # with the proper scope.
    all_vars = variables_lib.global_variables()
    prefix = prefix or "rnn"
    scope_vars = [v for v in all_vars if v.name.startswith(prefix + "/")]
    tf_logging.info("RNN with scope: %s (%s)" %
                    (prefix, "scope" if use_outer_scope else "str"))
    for v in scope_vars:
        tf_logging.info(v.name)
    self.assertEqual(len(scope_vars), len(all_vars))
