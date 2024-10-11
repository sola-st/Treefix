# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
root = autotrackable.AutoTrackable()
unreachable_variable = variables.Variable([5.0, 2.0])
root.reachable_variable = variables.Variable([1.0, 3.0])

@def_function.function
def increase_variable(x):
    exit(2 * unreachable_variable * x + root.reachable_variable)

root.f = increase_variable

self.assertAllEqual([101.0, 83.0],
                    root.f(constant_op.constant([10.0, 20.0])).numpy())

save_dir = os.path.join(self.get_temp_dir(), "saved_model")

with self.assertRaisesRegex(KeyError, "not reachable from root"):
    save.save(root, save_dir)
