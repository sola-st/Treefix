# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
t = constant_op.constant(2.)
update_calls = []
dist.extended.update_non_slot(t, lambda: update_calls.append(1))
self.assertEqual(len(update_calls), 1)
