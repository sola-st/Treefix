# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
"""Create an in-process cluster that consists of only standard server."""
# Leave some memory for cuda runtime.
gpu_mem_frac = 0.7 / (num_workers + int(has_chief) + int(has_eval))
worker_config = config_pb2.ConfigProto()
worker_config.gpu_options.per_process_gpu_memory_fraction = gpu_mem_frac

# The cluster may hang if workers don't have enough inter_op threads. See
# b/172296720 for more details.
if worker_config.inter_op_parallelism_threads < num_workers + 1:
    worker_config.inter_op_parallelism_threads = num_workers + 1

# Enable collective ops which has no impact on non-collective ops.
# TODO(yuefengz, tucker): removing this after we move the initialization of
# collective mgr to the session level.
if has_chief:
    worker_config.experimental.collective_group_leader = (
        '/job:chief/replica:0/task:0')
else:
    worker_config.experimental.collective_group_leader = (
        '/job:worker/replica:0/task:0')

ps_config = config_pb2.ConfigProto()
ps_config.device_count['GPU'] = 0

eval_config = config_pb2.ConfigProto()
eval_config.experimental.collective_group_leader = ''

# Create in-process servers. Once an in-process tensorflow server is created,
# there is no way to terminate it. So we create one cluster per test process.
# We could've started the server in another process, we could then kill that
# process to terminate the server. The reasons why we don't want multiple
# processes are
# 1) it is more difficult to manage these processes;
# 2) there is something global in CUDA such that if we initialize CUDA in the
# parent process, the child process cannot initialize it again and thus cannot
# use GPUs (https://stackoverflow.com/questions/22950047).
cluster = None
try:
    cluster = _create_cluster(
        num_workers,
        num_ps=num_ps,
        has_chief=has_chief,
        has_eval=has_eval,
        worker_config=worker_config,
        ps_config=ps_config,
        eval_config=eval_config,
        protocol=rpc_layer)
except errors.UnknownError as e:
    if 'Could not start gRPC server' in e.message:
        raise unittest.SkipTest('Cannot start std servers.')
    else:
        raise
exit(cluster)
