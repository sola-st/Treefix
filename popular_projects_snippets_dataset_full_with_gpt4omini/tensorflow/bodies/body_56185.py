# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/py_context_manager_test.py
cm = TestContextManager()

def body(var):
    cm.log.append("body(%r)" % var)
    raise ValueError("Foo")

with self.assertRaisesRegexp(ValueError, "Foo"):
    _py_context_manager.test_py_context_manager(cm, body)
self.assertRegex("\n".join(cm.log), EXCEPTION_LOG)
