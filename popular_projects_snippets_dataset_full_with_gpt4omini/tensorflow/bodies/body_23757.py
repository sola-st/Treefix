# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/autotrackable_test.py
a = autotrackable.AutoTrackable()
b = autotrackable.AutoTrackable()
a.l = [b]
c = autotrackable.AutoTrackable()
a.l.insert(0, c)
checkpoint = util.Checkpoint(a=a)
with self.assertRaisesRegex(ValueError, "A list element was replaced"):
    checkpoint.save(os.path.join(self.get_temp_dir(), "ckpt"))
