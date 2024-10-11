# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
# train.Saver is V1 only API.
with ops_lib.Graph().as_default(), self.session() as sess:
    # Calls .eval() to return the ndarray that makes up the full variable.
    rnd = random_ops.random_uniform(var_full_shape).eval()

    if partitioner:
        vs = [
            variable_scope.get_variable(
                var_name,
                shape=var_full_shape,
                initializer=rnd,
                partitioner=partitioner,
                use_resource=use_resource)
        ]
    else:
        if use_resource:
            vs = [resource_variable_ops.ResourceVariable(rnd, name=var_name)]
        else:
            vs = [variables.VariableV1(rnd, name=var_name)]

    self.evaluate(variables.global_variables_initializer())
    if call_saver_with_dict:
        saver = saver_module.Saver({var_name: vs[0]})
    else:
        saver = saver_module.Saver(vs)
    actual_path = saver.save(sess, saved_path)
    self.assertEqual(saved_path, actual_path)

    exit(rnd)
