# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
# We have to create a global in-process cluster because once an in-process
# tensorflow server is created, there is no way to terminate it. Please see
# multi_worker_test_base.py for more details.
# TODO(yuefengz): use the utitliy from multi_worker_test_base.
cls._workers, cls._ps = test_util.create_local_cluster(
    NUM_WORKERS, num_ps=NUM_PS)
cls._cluster_spec = {
    WORKER: [
        _strip_protocol(_bytes_to_str(w.target)) for w in cls._workers
    ],
    PS: [_strip_protocol(_bytes_to_str(ps.target)) for ps in cls._ps]
}
