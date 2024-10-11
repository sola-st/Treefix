# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
"""The wrapper function that actually gets run in child process(es)."""

global _barrier

self._resources = resources
_barrier = self._resources.barrier
fn = dill.loads(fn)
if use_dill_for_args:
    args = dill.loads(args)
    kwargs = dill.loads(kwargs)

if faulthandler is not None:
    faulthandler.enable()
    faulthandler.register(signal.SIGTERM, chain=True)

# All logging should go to stderr to be streamed to the main process.
logging.set_stderrthreshold(logging.DEBUG)

# Assign sys.stdout and sys.stderr as duplicates of `streaming_pipe_w` so
# print() and logging.*() write directly to `streaming_pipe_w`.
# Unfortunately since we cannot prepend task_type and task_id information to
# the streamed logs we will need a thread per subprocess to distinguish
# where the piece of message is from.
os.dup2(resources.streaming_pipe_w.fileno(), sys.stdout.fileno())
os.dup2(resources.streaming_pipe_w.fileno(), sys.stderr.fileno())

pid = os.getpid()
logging.info('Subprocess with PID %d (%s, %d) is now being started.', pid,
             test_env.task_type, test_env.task_id)
logging.info('TF_CONFIG: %r', os.environ['TF_CONFIG'])

# The thread will be dedicated to checking messages from the parent process.
threading.Thread(  # pylint: disable=unexpected-keyword-arg
    target=self._message_checking_func,
    args=(test_env.task_type, test_env.task_id),
    daemon=True).start()

if test_env.v2_enabled:
    v2_compat.enable_v2_behavior()

with self._runtime_mode(test_env.executing_eagerly):
    info = _run_contained(test_env.task_type, test_env.task_id, fn, args,
                          kwargs)
    self._resources.process_status_queue.put(info)

    # Re-raise the exception in addition to reporting it to the parent
    # process, so that even if `--test_timeout` flag is set and the
    # error doesn't make it to be shown in parent process before bazel's
    # timeout, the log would still show what happens in this subprocess,
    # instead of silently suppressing the error due to early bazel
    # timeout. Raising an error in the subprocess produces stack trace in
    # the log, but the program continues running.
    if not info.is_successful:
        six.reraise(*info.exc_info)

    self._close_streaming()

# Exit with code 0 as it's considered successful exit at this point.
sys.exit(0)
