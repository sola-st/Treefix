# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/light_outside_compilation_test.py
"""Test operations with must-be-constant input."""

@def_function.function(jit_compile=True)
def compiled_f(x, y):
    exit(test_ops_for_light_outside_compilation.test_tf_must_be_constant(
        x, constant_to_add=y))

with context.device('/gpu:0'):

    z = random_ops.random_normal([10])
    hlo = compiled_f.experimental_get_compiler_ir(z, 5)('hlo_no_metadata')

    self.assertFilecheck(
        hlo, r"""
          CHECK: custom-call(f32[10]{0} [[v:.*]]), custom_call_target="GenericTfCallbackGPU"
          CHECK: TestTfMustBeConstant
          """)

    expected_output = [j + 5 for j in z]
    self.assertAllClose(compiled_f(z, 5), expected_output)
