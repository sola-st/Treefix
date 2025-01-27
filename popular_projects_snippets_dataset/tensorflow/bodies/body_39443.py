# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore_test.py
root = autotrackable.AutoTrackable()
root.leaf = autotrackable.AutoTrackable()
root_ckpt = trackable_utils.Checkpoint(root=root)
root_save_path = root_ckpt.save(
    os.path.join(self.get_temp_dir(), "root_ckpt"))

root2 = autotrackable.AutoTrackable()
root2.leaf = autotrackable.AutoTrackable()

with self.assertRaisesRegex(
    ValueError,
    "Expecting a dictionary of node_id to Trackable for nodes_to_restore."):
    restore.restore_nodes(root_save_path, [0, 1])

with self.assertRaisesRegex(
    ValueError,
    "The expected node_id: 3 to Trackable <.*?> to restore does not exist "
    "in the checkpoint."):
    restore.restore_nodes(root_save_path, {3: root2})

with self.assertRaisesRegex(
    ValueError,
    "Expecting a valid Trackable to node_id: 0 but got trackable: None."):
    restore.restore_nodes(root_save_path, {0: None})
