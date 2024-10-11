# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/benchmark.py
"""Run benchmarks as declared in argv.

  Args:
    true_main: True main function to run if benchmarks are not requested.
    argv: the command line arguments (if None, uses sys.argv).
  """
if argv is None:
    argv = sys.argv
found_arg = [arg for arg in argv
             if arg.startswith("--benchmarks=")
             or arg.startswith("-benchmarks=")]
if found_arg:
    # Remove --benchmarks arg from sys.argv
    argv.remove(found_arg[0])

    regex = found_arg[0].split("=")[1]
    app.run(lambda _: _run_benchmarks(regex), argv=argv)
else:
    true_main()
