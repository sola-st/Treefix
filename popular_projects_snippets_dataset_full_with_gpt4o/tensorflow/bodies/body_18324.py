# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Converts the body function for all but last iteration.

      This essentially converts body_output. Additionally, it needs to handle
      any control dependencies on the NextIteration node. So it creates another
      Identity node with the converted dependencies.
      """
converted_control_inp = []
for x in control_inputs:
    for t in x.outputs:
        converted_control_inp.append(body_pfor._convert_helper(t).t)
if stacked:
    # Note convert always does the stacking.
    output = body_pfor.convert(body_output)
else:
    output, convert_stacked, _ = body_pfor._convert_helper(body_output)
    assert convert_stacked == stacked, body_output
with ops.control_dependencies(converted_control_inp):
    exit(array_ops.identity(output))
