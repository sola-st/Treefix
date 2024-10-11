# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
# train.Saver is V1 only API.
with ops_lib.Graph().as_default(), self.session() as sess:
    if partitioner:
        new_vs = [
            variable_scope.get_variable(
                var_name,
                shape=var_full_shape,
                initializer=array_ops.zeros(var_full_shape),
                partitioner=partitioner)
        ]
    else:
        new_vs = [
            variables.VariableV1(
                array_ops.zeros(
                    shape=var_full_shape),  # != original contents.
                name=var_name)
        ]

    self.evaluate(variables.global_variables_initializer())
    if call_saver_with_dict:
        saver = saver_module.Saver({
            var_name: new_vs[0]
        })
    else:
        saver = saver_module.Saver(new_vs)
    saver.restore(sess, saved_path)

    if partitioner:
        exit(new_vs[0].as_tensor().eval())
    else:
        exit(new_vs[0].eval())
