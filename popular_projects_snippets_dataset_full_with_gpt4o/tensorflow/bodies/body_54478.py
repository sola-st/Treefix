# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with ops.Graph().as_default() as g:
    with ops.name_scope("scope1"):
        with ops.name_scope("scope2"):
            with ops.name_scope("scope3"):
                self.assertEqual("scope1/scope2/scope3", g.get_name_scope())
            self.assertEqual("scope1/scope2", g.get_name_scope())
        self.assertEqual("scope1", g.get_name_scope())
    self.assertEqual("", g.get_name_scope())
