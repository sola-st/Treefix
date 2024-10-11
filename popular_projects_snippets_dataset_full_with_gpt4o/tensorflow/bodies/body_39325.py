# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_view_test.py
root1 = autotrackable.AutoTrackable()
leaf1 = root1.leaf1 = autotrackable.AutoTrackable()
leaf2 = root1.leaf2 = autotrackable.AutoTrackable()
leaf1.leaf3 = autotrackable.AutoTrackable()
leaf1.leaf4 = autotrackable.AutoTrackable()
leaf2.leaf5 = autotrackable.AutoTrackable()
root_ckpt = trackable_utils.Checkpoint(root=root1)
root_save_path = root_ckpt.save(
    os.path.join(self.get_temp_dir(), "root_ckpt"))

root2 = autotrackable.AutoTrackable()
leaf11 = root2.leaf1 = autotrackable.AutoTrackable()
leaf12 = root2.leaf2 = autotrackable.AutoTrackable()
leaf13 = leaf11.leaf3 = autotrackable.AutoTrackable()
leaf15 = leaf12.leaf5 = autotrackable.AutoTrackable()
leaf16 = leaf12.leaf6 = autotrackable.AutoTrackable()
diff = checkpoint_view.CheckpointView(root_save_path).diff(root2)
self.assertEqual(len(diff), 3)
self.assertDictEqual(diff[0], {
    0: root2,
    1: leaf11,
    2: leaf12,
    4: leaf13,
    6: leaf15
})
self.assertListEqual(diff[1], [3, 5])
self.assertListEqual(diff[2], [leaf16])
