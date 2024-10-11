# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_test.py
# We want to ensure the timestamp is something plausible, and aren't able
# to mock out the actual clock used through many layers of the stack, so
# just assert that it's within the past hour, which should always be true.
self.assertLessEqual(t, time.time())
self.assertLess(abs(t - time.time()), 3600)
