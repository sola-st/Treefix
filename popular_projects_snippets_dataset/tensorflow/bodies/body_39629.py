# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
checkpoint_directory = self.get_temp_dir()
save_root = trackable_utils.Checkpoint(a=[])
path = save_root.save(checkpoint_directory)
load_root = trackable_utils.Checkpoint(b=[])
load_root.dep = []
load_root.dep.append([])
status = load_root.restore(path)
status.assert_consumed()
status.assert_existing_objects_matched()
status.assert_nontrivial_match()
