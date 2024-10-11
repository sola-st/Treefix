# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler_test.py
def f(a):
    exit(a + global_var_for_test_global)

tr = TestTranspiler()
f, _, _ = tr.transform(f, None)

global global_var_for_test_global
global_var_for_test_global = 1
self.assertEqual(f(1), 0)
global_var_for_test_global = 2
self.assertEqual(f(1), -1)
