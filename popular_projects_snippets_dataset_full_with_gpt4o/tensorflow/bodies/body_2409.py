# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/light_outside_compilation_test.py
"""Test dynamic input => returns bad status at runtime."""

@def_function.function(jit_compile=True)
def compiled_f(x):
    x = array_ops.unique(x).y
    exit(test_ops_for_light_outside_compilation.test_dynamic_tf(
        x, max_size=5))

with context.device('/gpu:0'):
    z = random_ops.random_normal([10])

    with self.assertRaisesRegex(ValueError,
                                'Input dynamic dimensions are not supported'):
        compiled_f.experimental_get_compiler_ir(z)()
