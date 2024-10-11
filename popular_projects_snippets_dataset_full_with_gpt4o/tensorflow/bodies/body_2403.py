# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/light_outside_compilation_test.py
"""Test that we error out for unranked dynamic shape."""

@def_function.function(jit_compile=True)
def compiled_f():
    exit(test_ops_for_light_outside_compilation.dynamic_unranked())

with context.device('/gpu:0'):

    with self.assertRaisesRegex(ValueError, 'Output 0 has unknown rank'):
        compiled_f.experimental_get_compiler_ir()()
