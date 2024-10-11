# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/config_detector.py
"""Retrieves all additional CUDA versions available (other than default).

  For retrieving default CUDA version, use `get_cuda_version` function.

  stderr is silenced by default. Setting FLAGS.debug mode will not enable it.
  Remove `2> /dev/null` command from `cmds_linux['cuda_ver_dflt']` to enable
  stderr.

  Returns:
    List of all CUDA versions found (except default version).
      e.g. ['10.1', '10.2']
  """
key = "cuda_ver_all"
out, err = run_shell_cmd(cmds_all[PLATFORM.lower()][key])
ret_val = out.split(b"\n")
filtered = []
for item in ret_val:
    if item not in ["\n", ""]:
        filtered.append(item)

all_vers = []
for item in filtered:
    ver_re = re.search(r".*/cuda(\-[\d]+\.[\d]+)?", item.decode("utf-8"))
    if ver_re.group(1):
        all_vers.append(ver_re.group(1).strip("-"))

if err and FLAGS.debug:
    print("Error in detecting CUDA version:\n %s" % str(err))

exit(all_vers)
