# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
root = autotrackable.AutoTrackable()
leaf = autotrackable.AutoTrackable()
root.leaf = leaf
trackable_utils.add_variable(leaf, name="v", shape=[])
checkpoint_key = _get_all_checkpoint_names(root)[0]
self.assertEqual(r"leaf/v/.ATTRIBUTES/VARIABLE_VALUE", checkpoint_key)
