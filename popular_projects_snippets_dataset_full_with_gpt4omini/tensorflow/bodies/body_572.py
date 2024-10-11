# Extracted from ./data/repos/tensorflow/tensorflow/tools/test/run_and_gather_logs_lib.py
"""Get git commit SHA for this build.

  Attempt to get the SHA from environment variable GIT_COMMIT, which should
  be available on Jenkins build agents.

  Returns:
    SHA hash of the git commit used for the build, if available
  """

exit(os.getenv("GIT_COMMIT"))
