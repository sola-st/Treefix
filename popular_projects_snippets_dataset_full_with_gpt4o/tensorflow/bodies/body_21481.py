# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
with ops_lib.Graph().as_default() as g:
    v = resource_variable_ops.ResourceVariable(1.0, name="v")
    with ops_lib.name_scope("saver1"):
        saver_module.Saver()
    with ops_lib.name_scope("saver2"):
        saver_module.Saver({"name": v})
ops_in_saver1_scope_but_not_save_scope = [
    op for op in g.get_operations()
    if (op.name.startswith("saver1/") and
        not op.name.startswith("saver1/save/"))]
self.assertEqual(ops_in_saver1_scope_but_not_save_scope, [])
ops_in_saver2_scope_but_not_save_scope = [
    op for op in g.get_operations()
    if (op.name.startswith("saver2/") and
        not op.name.startswith("saver2/save/"))]
self.assertEqual(ops_in_saver2_scope_but_not_save_scope, [])
