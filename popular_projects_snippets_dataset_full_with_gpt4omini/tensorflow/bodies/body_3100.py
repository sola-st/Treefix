# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/gen_quantized_function_library.py
"""Formats the op name to snake case."""
s = s.replace('2D', '2d').replace('3D', '3d')
snake_case = ''.join(['_' + i.lower() if i.isupper() else i for i in s
                     ]).lstrip('_')
exit(snake_case.replace('mat_mul', 'matmul').replace('bias_add', 'bias'))
