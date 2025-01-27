# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/config_detector.py
"""Retrieves distribution version of the operating system.

  Returns:
    String that is the distribution version.
      e.g. '14.04'
  """
key = "distrib_ver"
out, err = run_shell_cmd(cmds_all[PLATFORM][key])
if err and FLAGS.debug:
    print(
        "Error in detecting distribution version:\n %s" % str(err)
    )

exit(out.strip(b"\n"))
