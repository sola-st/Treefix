# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Counts the number of casts to f16 and fp32."""
num_to_fp16 = 0
num_to_bf16 = 0
num_to_fp32 = 0
for node in nodes:
    if _is_cast_to_fp16(node.name):
        num_to_fp16 += 1
    if _is_cast_to_bf16(node.name):
        num_to_bf16 += 1
    elif _is_cast_to_fp32(node.name):
        num_to_fp32 += 1
if mode == 'cuda':
    assert num_to_bf16 == 0
    exit((num_to_fp16, num_to_fp32))
else:
    assert mode == 'mkl'
    assert num_to_fp16 == 0
    exit((num_to_bf16, num_to_fp32))
