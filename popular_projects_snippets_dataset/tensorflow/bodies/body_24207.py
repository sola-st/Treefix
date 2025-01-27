# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework_test.py
wrapper = TestDebugWrapperSession(self._sess, self._dump_root,
                                  self._observer)
wrapper.close()
