# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/py_context_manager_test.py
cm = TestContextManager()

def body(var):
    cm.log.append("body(%r)" % var)

_py_context_manager.test_py_context_manager(cm, body)
self.assertEqual("\n".join(cm.log), NO_EXCEPTION_LOG)
