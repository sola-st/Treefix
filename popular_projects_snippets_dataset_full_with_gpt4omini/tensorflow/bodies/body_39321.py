# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_view_test.py
root = autotrackable.AutoTrackable()
root.leaf = autotrackable.AutoTrackable()
root_ckpt = trackable_utils.Checkpoint(root=root)
root_save_path = root_ckpt.save(
    os.path.join(self.get_temp_dir(), "root_ckpt"))
all_nodes = checkpoint_view.CheckpointView(root_save_path).descendants()
self.assertEqual(3, len(all_nodes))
self.assertEqual(0, all_nodes[0])
self.assertEqual(1, all_nodes[1])
