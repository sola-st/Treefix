# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/py_context_manager_test.py
cm = TestContextManager("raise_from_exit")

def body(var):
    cm.log.append("body(%r)" % var)

# Note: this does *not* raise an exception (but does log a warning):
_py_context_manager.test_py_context_manager(cm, body)
self.assertEqual("\n".join(cm.log), NO_EXCEPTION_LOG)
