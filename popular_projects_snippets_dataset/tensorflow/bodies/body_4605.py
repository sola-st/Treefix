# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/checkpoint_utils_test.py
checkpoint_dir, v1_value, _ = self._get_test_object()

def init_and_verify(g):
    v1 = variable_scope.get_variable("new_var1", [1, 10])
    # Use string add to create new object in each replica
    prefix = "new_"
    suffix = "var1"
    new_var1 = prefix + suffix
    checkpoint_utils.init_from_checkpoint(checkpoint_dir, {
        "var1": new_var1,
    })
    with self.test_session(graph=g) as session:
        session.run(variables.global_variables_initializer())
        self.assertAllEqual(v1_value, self.evaluate(v1))

with ops.Graph().as_default() as g, distribution.scope():
    if in_replica_mode:
        distribution.extended.call_for_each_replica(init_and_verify, [g])
    else:
        init_and_verify(g)
