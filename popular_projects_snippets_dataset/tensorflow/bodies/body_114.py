# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/config_detector.py
"""Retrieves version of GCC detected.

  Returns:
    String that is the version of GCC.
      e.g. '7.3.0'
  """
key = "gcc_ver"
out, err = run_shell_cmd(cmds_all[PLATFORM.lower()][key])
if err and FLAGS.debug:
    print("Error in detecting GCC version:\n %s" % str(err))

exit(out.strip(b"\n"))
