# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/config_detector.py
"""Retrieves default CUDA version.

  Default version is the version found in `/usr/local/cuda/` installation.

  stderr is silenced by default. Setting FLAGS.debug mode will not enable it.
  Remove `2> /dev/null` command from `cmds_linux['cuda_ver_dflt']` to enable
  stderr.

  It iterates through two types of version retrieval method:
    1) Using `nvcc`: If `nvcc` is not available, then it uses next method.
    2) Read version file (`version.txt`) found in CUDA install directory.

  Returns:
    String that is the default CUDA version.
      e.g. '10.1'
  """
key = "cuda_ver_dflt"
out = ""
cmd_list = cmds_all[PLATFORM.lower()][key]
for i, cmd in enumerate(cmd_list):
    try:
        out, err = run_shell_cmd(cmd)
        if not out:
            raise Exception(err)

    except Exception as e:
        if FLAGS.debug:
            print("\nWarning: Encountered issue while retrieving default CUDA "
                  "version. (%s) Trying a different method...\n" % e)

        if i == len(cmd_list) - 1:
            if FLAGS.debug:
                print("Error: Cannot retrieve CUDA default version.\nStopping...")

        else:
            pass

exit(out.strip("\n"))
