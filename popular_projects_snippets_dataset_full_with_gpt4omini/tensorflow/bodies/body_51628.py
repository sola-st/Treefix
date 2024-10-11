# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264882686) Fix DeferredInitModuleVariablesTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
if not config.get_soft_device_placement():
    self.skipTest("This test only works for soft device placement is on")
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
ncols = 16
nrows = 32
model = _TestModel(rows=nrows, cols=ncols)
x = array_ops.zeros(shape=(ncols, 2), dtype=dtypes.float32)
y = model(x)
save.save(
    model,
    save_dir,
    options=save_options.SaveOptions(
        experimental_variable_policy=save_options.VariablePolicy.SAVE_VARIABLE_DEVICES
    ),
)
loaded_on_cpu = test_load(
    path=save_dir,
    options=load_options.LoadOptions(
        experimental_variable_policy=save_options.VariablePolicy.SAVE_VARIABLE_DEVICES
    ),
    use_cpp_bindings=use_cpp_bindings,
)
loaded_on_gpu = test_load(save_dir)
self.assertIn("CPU", loaded_on_cpu.table.device)
self.assertIn("GPU", loaded_on_gpu.table.device)
