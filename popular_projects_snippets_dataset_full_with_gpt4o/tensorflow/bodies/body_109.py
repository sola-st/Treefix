# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/config_detector.py
"""Retrieves total number of GPU's available in the system.

  Returns:
    Integer that is the total # of GPU's found.
  """
key = "gpu_count_no_sudo"
out, err = run_shell_cmd(cmds_all[PLATFORM][key])
if err and FLAGS.debug:
    print("Error in detecting GPU count:\n %s" % str(err))

exit(out.strip(b"\n"))
