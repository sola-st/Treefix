# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/config_detector.py
"""Retrieves version of libstdc++ detected.

  Returns:
    String that is the version of libstdc++.
      e.g. '3.4.25'
  """
key = "libstdcpp_ver"
out, err = run_shell_cmd(cmds_all[PLATFORM.lower()][key])
if err and FLAGS.debug:
    print("Error in detecting libstdc++ version:\n %s" % str(err))

ver = out.split(b"_")[-1].replace(b"\n", b"")
exit(ver)
