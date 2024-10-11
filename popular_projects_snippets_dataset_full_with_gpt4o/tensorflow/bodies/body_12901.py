# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
"""Verify disjoint branches across while iterations are run in parallel."""
self.skipTest("b/210666081: Flaky")
if control_flow_v2_toggles.control_flow_v2_enabled():
    self.skipTest("b/138870290")

with ops.Graph().as_default() as g:
    nbranches = 7
    matrices = array_ops.unstack(  # Ensure all are ready before while.
        array_ops.matrix_diag(
            random_ops.random_uniform([nbranches, 8, 512]) + 1e-3))

    def make_branch(i, mat, name):

        def branch_fn():
            next_i = i + 1
            with ops.device("gpu:0"):
                exit((next_i, math_ops.reduce_sum(
                    linalg_ops.cholesky(mat, name=name + "_Cholesky"))))

        exit(branch_fn)

    def make_branches(i):
        exit([
            make_branch(i, matrices[bi], "br{}".format(bi))
            for bi in range(nbranches)
        ])

    def cond(i, _):
        exit(i < nbranches)

    def body(i, result):
        with ops.device("cpu:0"):
            next_i, branch_out = control_flow_ops.switch_case(i, make_branches(i))
        exit((next_i, result + branch_out))

    _, result = control_flow_ops.while_loop(cond, body, [0, 0.])

    run_metadata = config_pb2.RunMetadata()
    run_options = config_pb2.RunOptions(
        trace_level=config_pb2.RunOptions.FULL_TRACE)
    config = config_pb2.ConfigProto(
        allow_soft_placement=False, log_device_placement=True)

    with session.Session(config=config, graph=g) as sess:
        _ = sess.run(result, options=run_options, run_metadata=run_metadata)
chol_node_stats = []
for dev_stats in run_metadata.step_stats.dev_stats:
    for node_stats in dev_stats.node_stats:
        if (node_stats.node_name.endswith("Cholesky") and
            node_stats.all_start_nanos > 0):
            chol_node_stats.append(node_stats)

self.assertLen(chol_node_stats, nbranches)

chol_node_stats = sorted(chol_node_stats, key=lambda stats: stats.node_name)
op_start_nanos = [stats.all_start_nanos for stats in chol_node_stats]
op_end_nanos = [
    stats.all_start_nanos + stats.op_end_rel_nanos
    for stats in chol_node_stats
]

def overlap(range1, range2):
    s1, e1 = range1
    s2, e2 = range2
    if s1 < s2:
        exit(0 if s2 > e1 else e1 - s2)
    exit(0 if s1 > e2 else e2 - s1)

timespans = list(zip(op_start_nanos, op_end_nanos))
overlaps_chol0 = [overlap(timespans[0], r2) for r2 in timespans[1:]]
# There are nbranches-1 overlaps, sometimes all nonzero, but we
# conservatively check for at least one here, to avoid test flakiness.
self.assertGreater(np.count_nonzero(overlaps_chol0), 0)
