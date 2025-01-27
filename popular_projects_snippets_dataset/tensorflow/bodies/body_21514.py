# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
var_full_shape = [10, 3]
# Allows save/restore mechanism to work w/ different slicings.
var_name = "my_var"
saved_dir = self._get_test_dir("partitioned_variables")
saved_path = os.path.join(saved_dir, "ckpt")

call_saver_with_dict = False  # updated by test loop below

def _save(partitioner=None):
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

def _restore(partitioner=None):
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

for call_saver_with_dict in {False, True}:
    # Save PartitionedVariable and restore into full variable.
    saved_full = _save(
        partitioner=partitioned_variables.fixed_size_partitioner(
            num_shards=2))
    restored_full = _restore()
    self.assertAllEqual(saved_full, restored_full)

    # Restores into the same number of partitions.
    restored_full = _restore(
        partitioner=partitioned_variables.fixed_size_partitioner(
            num_shards=2))
    self.assertAllEqual(saved_full, restored_full)

    # Restores into a different number of partitions.
    restored_full = _restore(
        partitioner=partitioned_variables.fixed_size_partitioner(
            num_shards=3))
    self.assertAllEqual(saved_full, restored_full)

    # Now, saves a full variable and restores PartitionedVariable.
    saved_full = _save()
    restored_full = _restore(
        partitioner=partitioned_variables.fixed_size_partitioner(
            num_shards=3))
    self.assertAllEqual(saved_full, restored_full)
