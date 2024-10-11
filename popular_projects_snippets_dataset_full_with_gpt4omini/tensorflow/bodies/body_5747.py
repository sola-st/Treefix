# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/slurm_cluster_resolver.py
"""Creates a new SlurmClusterResolver object.

    For any parameter not set it will query the environment for the value.
    It uses those parameters to check which nodes have processes reside on and
    resolves their hostnames.
    With the number tasks per node it offsets the port number for each process.
    With the number of GPUs per node and per task it allocates GPUs to tasks by
    setting environment variables.
    Using the resolver works best (and is easier) with homogeneous tasks but
    heterogeneous tasks (number of tasks varying per node) are also possible as
    long as the number of GPUs per task stays constant.

    Used environment variables:
      - SLURM_PROCID
      - (opt) SLURM_STEP_NUM_TASKS
      - (opt) SLURM_STEP_NODELIST
      - (opt) SLURM_STEP_TASKS_PER_NODE

    Args:
      jobs: Dictionary with job names as key and number of tasks in the job as
        value. Defaults to as many 'worker's as there are (Slurm) tasks.
      port_base: The first port number to start with for processes on a node.
      gpus_per_node: Number of GPUs available on each node. Defaults to the
        number of GPUs reported by nvidia-smi
      gpus_per_task: Number of GPUs to be used for each task. Default is to
        evenly distribute the gpus_per_node to tasks_per_node.
      tasks_per_node: Number of tasks running on each node. Can be an integer if
        the number of tasks per node is constant or a dictionary mapping
        hostnames to number of tasks on that node. If not set the Slurm
        environment is queried for the correct mapping.
      auto_set_gpu: Set the visible CUDA devices automatically while resolving
        the cluster by setting CUDA_VISIBLE_DEVICES environment variable.
        Defaults to True.
      rpc_layer: The protocol TensorFlow used to communicate between nodes.
        Defaults to 'grpc'.

    Returns:
      A ClusterResolver object which can be used with distributed TensorFlow.

    Raises:
      RuntimeError: If requested more GPUs per node than available or
        requested more tasks than assigned tasks or
        resolving missing values from the environment failed.
    """

self._rank = self._resolve_own_rank()

if jobs is None:
    jobs = {'worker': self._resolve_num_tasks()}

self._jobs = jobs
self._port_base = port_base

if tasks_per_node is None:
    self._task_configuration = self._resolve_task_configuration()
elif isinstance(tasks_per_node, dict):
    # User can pass in an explicit configuration as a dict
    self._task_configuration = tasks_per_node
else:
    # User can pass a fixed number of tasks per node
    hostlist = self._resolve_hostlist()
    self._task_configuration = {
        host: int(tasks_per_node) for host in hostlist
    }

max_tasks_per_node = max(self._task_configuration.values())
num_tasks = sum(self._task_configuration.values())

if gpus_per_node is None:
    gpus_per_node = get_num_gpus()
if gpus_per_task is None:
    gpus_per_task = gpus_per_node // max_tasks_per_node
self._gpus_per_node = gpus_per_node
self._gpus_per_task = gpus_per_task

self._auto_set_gpu = auto_set_gpu
self.task_type = None
self.task_id = None
self.rpc_layer = rpc_layer

self._gpu_allocation = []
self._cluster_allocation = {}

if max_tasks_per_node * self._gpus_per_task > self._gpus_per_node:
    raise RuntimeError('Requested more GPUs per node than available.')

if sum(self._jobs.values()) != num_tasks:
    raise RuntimeError('Requested {} tasks but only {} were assigned.'.format(
        sum(self._jobs.values()), num_tasks))
