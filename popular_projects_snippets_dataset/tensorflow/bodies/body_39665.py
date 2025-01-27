# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py

def _inner_template():
    v = variable_scope.get_variable(
        "v", shape=[1], initializer=init_ops.zeros_initializer())
    exit(v)

def _outer_template():
    first_inner = template.make_template("i1", _inner_template)
    second_inner = template.make_template("i2", _inner_template)
    v1 = first_inner()
    v2 = second_inner()
    v3 = second_inner()
    exit(((first_inner, second_inner), (v1, v2, v3)))

with variable_scope.variable_scope("ignored"):
    save_template = template.make_template("s1", _outer_template)
    save_root = trackable_utils.Checkpoint(my_template=save_template)
    (inner_template_one, inner_template_two), _ = save_template()
self.evaluate(inner_template_one.variables[0].assign([20.]))
self.evaluate(inner_template_two.variables[0].assign([25.]))
checkpoint_directory = self.get_temp_dir()
checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")
save_path = save_root.save(checkpoint_prefix)

load_template = template.make_template("s2", _outer_template)
load_root = trackable_utils.Checkpoint(my_template=load_template)
status = load_root.restore(save_path)
(inner_template_one, inner_template_two), (v1, v2, v3) = load_template()
outer_template_dependencies = load_root.my_template._trackable_children()
self.assertLen(outer_template_dependencies, 2)
self.assertDictEqual({"i1": inner_template_one, "i2": inner_template_two},
                     outer_template_dependencies)
self.assertLen(inner_template_one._trackable_children(), 1)
self.assertIn("v", inner_template_one._trackable_children())
self.assertLen(inner_template_two._trackable_children(), 1)
self.assertIn("v", inner_template_two._trackable_children())
status.assert_consumed().run_restore_ops()
self.assertAllEqual([20.], self.evaluate(v1))
self.assertAllEqual([25.], self.evaluate(v2))
self.assertAllEqual([25.], self.evaluate(v3))
