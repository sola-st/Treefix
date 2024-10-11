# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
if not psutil_import_succeeded:
    self.skipTest(
        "psutil is required to check that we've closed our files.")
root = autotrackable.AutoTrackable()
root.v = variables_lib.Variable(1)
ckpt = trackable_utils.Checkpoint(root=root)
save_path = ckpt.save(os.path.join(self.get_temp_dir(), "ckpt"))

root2 = autotrackable.AutoTrackable()
ckpt2 = trackable_utils.Checkpoint(root=root2)
ckpt2.restore(save_path)

proc = psutil.Process()
for file in proc.open_files():
    self.assertNotIn(save_path, file[0])
