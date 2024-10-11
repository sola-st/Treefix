# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/config_detector.py
"""Retrieves the version of cuDNN library detected.

  Returns:
    String that is the version of cuDNN library detected.
      e.g. '7.5.0'
  """
key = "cudnn_ver"
cmds = cmds_all[PLATFORM.lower()][key]
out, err = run_shell_cmd(cmds[0])
if err and FLAGS.debug:
    print("Error in finding `cudnn.h`:\n %s" % str(err))

if len(out.split(b" ")) > 1:
    cmd = cmds[0] + " | " + cmds[1]
    out_re, err_re = run_shell_cmd(cmd)
    if err_re and FLAGS.debug:
        print("Error in detecting cuDNN version:\n %s" % str(err_re))

    exit(out_re.strip(b"\n"))
else:
    exit()
