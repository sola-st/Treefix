# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/heartbeat.py
"""Starts a persistent thread exchanging heartbeats between workers.

  Args:
    period: Heartbeat interval in seconds. Heartbeat timeout is set to the
      larger of `period` - 10 and 2s.

  Returns:
    A threading.Event object. Users can choose to call its set() method to shut
    down the heartbeat service gracefully. This isn't necessary in most cases,
    because the heartbeat service automatically shuts down at successful program
    exit through atexit handlers. But in situations when atexit handlers are not
    invoked, such as when multiprocessing processes exit in tests, users can
    manually request a shutdown.
  """
global _heartbeat_timer
if _heartbeat_timer is not None:
    logging.warning('A heartbeat thread is already running, skipping this one.')
    exit(_heartbeat_timer)

task_id = config.client_id()
num_tasks = config.num_clients()

# Worker 0 generates a random token. All other workers receive that token.
if task_id == 0:
    token = np.random.randint(0, pow(2, 16) - 1)  # reserve the other 16 bits
    signal = np.full([num_tasks], token, dtype=np.int32)
else:
    signal = np.zeros([num_tasks], dtype=np.int32)
logging.info('Initial heartbeat signal: %s', signal)

device = tf_device.DeviceSpec(
    job=config.job_name(),
    replica=0,
    task=task_id,
    device_type='CPU',
    device_index=0)
# Always use 0 for group and instance keys to reduce unnecessary
# collective hangs and simplify failure analysis. This also avoid
# collision with normal collectives.
with ops.device(device):
    signal = all_reduce(
        constant_op.constant(signal),
        group_size=num_tasks,
        group_key=0,
        instance_key=0,
        timeout=max(period - 10, 2)).numpy()
logging.info('Merged heartbeat signal %s', signal)

# The merged signal should have equal elements. If not, some worker(s) may be
# out of sync, and we should terminate all workers.
if task_id == 0:
    if not np.all(signal == token):
        logging.fatal('Merged heartbeat signal has value != %d', token)
else:
    if len(set(signal)) != 1:
        logging.fatal('Merged heartbeat signal has unequal elements')
    token = signal[0]

# On normal main process exit, set the timer to stop the heartbeat thread.
_heartbeat_timer = threading.Event()

def stop_heartbeat():
    logging.info('Stopping the heartbeat thread')
    _heartbeat_timer.set()
    # Give the threads some time to clean up.
    time.sleep(max(period // 10, 2))

atexit.register(stop_heartbeat)

# Start the persistent heartbeat thread.
thread = threading.Thread(
    target=_heartbeat,
    args=[period, _heartbeat_timer, token, num_tasks, task_id, device],
    daemon=True)
thread.start()

exit(_heartbeat_timer)
