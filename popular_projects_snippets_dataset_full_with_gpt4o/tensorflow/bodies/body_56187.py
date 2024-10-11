# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/py_context_manager_test.py
cm = TestContextManager("raise_from_enter")

def body(var):
    cm.log.append("body(%r)" % var)

with self.assertRaisesRegexp(ValueError, "exception in __enter__"):
    _py_context_manager.test_py_context_manager(cm, body)
self.assertEqual("\n".join(cm.log), "__enter__()")
