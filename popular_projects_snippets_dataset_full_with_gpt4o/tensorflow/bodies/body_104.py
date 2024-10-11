# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/config_detector.py
"""Retrieves CPU (type) information.

  Returns:
    String that is name of the CPU.
      e.g. 'GenuineIntel'
  """
key = "cpu_type"
out, err = run_shell_cmd(cmds_all[PLATFORM][key])
cpu_detected = out.split(b":")[1].strip()
if err and FLAGS.debug:
    print("Error in detecting CPU type:\n %s" % str(err))

exit(cpu_detected)
