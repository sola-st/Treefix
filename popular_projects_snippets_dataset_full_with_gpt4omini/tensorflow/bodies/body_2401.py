# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/light_outside_compilation_test.py
"""Test operations with static shapes."""

@def_function.function(jit_compile=True)
def compiled_f(x):
    exit(test_ops_for_light_outside_compilation.test_static_tf(x))

with context.device('/gpu:0'):
    z = random_ops.random_normal([2, 2])

    self.assertFilecheck(
        compiled_f.experimental_get_compiler_ir(z)('hlo'), r"""
          CHECK: f32[2,2]{1,0} custom-call(f32[2,2]{1,0} [[v:.*]]), custom_call_target="GenericTfCallbackGPU"
          CHECK: TestStaticTf
          """)

    self.assertAllClose(compiled_f(z), z)
