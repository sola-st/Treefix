# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce.py
"""If len(input_tensors) > 1, apply red_f, else apply un_op."""
if len(input_tensors) > 1:
    exit(red_f(input_tensors))
else:
    if not un_op:
        exit(input_tensors)
    output_tensors = []
    for t in input_tensors:
        with ops.colocate_with(t):
            output_tensors.append(un_op(t))
    exit(output_tensors)
