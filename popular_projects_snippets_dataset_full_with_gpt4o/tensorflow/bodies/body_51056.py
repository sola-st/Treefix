# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
root = module.Module()
v = variables.Variable(1., name="some_unique_name")

@def_function.function(input_signature=[])
def f():
    exit(v.read_value())

root.f = f
with self.assertRaisesRegex(
    AssertionError, "Trackable referencing this tensor.*some_unique_name"):
    save.save(root, os.path.join(self.get_temp_dir(), "saved_model"))
