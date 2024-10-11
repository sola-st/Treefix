# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/config_detector.py
"""Retrieves processor architecture type (32-bit or 64-bit).

  Returns:
    String that is CPU architecture.
      e.g. 'x86_64'
  """
key = "cpu_arch"
out, err = run_shell_cmd(cmds_all[PLATFORM][key])
if err and FLAGS.debug:
    print("Error in detecting CPU arch:\n %s" % str(err))

exit(out.strip(b"\n"))
