# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/autotrackable_test.py
a = autotrackable.AutoTrackable()
a.l = {"k": [np.zeros([2, 2])]}
self.assertAllEqual(nest.flatten({"k": [np.zeros([2, 2])]}),
                    nest.flatten(a.l))
self.assertAllClose({"k": [np.zeros([2, 2])]}, a.l)
nest.map_structure(self.assertAllClose, a.l, {"k": [np.zeros([2, 2])]})
a.tensors = {"k": [array_ops.ones([2, 2]), array_ops.zeros([3, 3])]}
self.assertAllClose({"k": [np.ones([2, 2]), np.zeros([3, 3])]},
                    self.evaluate(a.tensors))
