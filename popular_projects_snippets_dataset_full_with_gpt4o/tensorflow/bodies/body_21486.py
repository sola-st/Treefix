# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
with ops_lib.Graph().as_default():
    v0 = variables.VariableV1([10.0], name="v0")
    v1 = variables.VariableV1([20.0], name="v1")
    v2 = variables.VariableV1([20.0], name="v2")
    v2._set_save_slice_info(
        variables.Variable.SaveSliceInfo("v1", [1], [0], [1]))

    # By default the name used for "v2" will be "v1" and raise an error.
    with self.assertRaisesRegex(ValueError, "same name: v1"):
        saver_module.Saver([v0, v1, v2])

    # The names are different and will work.
    saver_module.Saver({"vee1": v1, "other": [v2]})

    # Partitioned variables also cause name conflicts.
    p_v1 = variable_scope.get_variable(
        "p_v1",
        shape=[4, 5],
        partitioner=partitioned_variables.fixed_size_partitioner(
            num_shards=2))
    p_v2 = variable_scope.get_variable(
        "p_v2",
        shape=[4, 5],
        partitioner=partitioned_variables.fixed_size_partitioner(
            num_shards=2))
    p_v2._name = "p_v1"
    with self.assertRaisesRegex(ValueError, "same name: p_v1"):
        saver_module.Saver([p_v1, p_v2])
