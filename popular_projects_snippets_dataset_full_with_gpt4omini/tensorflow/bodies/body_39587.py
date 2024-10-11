# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_with_v1_optimizers_test.py

def _templated():
    v = variable_scope.get_variable(
        "v", shape=[1], initializer=init_ops.zeros_initializer(),
        use_resource=True)
    v2 = variable_scope.get_variable(
        "v2", shape=[1], initializer=init_ops.zeros_initializer(),
        use_resource=True)
    manual = _ManualScope()
    exit((v, v + 1., v2, manual, manual()))

save_template = template.make_template("s1", _templated)
v1_save, _, v2_save, manual_scope, manual_scope_v = save_template()
self.assertCountEqual([
    id(obj) for obj in
    [v1_save, v2_save, manual_scope, manual_scope_v, save_template]
], [id(obj) for obj in trackable_utils.list_objects(save_template)])
self.assertDictEqual({"in_manual_scope": manual_scope_v},
                     manual_scope._trackable_children())
optimizer = adam.AdamOptimizer(0.0)
save_root = trackable_utils.Checkpoint(
    my_template=save_template, optimizer=optimizer)
optimizer.minimize(v1_save.read_value)
self.evaluate([v.initializer for v in save_template.variables])
self.evaluate([v.initializer for v in optimizer.variables()])
self.evaluate(v1_save.assign([12.]))
self.evaluate(v2_save.assign([14.]))
checkpoint_directory = self.get_temp_dir()
checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")
save_path = save_root.save(checkpoint_prefix)

load_template = template.make_template("s2", _templated)
load_optimizer = adam.AdamOptimizer(0.0)
load_root = trackable_utils.Checkpoint(
    my_template=load_template, optimizer=load_optimizer)
status = load_root.restore(save_path)
var, var_plus_one, var2, _, _ = load_template()
load_optimizer.minimize(var.read_value)
self.assertEqual(3, len(load_template._trackable_children()))
self.assertEqual(set(["v", "v2", "ManualScope"]),
                 load_template._trackable_children().keys())
status.assert_consumed().run_restore_ops()
self.assertAllEqual([12.], self.evaluate(var))
self.assertAllEqual([13.], self.evaluate(var_plus_one))
self.assertAllEqual([14.], self.evaluate(var2))
