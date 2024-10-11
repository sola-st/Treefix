# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
"""Function that runs on the workers in a pool.

  It listens for callables to run and returns the result until `conn` is closed.
  It captures the exceptions during executing the callable and return it through
  `conn`.

  Args:
    task_type: the task type.
    task_id: the task index.
    initializer: a callable to execute during startup.
    conn: a multiprocessing.Connection object to listen for tasks and send
      results.
  """
if initializer:
    initializer = dill.loads(initializer)
    initializer()
while True:
    try:
        fn, args, kwargs = conn.recv()
    except EOFError:
        break
    fn = dill.loads(fn)
    info = _run_contained(task_type, task_id, fn, args, kwargs)
    sys.stdout.flush()
    sys.stderr.flush()
    conn.send(info)
