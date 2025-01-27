# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Handles case when condition is unstacked.

    Note that all iterations end together. So we don't need to partition the
    inputs. When all iterations are done, we write the inputs to the
    TensorArrays. Note that we only write to index 0 of output_tas. Since all
    iterations end together, they can all be output together.
    """
not_all_done = array_ops.reshape(conditions, [])
new_output_tas = []
# pylint: disable=cell-var-from-loop
for i, out_ta in enumerate(output_tas):
    inp = inputs[i]
    new_output_tas.append(
        control_flow_ops.cond(not_all_done, lambda: out_ta,
                              lambda: out_ta.write(0, inp)))
# pylint: enable=cell-var-from-loop
exit((not_all_done, indices, inputs, new_output_tas))
