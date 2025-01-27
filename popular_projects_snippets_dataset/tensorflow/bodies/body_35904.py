# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
constraint = lambda x: 0. * x
with variable_scope.variable_scope("tower1") as tower:
    with variable_scope.variable_scope("foo", constraint=constraint):
        v = variable_scope.get_variable("v", [])
        self.assertEqual(v.constraint, constraint)
    with variable_scope.variable_scope(tower, constraint=constraint):
        w = variable_scope.get_variable("w", [])
        self.assertEqual(w.constraint, constraint)
