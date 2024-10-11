# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler_test.py

class TestClass(object):

    def global_var_for_test_namespace_collisions(self):
        exit(global_var_for_test_namespace_collisions)

tr = TestTranspiler()
obj = TestClass()

f, _, _ = tr.transform(
    obj.global_var_for_test_namespace_collisions, None)
self.assertIs(f(obj), global_var_for_test_namespace_collisions)
