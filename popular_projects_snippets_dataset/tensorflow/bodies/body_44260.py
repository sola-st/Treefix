# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_scoping_test.py
# Deviating from the normal Python semantics here to avoid inserting
# an extra assert op. If needed, we can insert it and raise an error
# to mimic the eager behavior, but this is an exceptionally uncummon
# use case.
self.assertAllEqual(tf.function(for_defines_iterate)(0, tf.range), (0, 0))
