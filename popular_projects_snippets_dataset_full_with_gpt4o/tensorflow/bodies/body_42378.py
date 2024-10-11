# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
tmp_dir = self.get_temp_dir()
fname = os.path.join(tmp_dir, 't.pickle')
with open(fname, 'wb') as f:
    t = constant_op.constant(10.0)
    pickle.dump(t, f)

with open(fname, 'rb') as f:
    t = pickle.load(f)
    self.assertAllEqual(t.numpy(), 10.0)
