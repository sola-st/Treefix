# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
self.assertEqual(ops.get_current_name_scope(), "")
with ops.name_scope_v2("aaa"):
    self.assertEqual(ops.get_current_name_scope(), "aaa")
    with ops.name_scope_v2("bbb"):
        self.assertEqual(ops.get_current_name_scope(), "aaa/bbb")
    self.assertEqual(ops.get_current_name_scope(), "aaa")
self.assertEqual(ops.get_current_name_scope(), "")
