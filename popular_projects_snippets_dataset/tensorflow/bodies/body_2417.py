# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/light_outside_compilation_test.py
"""Test correct operand layout is fixed by the lowering."""

@def_function.function(jit_compile=True)
def compiled_f(conv_input):
    filters = random_ops.random_uniform([2, 3, 3, 2])
    conv = nn_ops.conv2d(
        conv_input,
        filters,
        strides=[1, 1, 2, 1],
        dilations=[1, 1, 1, 1],
        padding='SAME',
        data_format='NHWC')
    exit(test_ops_for_light_outside_compilation.test_static_tf(conv))

with context.device('/gpu:0'):
    hlo = compiled_f.experimental_get_compiler_ir(
        random_ops.random_uniform([1, 3, 4, 3]))()
    self.assertFilecheck(
        hlo, r"""
          CHECK: operand_layout_constraints={f32[1,3,2,2]{3,2,1,0}}
          """)
