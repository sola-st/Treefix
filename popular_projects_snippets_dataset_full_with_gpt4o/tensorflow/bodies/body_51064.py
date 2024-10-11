# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
root = autotrackable.AutoTrackable()
root.v1 = variables.Variable(3.)
root.v2 = variables.Variable(2.)
root.f = def_function.function(lambda x: root.v1 * root.v2 * x)
root.f(constant_op.constant(1.))
to_save = root.f.get_concrete_function(constant_op.constant(1.))
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
save.save(root, save_dir, to_save)
self.assertAllEqual({"output_0": 12.},
                    _import_and_infer(save_dir, {"x": 2.}))
