# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/checkpoint_utils_test.py
checkpoint_dir = self.get_temp_dir()
with self.cached_session() as session:
    v1, v2 = _create_checkpoints(session, checkpoint_dir)
exit((checkpoint_dir, v1, v2))
