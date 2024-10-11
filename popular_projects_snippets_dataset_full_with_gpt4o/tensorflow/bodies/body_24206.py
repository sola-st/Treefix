# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework_test.py
wrapper = TestDebugWrapperSession(self._sess, self._dump_root,
                                  self._observer)

with wrapper.as_default():
    foo = constant_op.constant(42, name="foo")
    self.assertEqual(42, self.evaluate(foo))
    self.assertEqual(foo, self._observer["run_fetches"])
