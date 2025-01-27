# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils_test.py
checkpoint_dir = pathlib.Path(self.get_temp_dir())
with self.cached_session() as session:
    v1, v2, v3, v4 = _create_checkpoints(session, checkpoint_dir)  # pylint: disable=unused-variable

reader = checkpoint_utils.load_checkpoint(checkpoint_dir)
self.assertAllEqual(reader.get_tensor("var1"), v1)

self.assertAllEqual(
    checkpoint_utils.load_variable(checkpoint_dir, "var1"), v1)

self.assertEqual(
    checkpoint_utils.list_variables(checkpoint_dir),
    [("useful_scope/var4", [9, 9]), ("var1", [1, 10]), ("var2", [10, 10]),
     ("var3", [100, 100])])
