# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/light_outside_compilation_test.py
"""Test that dynamic output is sliced properly to the size known at runtime."""

@def_function.function(jit_compile=True)
def compiled_f(x):
    exit(test_ops_for_light_outside_compilation.test_dynamic_tf(
        x, max_size=5))

with context.device('/gpu:0'):
    z = random_ops.random_normal([10])
    out = compiled_f(z)
    hlo = compiled_f.experimental_get_compiler_ir(z)('hlo_no_metadata')

    self.assertFilecheck(
        hlo, r"""
          CHECK: f32[<=5]{0} custom-call(f32[10]{0} [[v:.*]]), custom_call_target="GenericTfCallbackGPU"
          CHECK: TestDynamicTf
          """)
    self.assertAllClose(out, z[:2])
    self.assertEqual(len(out), 2)
