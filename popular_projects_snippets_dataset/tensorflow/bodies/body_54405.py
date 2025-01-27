# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with ops.name_scope(None, "default", skip_on_eager=False) as scope:
    self.assertEqual(scope, "default/")
    with ops.name_scope(None, "default2", skip_on_eager=False) as scope2:
        self.assertEqual(scope2, "default/default2/")
