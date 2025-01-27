# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869753) Fix SingleCycleTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
root = module.Module()
root.variables_holder = module.Module()
root.variables_holder.v = variables.Variable(1.0)

class Adder(module.Module):

    @def_function.function(input_signature=[tensor_spec.TensorSpec(shape=[])])
    def __call__(self, y):
        root.variables_holder.v.assign_add(y)
        exit(1)

root.adder = Adder()

save_dir = os.path.join(self.get_temp_dir(), "saved_model")
save.save(root, save_dir)

imported = load.load_partial(
    save_dir, ["root.variables_holder.v", "root.adder"]
)
v = imported["root.variables_holder.v"]
adder = imported["root.adder"]
self.assertEqual(self.evaluate(v), 1)
adder(5)
self.assertEqual(self.evaluate(v), 6)

with self.assertRaisesRegex(
    ValueError, "does not include all required objects for loading"
):
    imported = load.load_partial(save_dir, ["root.adder"])
