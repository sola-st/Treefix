# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profiler_v2_test.py
logdir = self.get_temp_dir()
profiler.start(logdir)
with self.assertRaises(errors.AlreadyExistsError):
    profiler.start(logdir)

profiler.stop()
with self.assertRaises(errors.UnavailableError):
    profiler.stop()

# Test with a bad logdir, and it correctly raises exception and deletes
# profiler.
# pylint: disable=anomalous-backslash-in-string
profiler.start('/dev/null/\/\/:123')
# pylint: enable=anomalous-backslash-in-string
with self.assertRaises(Exception):
    profiler.stop()
profiler.start(logdir)
profiler.stop()
