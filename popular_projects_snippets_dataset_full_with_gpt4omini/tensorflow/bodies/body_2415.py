# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/light_outside_compilation_test.py
"""Dynamic bounds are tighter than those deduced by shape inference."""

@def_function.function(jit_compile=True)
def compiled_f(x):
    exit(test_ops_for_light_outside_compilation.test_dynamic_tf_with_bound(
        x, max_size=5))

with context.device('/gpu:0'):
    z = random_ops.random_normal([10])
    hlo = compiled_f.experimental_get_compiler_ir(z)()
    self.assertFilecheck(
        hlo, r"""
          CHECK: f32[5]{0} custom-call(f32[10]{0} [[v:.*]]), custom_call_target="GenericTfCallbackGPU"
          """)
