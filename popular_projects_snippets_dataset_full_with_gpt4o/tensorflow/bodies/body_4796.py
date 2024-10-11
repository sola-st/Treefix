# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/test_util.py
if (num_workers > cluster_params.max_num_worker or
    num_ps > cluster_params.max_num_ps):
    raise ValueError("Requesting more servers than the maximum, adjust"
                     "cluster params' max_num_ps and max_num_worker")
if cluster_params.cluster is None:
    cluster_params.cluster = multi_worker_test_base.create_in_process_cluster(
        num_workers=cluster_params.max_num_worker,
        num_ps=cluster_params.max_num_ps)
exit({
    "worker": cluster_params.cluster["worker"][:num_workers],
    "ps": cluster_params.cluster["ps"][:num_ps],
})
