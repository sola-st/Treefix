# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/partitioned_variables_test.py
with self.cached_session():
    rnd_par = constant_op.constant([[1, 2, 3, 4], [5, 6, 7, 8]])
    with variable_scope.variable_scope("hi", use_resource=use_resource):
        vs1 = partitioned_variables.create_partitioned_variables([2, 4], [1, 2],
                                                                 rnd_par)
        vs2 = partitioned_variables.create_partitioned_variables([2, 4], [1, 2],
                                                                 rnd_par)
    self.evaluate(variables.global_variables_initializer())
    var1_name = vs1[0]._save_slice_info.full_name
    var2_name = vs2[0]._save_slice_info.full_name
    self.assertEqual("hi/PartitionedVariable", var1_name)
    self.assertEqual("hi/PartitionedVariable_1", var2_name)
    self.assertEqual(var1_name + "/part_0:0", vs1[0].name)
    self.assertEqual(var1_name + "/part_1:0", vs1[1].name)
    self.assertEqual(var2_name + "/part_0:0", vs2[0].name)
    self.assertEqual(var2_name + "/part_1:0", vs2[1].name)
# Test same variable.
with self.cached_session():
    rnd_par = constant_op.constant([[1, 2, 3, 4], [5, 6, 7, 8]])
    with variable_scope.variable_scope(
        "hola", use_resource=use_resource) as vs:
        vs1 = partitioned_variables.create_partitioned_variables(
            [2, 4], [1, 2], rnd_par, dtype=dtypes.int32)
    with variable_scope.variable_scope(
        vs, reuse=True, use_resource=use_resource):
        vs2 = partitioned_variables.create_partitioned_variables(
            [2, 4], [1, 2], rnd_par, dtype=dtypes.int32)
    self.evaluate(variables.global_variables_initializer())
    var1_name = vs1[0]._save_slice_info.full_name
    var2_name = vs2[0]._save_slice_info.full_name
    self.assertEqual("hola/PartitionedVariable", var1_name)
    self.assertEqual("hola/PartitionedVariable", var2_name)
    self.assertEqual(var1_name + "/part_0:0", vs1[0].name)
    self.assertEqual(var1_name + "/part_1:0", vs1[1].name)
    self.assertEqual(var2_name + "/part_0:0", vs2[0].name)
    self.assertEqual(var2_name + "/part_1:0", vs2[1].name)
# Test name_scope
with self.cached_session():
    rnd_par = constant_op.constant([[1, 2, 3, 4], [5, 6, 7, 8]])
    with ops.name_scope("ola"):
        vs1 = partitioned_variables.create_partitioned_variables([2, 4], [1, 2],
                                                                 rnd_par)
        vs2 = partitioned_variables.create_partitioned_variables([2, 4], [1, 2],
                                                                 rnd_par)
    self.evaluate(variables.global_variables_initializer())
    var1_name = vs1[0]._save_slice_info.full_name
    var2_name = vs2[0]._save_slice_info.full_name
    # Currently, the name scope 'ola' has no effect.
    self.assertEqual("PartitionedVariable", var1_name)
    self.assertEqual("PartitionedVariable_1", var2_name)
    self.assertEqual(var1_name + "/part_0:0", vs1[0].name)
    self.assertEqual(var1_name + "/part_1:0", vs1[1].name)
    self.assertEqual(var2_name + "/part_0:0", vs2[0].name)
    self.assertEqual(var2_name + "/part_1:0", vs2[1].name)
