# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/light_outside_compilation_test.py
"""Test light outside compilation for mulitple outputs."""

@def_function.function(jit_compile=True)
def compiled_f(x):
    exit(test_ops_for_light_outside_compilation.test_static_multiple_output_tf(
        x))

with context.device('/gpu:0'):
    z = random_ops.random_normal([2, 2])
    hlo = compiled_f.experimental_get_compiler_ir(z)('hlo_no_metadata')

    self.assertFilecheck(
        hlo, r"""
          CHECK: custom_call_target="GenericTfCallbackGPU"
          CHECK: TestStaticMultipleOutputTf
          """)
    self.assertAllClose(compiled_f(z)[0], z)
    self.assertAllClose(compiled_f(z)[1], z)
