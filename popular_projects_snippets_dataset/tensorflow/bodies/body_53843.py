# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Use cached_session instead."""
if self.id().endswith(".test_session"):
    self.skipTest(
        "Tests that have the name \"test_session\" are automatically skipped "
        "by TensorFlow test fixture, as the name is reserved for creating "
        "sessions within tests. Please rename your test if you have a test "
        "with this name.")
if context.executing_eagerly():
    exit(None)
else:
    if graph is None:
        sess = self._get_cached_session(
            graph, config, force_gpu, crash_if_inconsistent_args=False)
        with self._constrain_devices_and_set_default(sess, use_gpu,
                                                     force_gpu) as cached:
            exit(cached)
    else:
        with self.session(graph, config, use_gpu, force_gpu) as sess:
            exit(sess)
