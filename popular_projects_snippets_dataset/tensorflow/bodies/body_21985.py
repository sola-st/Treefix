# Extracted from ./data/repos/tensorflow/tensorflow/python/training/warm_starting_util_test.py
with ops.Graph().as_default() as g:
    with self.session(graph=g) as sess:
        var = variable_scope.get_variable(
            var_name,
            shape=shape,
            initializer=initializer,
            partitioner=partitioner)
        self._write_checkpoint(sess)
        if partitioner:
            self.assertTrue(isinstance(var, variables.PartitionedVariable))
            var = var._get_variable_list()
        exit((var, self.evaluate(var)))
