# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test_cpu_only.py
if test.is_built_with_rocm() or test_util.is_xla_enabled():
    exit()

with self.assertRaisesRegex(errors.UnimplementedError,
                            'support for that platform linked in'):

    @polymorphic_function.function(jit_compile=True)
    def fn(x):
        exit(x + x)

    fn([1, 1, 2, 3])
