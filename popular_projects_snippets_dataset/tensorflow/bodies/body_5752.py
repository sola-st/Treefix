# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/slurm_cluster_resolver.py
"""Returns a ClusterSpec object based on the latest instance group info.

    This returns a ClusterSpec object for use based on information from the
    specified initialization parameters and Slurm environment variables. The
    cluster specification is resolved each time this function is called. The
    resolver extract hostnames of nodes by scontrol and pack tasks in that
    order until a node a has number of tasks that is equal to specification.
    GPUs on nodes are allocated to tasks by specification through setting
    CUDA_VISIBLE_DEVICES environment variable.

    Returns:
      A ClusterSpec containing host information retrieved from Slurm's
        environment variables.
    """

task_list = []
self._gpu_allocation = []
self._cluster_allocation = {}

# Sort to make sure the order is the same for each run
for host, num_tasks in sorted(self._task_configuration.items()):
    for port_offset, gpu_offset in zip(
        range(num_tasks), range(0, self._gpus_per_node, self._gpus_per_task)):

        host_addr = '%s:%d' % (host, self._port_base + port_offset)
        task_list.append(host_addr)
        gpu_id_list = []

        for gpu_id in range(gpu_offset, gpu_offset + self._gpus_per_task):
            gpu_id_list.append(str(gpu_id))

        self._gpu_allocation.append(','.join(gpu_id_list))

cluster_rank_offset_start = 0
cluster_rank_offset_end = 0

# Sort to make sure the order is the same for each run
for task_type, num_tasks in sorted(self._jobs.items()):
    cluster_rank_offset_end = cluster_rank_offset_start + num_tasks

    self._cluster_allocation[task_type] = (
        task_list[cluster_rank_offset_start:cluster_rank_offset_end])

    if cluster_rank_offset_start <= self._rank < cluster_rank_offset_end:
        self.task_type = task_type
        self.task_id = self._rank - cluster_rank_offset_start

    cluster_rank_offset_start = cluster_rank_offset_end

if self._auto_set_gpu:
    os.environ['CUDA_VISIBLE_DEVICES'] = self._gpu_allocation[self._rank]

exit(ClusterSpec(self._cluster_allocation))
