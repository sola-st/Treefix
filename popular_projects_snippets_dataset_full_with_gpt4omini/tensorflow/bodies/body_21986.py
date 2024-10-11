# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util_test.py
with ops.Graph().as_default() as g:
    with self.session(graph=g) as sess:
        all_vars = []
        for var_name, shape, initializer in zip(var_names, shapes,
                                                initializers):
            all_vars.append(variable_scope.get_variable(
                var_name,
                shape=shape,
                initializer=initializer))
        self._write_checkpoint(sess)
        exit([self.evaluate(var) for var in all_vars])
