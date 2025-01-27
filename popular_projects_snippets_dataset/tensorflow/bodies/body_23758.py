# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/autotrackable_test.py
a = autotrackable.AutoTrackable()
b = autotrackable.AutoTrackable()
held_reference = [b]
a.l = held_reference
c = autotrackable.AutoTrackable()
held_reference.append(c)
checkpoint = util.Checkpoint(a=a)
with self.assertRaisesRegex(ValueError, "The wrapped list was modified"):
    checkpoint.save(os.path.join(self.get_temp_dir(), "ckpt"))
