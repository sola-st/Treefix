# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
"""Instantiation of a `MultiProcessRunner`.

    Args:
      fn: Function to be run on child processes. This will be run on processes
        for all task types.
      cluster_spec: Dict for cluster spec. The utility function
        `tf.__internal__.distribute.multi_process_runner.create_cluster_spec`
        can be conveniently used to create such dict. The following is an
        example of cluster with three workers and two ps's.
        {"worker": ["worker0.example.com:2222",
                    "worker1.example.com:2222",
                    "worker2.example.com:2222"],
         "ps": ["ps0.example.com:2222",
                "ps1.example.com:2222"]}
      rpc_layer: RPC layer to use. Default value is 'grpc'.
      max_run_time: `None` or integer. If not `None`, child processes are forced
        to exit at approximately this many seconds after this utility is called.
        We achieve this through `signal.alarm()` api. Note that this is best
        effort at Python level since Python signal handler does not get executed
        when it runs lower level C/C++ code. So it can be delayed for
        arbitrarily long time. If any of the child process is still running when
        `max_run_time` is up, they will be force-terminated and an
        `UnexpectedSubprocessExitError` may be raised. If `None`, child
        processes are not forced to exit.
      grpc_fail_fast: Whether GRPC connection between processes should fail
        without retrying. Defaults to None, in which case the environment
        variable is not explicitly set.
      stream_output: True if the output/error from the subprocesses should be
        streamed to be printed in parent process' log. Defaults to True.
      return_output: If True, the output/error from the subprocesses should be
        collected to be attached to the resulting namedtuple returned from
        `join()`. The list of output can be retrieved via `stdout` attribute.
        Defaults to False.
      use_dill_for_args: Whether to use dill to pickle `args` and `kwargs`. dill
        can pickle more objects, but doesn't work with types in
        `multiprocessing` library like `Mutex`.
      daemon: Whether to start processes as daemons.
      dependence_on_chief: Whether to terminates the cluster if the chief exits.
        If auto_restart is True, it only terminates the cluster if the chief
        exits with a zero exit code.
      auto_restart: Whether to automatically restart processes that exit with
        non-zero exit code.
      share_gpu: Whether to share GPUs among workers. If False, each worker is
        assigned different GPUs in a roundrobin fashion. This should be True
        whenever possible for better test execution coverage; some situations
        that need it to be False are tests that runs NCCL.
      args: Positional arguments to be sent to `fn` run on subprocesses.
      kwargs: Keyword arguments to be sent to `fn` run on subprocesses.

    Raises:
      RuntimeError: if `multi_process_runner.test_main()` is not called.
      ValueError: if there are more than one chief in the `cluster_spec`.
      SkipTest: if thread sanitizer is enabled (which is incompatible with MPR).
    """
if test_util.is_tsan_enabled():
    raise unittest.SkipTest(
        'ThreadSanitizer is not compatible with MultiProcessRunner.')

assert cluster_spec is not None
if 'chief' in cluster_spec and len(cluster_spec['chief']) > 1:
    raise ValueError('If chief exists in the cluster, there must be at most '
                     'one chief. Current `cluster_spec` has {} chiefs.'
                     .format(len(cluster_spec['chief'])))
_check_initialization()
if not callable(fn):
    raise ValueError('fn is not a callable')

self._fn = fn
self._cluster_spec = cluster_spec
self._rpc_layer = rpc_layer or 'grpc'
self._max_run_time = max_run_time
self._grpc_fail_fast = grpc_fail_fast
self._stream_output = stream_output
# TODO(rchao): Revisit return_output argument to consider other solution.
self._return_output = return_output
self._dependence_on_chief = dependence_on_chief
self._use_dill_for_args = use_dill_for_args
self._daemon = daemon
self._auto_restart = auto_restart
self._args = args or ()
self._kwargs = kwargs or {}

self._share_gpu = share_gpu
self._total_gpu = len(context.context().list_physical_devices('GPU'))

# Child processes should have the same v2 and eager behavior.
self._v2_enabled = tf2.enabled()
self._executing_eagerly = context.executing_eagerly()

self._joined = False
self._process_lock = threading.Lock()
# Guarded by self._process_lock.
self._processes = {}
# Record which processes are terminated. Due to a bug in Python<3.7,
# terminated processes return 255 exit code, which should cause an exception
# in join().
# https://bugs.python.org/issue30589
# Guarded by self._process_lock.
self._terminated = set()
self._reading_threads = []

self._manager = manager()
self._process_status_queue = self._manager.Queue()
self._parent_to_sub_queue = self._manager.Queue()
parties = sum(len(addresses) for addresses in self._cluster_spec.values())
self._barrier = self._manager.Barrier(parties)

# We use a queue to collect outputs from worker processes since it's thread
# safe.
self._streaming_queue = self._manager.Queue()

self._watchdog_thread = None
