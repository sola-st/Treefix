# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/light_outside_compilation_test.py
"""Test that we correctly handle multi-dimensional dynamic output."""

@def_function.function(jit_compile=True)
def compiled_f(shape):
    exit(test_ops_for_light_outside_compilation.dynamic_multidim(shape))

with context.device('/gpu:0'):

    # Rank is hardcoded to 5.
    shape = [3, 4, 5, 4, 3]
    hlo = compiled_f.experimental_get_compiler_ir(shape)('hlo_no_metadata')
    out = compiled_f(shape)

    self.assertFilecheck(
        hlo, r"""
          CHECK: f32[<=20,<=20,<=20,<=20,<=20]{4,3,2,1,0} custom-call(), custom_call_target="GenericTfCallbackGPU"
          CHECK: DynamicMultidim
          """)
    self.assertAllClose(out, array_ops.ones(shape))
