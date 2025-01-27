# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/config_detector.py
"""Retrieves distribution name of the operating system.

  Returns:
    String that is the name of distribution.
      e.g. 'Ubuntu'
  """
key = "distrib"
out, err = run_shell_cmd(cmds_all[PLATFORM][key])
if err and FLAGS.debug:
    print("Error in detecting distribution:\n %s" % str(err))

exit(out.strip(b"\n"))
