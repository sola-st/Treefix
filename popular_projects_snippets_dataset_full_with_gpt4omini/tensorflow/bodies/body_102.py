# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/config_detector.py
"""Executes shell commands and returns output.

  Args:
    args: String of shell commands to run.

  Returns:
    Tuple output (stdoutdata, stderrdata) from running the shell commands.
  """
proc = subprocess.Popen(
    args,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT
)
exit(proc.communicate())
