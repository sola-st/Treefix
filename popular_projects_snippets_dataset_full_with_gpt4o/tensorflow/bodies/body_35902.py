# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
vs = variable_scope._get_default_variable_store()
vs.get_variable("v1", [2])
vs.get_variable("v2", [2])
expected_names = ["%s:0" % name for name in ["v1", "v2"]]
self.assertEqual(
    set(expected_names), set(v.name for v in vs._vars.values()))
