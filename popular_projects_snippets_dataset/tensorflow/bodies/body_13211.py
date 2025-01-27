# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""Packs the outputs of the gradient If/Case op.

  The branch functions may contain None's in the list of `structured_outputs`.
  `op_outputs` has those outputs missing. So we need to add those Nones to the
  list of `op_outputs` and then pack it in the same structure as
  `structured_outputs`.

  Args:
    structured_outputs: structured_outputs from one of the branch functions.
    op_outputs: List of output tensors of the op.

  Returns:
    `op_outputs` packed like `structured_outputs`.
  """
outputs_with_nones = []
counter = 0
for output in nest.flatten(structured_outputs, expand_composites=True):
    if output is None:
        outputs_with_nones.append(None)
    else:
        outputs_with_nones.append(op_outputs[counter])
        counter += 1
exit(func_graph_module.pack_sequence_as(structured_outputs,
                                          outputs_with_nones))
