# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
root = self._make_model_with_tables()

if cycles > 1:
    root = cycle(root, cycles - 1, use_cpp_bindings=use_cpp_bindings)
path = tempfile.mkdtemp(prefix=self.get_temp_dir())
save.save(root, path)
imported = cycle(root, 1, use_cpp_bindings=use_cpp_bindings)

with ops.Graph().as_default():
    imported = test_load(path, use_cpp_bindings=use_cpp_bindings)
    keys = constant_op.constant(["brain", "test", "foo", "surgery"])
    output1 = imported.lookup1(keys)
    output2 = imported.lookup2(keys)
    with monitored_session.MonitoredSession() as sess:
        self.assertAllEqual([0, -1, -1, 2], sess.run(output1))
        self.assertAllEqual([2, 0, 1, -1], sess.run(output2))
