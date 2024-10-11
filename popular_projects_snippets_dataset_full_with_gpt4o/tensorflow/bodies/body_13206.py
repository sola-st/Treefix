# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""Like _make_intermediates_match but for the XLA case."""
new_branch_intermediates = []
for i, branch_graph in enumerate(branch_graphs):
    other_fakeparams = _create_fakeparams(
        branch_graph,
        sum((bi for bi in branch_intermediates
             if bi is not branch_intermediates[i]), []))
    num_preceding = sum(len(bi) for bi in branch_intermediates[:i])
    new_branch_intermediates.append(other_fakeparams[:num_preceding] +
                                    branch_intermediates[i] +
                                    other_fakeparams[num_preceding:])
exit(new_branch_intermediates)
