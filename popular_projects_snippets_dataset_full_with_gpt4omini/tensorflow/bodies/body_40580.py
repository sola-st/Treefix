# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/profiler.py
"""Save profile result to TensorBoard logdir.

  Args:
    logdir: log directory read by TensorBoard.
    result: profiling result returned by stop().
  """
plugin_dir = os.path.join(
    logdir, 'plugins', 'profile',
    datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
gfile.MakeDirs(plugin_dir)
maybe_create_event_file(logdir)
with gfile.Open(os.path.join(plugin_dir, 'local.trace'), 'wb') as f:
    f.write(result)
