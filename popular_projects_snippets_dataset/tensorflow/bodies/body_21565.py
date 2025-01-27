# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
# Builds a graph.
v0 = variables.VariableV1(
    [[1, 2, 3], [4, 5, 6]], dtype=dtypes.float32, name="v0")
v1 = variables.VariableV1(
    [[[1], [2]], [[3], [4]], [[5], [6]]], dtype=dtypes.float32, name="v1")
init_all_op = variables.global_variables_initializer()
save = saver_module.Saver(
    {
        "v0": v0,
        "v1": v1
    }, write_version=self._WRITE_VERSION)
save_path = os.path.join(self.get_temp_dir(),
                         "ckpt_for_debug_string" + str(self._WRITE_VERSION))
with self.cached_session() as sess:
    self.evaluate(init_all_op)
    # Saves a checkpoint.
    save.save(sess, save_path)

    # Creates a reader.
    reader = py_checkpoint_reader.NewCheckpointReader(save_path)
    # Verifies that the tensors exist.
    self.assertTrue(reader.has_tensor("v0"))
    self.assertTrue(reader.has_tensor("v1"))
    debug_string = reader.debug_string()
    # Verifies that debug string contains the right strings.
    self.assertTrue(compat.as_bytes("v0 (DT_FLOAT) [2,3]") in debug_string)
    self.assertTrue(compat.as_bytes("v1 (DT_FLOAT) [3,2,1]") in debug_string)
    # Verifies get_variable_to_shape_map() returns the correct information.
    var_map = reader.get_variable_to_shape_map()
    self.assertEqual([2, 3], var_map["v0"])
    self.assertEqual([3, 2, 1], var_map["v1"])
    # Verifies get_tensor() returns the tensor value.
    v0_tensor = reader.get_tensor("v0")
    v1_tensor = reader.get_tensor("v1")
    self.assertAllEqual(v0, v0_tensor)
    self.assertAllEqual(v1, v1_tensor)
    # Verifies get_tensor() fails for non-existent tensors.
    with self.assertRaisesRegex(errors.NotFoundError,
                                "v3 not found in checkpoint"):
        reader.get_tensor("v3")
