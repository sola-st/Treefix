# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_view_test.py
root = autotrackable.AutoTrackable()
leaf1 = root.leaf1 = autotrackable.AutoTrackable()
leaf2 = root.leaf2 = autotrackable.AutoTrackable()
leaf1.leaf3 = autotrackable.AutoTrackable()
leaf1.leaf4 = autotrackable.AutoTrackable()
leaf2.leaf5 = autotrackable.AutoTrackable()
root_ckpt = trackable_utils.Checkpoint(root=root)
root_save_path = root_ckpt.save(
    os.path.join(self.get_temp_dir(), "root_ckpt"))
all_nodes_with_paths = checkpoint_view.CheckpointView(
    root_save_path)._descendants_with_paths()
self.assertEqual(
    {
        "root", "root.leaf1", "root.leaf2", "root.save_counter",
        "root.leaf1.leaf3", "root.leaf1.leaf4", "root.leaf2.leaf5"
    }, set(all_nodes_with_paths.values()))
