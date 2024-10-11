# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_view_test.py
root1 = autotrackable.AutoTrackable()
root1.a = root1.b = autotrackable.AutoTrackable()
root_ckpt = trackable_utils.Checkpoint(root=root1)
root_save_path = root_ckpt.save(
    os.path.join(self.get_temp_dir(), "root_ckpt"))

root2 = autotrackable.AutoTrackable()
a1 = root2.a = autotrackable.AutoTrackable()
root2.b = autotrackable.AutoTrackable()
with self.assertLogs(level="WARNING") as logs:
    matching_nodes = checkpoint_view.CheckpointView(root_save_path).match(
        root2)
self.assertDictEqual(
    matching_nodes,
    {
        0: root2,
        1: a1,
        # Only the first element at the same position will be matched.
    })
expected_message = (
    "Inconsistent references when matching the checkpoint into this object"
    " graph.")
self.assertIn(expected_message, logs.output[0])
