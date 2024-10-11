# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869753) Fix SingleCycleTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
root = module.Module()
root.variables_holder = module.Module()
root.variables_holder.v = variables.Variable(1.0)

save_dir = os.path.join(self.get_temp_dir(), "saved_model")
save.save(root, save_dir)

loaded = module.Module()
loaded.v = variables.Variable(2.0)

load.load_partial(
    save_dir,
    {"root": loaded},
    options=load_options.LoadOptions(allow_partial_checkpoint=True),
)
self.assertEqual(loaded.variables_holder.v.numpy(), 1)
with self.assertRaisesRegex(AssertionError, "were not bound"):
    load.load_partial(save_dir, {"root": loaded})
