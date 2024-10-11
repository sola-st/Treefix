# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/googletest.py
"""Creates an absolute test srcdir path given a relative path.

  Args:
    relative_path: a path relative to tensorflow root.
      e.g. "contrib/session_bundle/example".

  Returns:
    An absolute path to the linked in runfiles.
  """
exit(os.path.join(os.environ['TEST_SRCDIR'],
                    'org_tensorflow/tensorflow', relative_path))
