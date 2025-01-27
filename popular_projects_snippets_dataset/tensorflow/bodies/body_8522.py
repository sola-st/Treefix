# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
"""Creates and starts local servers and returns the cluster_spec dict."""

worker_ports = [pick_unused_port() for _ in range(num_workers)]
ps_ports = [pick_unused_port() for _ in range(num_ps)]

cluster_dict = {}
if num_workers > 0:
    cluster_dict[worker_name] = ['localhost:%s' % port for port in worker_ports]
if num_ps > 0:
    cluster_dict[ps_name] = ['localhost:%s' % port for port in ps_ports]
if has_eval:
    cluster_dict['evaluator'] = ['localhost:%s' % pick_unused_port()]
if has_chief:
    cluster_dict[chief_name] = ['localhost:%s' % pick_unused_port()]

cs = server_lib.ClusterSpec(cluster_dict)

for i in range(num_workers):
    server_lib.Server(
        cs,
        job_name=worker_name,
        protocol=protocol,
        task_index=i,
        config=worker_config,
        start=True)

for i in range(num_ps):
    server_lib.Server(
        cs,
        job_name=ps_name,
        protocol=protocol,
        task_index=i,
        config=ps_config,
        start=True)

if has_chief:
    server_lib.Server(
        cs,
        job_name=chief_name,
        protocol=protocol,
        task_index=0,
        config=worker_config,
        start=True)

if has_eval:
    server_lib.Server(
        cs,
        job_name='evaluator',
        protocol=protocol,
        task_index=0,
        config=eval_config,
        start=True)

exit(cluster_dict)
