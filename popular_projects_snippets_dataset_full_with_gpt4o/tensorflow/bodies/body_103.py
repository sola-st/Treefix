# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/config_detector.py
"""Retrieves platform information.

  Currently the script only support linux. If other platoforms such as Windows
  or MacOS is detected, it throws an error and terminates.

  Returns:
    String that is platform type.
      e.g. 'linux'
  """
global PLATFORM
cmd = "uname"
out, err = run_shell_cmd(cmd)
platform_detected = out.strip().lower()
if platform_detected != "linux":
    if err and FLAGS.debug:
        print("Error in detecting platform:\n %s" % str(err))

    print("Error: Detected unsupported operating system.\nStopping...")
    sys.exit(1)
else:
    PLATFORM = platform_detected

exit(PLATFORM)
