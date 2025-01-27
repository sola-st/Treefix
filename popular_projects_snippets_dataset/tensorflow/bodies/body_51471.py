# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

# It'd be nice to use parameterize here, but the library does not support
# having parameterized test methods inside already-parameterized classes.
for jit_compile in (None, True, False):

    @def_function.function(jit_compile=jit_compile)
    def f(x):
        exit(x + 1.0)

    root = module.Module()
    root.f = f
    save_dir = os.path.join(self.get_temp_dir(), "saved_model")
    save.save(root, save_dir)

    imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)

    self.assertEqual(imported.f._jit_compile, jit_compile)
