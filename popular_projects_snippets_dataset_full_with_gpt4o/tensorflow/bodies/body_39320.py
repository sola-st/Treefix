# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_view_test.py
root = autotrackable.AutoTrackable()
root.leaf = autotrackable.AutoTrackable()
root_ckpt = trackable_utils.Checkpoint(root=root)
root_save_path = root_ckpt.save(
    os.path.join(self.get_temp_dir(), "root_ckpt"))
current_name, node_id = next(
    iter(
        checkpoint_view.CheckpointView(root_save_path).children(0).items()))
self.assertEqual("leaf", current_name)
self.assertEqual(1, node_id)
