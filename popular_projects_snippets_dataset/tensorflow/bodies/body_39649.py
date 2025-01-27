# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
# Tests that there are no reference cycles when running garbage collection.
# Python uses reference counts as the primary garbage collector, which will
# not delete and finalize (__del__) objects in a cycle. The deletion is
# eventually triggered by gc, which only runs when the garbage has reached
# a certain threshold.

delete_counter = 0

class TrackableWithDel(autotrackable.AutoTrackable):

    def __del__(self):
        nonlocal delete_counter
        delete_counter += 1

x = autotrackable.AutoTrackable()
x.v = variables_lib.Variable(100.)
x.has_del = TrackableWithDel()

checkpoint = trackable_utils.Checkpoint(x)
checkpoint_prefix = os.path.join(self.get_temp_dir(), "ckpt")
save_path = checkpoint.save(checkpoint_prefix)

self.assertEqual(delete_counter, 0)
del checkpoint
del x
self.assertEqual(delete_counter, 1)

no_v = autotrackable.AutoTrackable()
no_v.has_del = TrackableWithDel()
checkpoint = trackable_utils.Checkpoint(no_v)
checkpoint.restore(save_path).expect_partial()
del checkpoint
del no_v
self.assertEqual(delete_counter, 2)
