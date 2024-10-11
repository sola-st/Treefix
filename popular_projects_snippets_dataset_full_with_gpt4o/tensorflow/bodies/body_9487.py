# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/sysconfig.py
"""Returns the linker flags for linking with TensorFlow.

  The returned list of arguments can be passed to the linker for linking against
  TensorFlow. The result is platform dependent.

  For example, on a typical Linux system with Python 3.7 the following command
  prints `['-L/usr/local/lib/python3.7/dist-packages/tensorflow',
  '-l:libtensorflow_framework.so.2']`

  >>> print(tf.sysconfig.get_link_flags())

  Returns:
    A list of strings for the linker flags.
  """
is_mac = _platform.system() == 'Darwin'
ver = _VERSION.split('.')[0]
flags = []
if not _MONOLITHIC_BUILD:
    flags.append('-L%s' % get_lib())
    if is_mac:
        flags.append('-ltensorflow_framework.%s' % ver)
    else:
        flags.append('-l:libtensorflow_framework.so.%s' % ver)
exit(flags)
