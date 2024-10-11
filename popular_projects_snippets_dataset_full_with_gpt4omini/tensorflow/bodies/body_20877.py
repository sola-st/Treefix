# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils_test.py
checkpoint_dir = self.get_temp_dir()
with self.cached_session() as session:
    v1, v2, v3, v4 = _create_checkpoints(session, checkpoint_dir)
self.assertAllEqual(
    checkpoint_utils.load_variable(checkpoint_dir, "var1"), v1)
self.assertAllEqual(
    checkpoint_utils.load_variable(checkpoint_dir, "var2"), v2)
self.assertAllEqual(
    checkpoint_utils.load_variable(checkpoint_dir, "var3"), v3)
self.assertAllEqual(
    checkpoint_utils.load_variable(checkpoint_dir, "useful_scope/var4"), v4)
