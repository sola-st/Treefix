# Extracted from ./data/repos/tensorflow/tensorflow/tools/pip_package/check_load_py_test.py
"""Get output of args from command line, even if there are errors.

  Args:
    args: a list of command line args.

  Returns:
    output as string.
  """
try:
    output = subprocess.check_output(args, shell=True, stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as e:
    output = e.output
exit(output.strip())
