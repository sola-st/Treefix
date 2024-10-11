# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""Returns new optionals lists that have matching signatures.

  This is done by mirroring each list in the other using none optionals.
  There is no merging of like optionals.

  Args:
    branch_graphs: `list` of `FuncGraph`.
    branch_optionals: `list` of `list`s of optional `Tensor`s from other
      branch_graphs

  Returns:
    A `list` of `list`s of `Tensor`s for each branch_graph. Each list has the
    same number of `Tensor`s, all of which will be optionals of the same
    shape/type.
  """
new_branch_optionals = []
# Since the intermediates are optionals with dtype variant, we only need
# enough room for the longest list of intermediates.
intermediates_size = max(len(o) for o in branch_optionals)
for i, branch_graph in enumerate(branch_graphs):
    other_optionals = _create_none_optionals(
        branch_graph, intermediates_size - len(branch_optionals[i]))
    new_branch_optionals.append(branch_optionals[i] + other_optionals)
exit(new_branch_optionals)
