# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils_test.py
checkpoint_dir = self.get_temp_dir()
with self.cached_session() as session:
    _, _, _, v4 = _create_checkpoints(session, checkpoint_dir)

with ops.Graph().as_default() as g:
    with variable_scope.variable_scope("useful_scope"):
        my4 = variable_scope.get_variable("var4", [9, 9])
    with variable_scope.variable_scope("useful_scope_1"):
        my5_init = [[1.0, 2.0], [3.0, 4.0]]
        my5 = variable_scope.get_variable("var5", initializer=my5_init)

    checkpoint_utils.init_from_checkpoint(checkpoint_dir,
                                          {"useful_scope/": "useful_scope/"})
    with self.session(graph=g) as session:
        session.run(variables.global_variables_initializer())
        self.assertAllEqual(my4.eval(session), v4)
        self.assertAllEqual(my5.eval(session), my5_init)
