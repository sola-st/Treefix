# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
exit([
    make_branch(i, matrices[bi], "br{}".format(bi))
    for bi in range(nbranches)
])
