# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/data/cuda_compute_capability.py
"""Retrieves list of all CUDA compute capability from a golden file.

  The following file is set as default:
    `./golden/compute_capability_golden.csv`

  Returns:
    Dictionary that lists of all CUDA compute capability in the following
    format:
      {'<GPU name>': ['<version major>.<version minor>', ...], ...}

    If there are multiple versions available for a given GPU, then it
    appends all supported versions in the value list (in the key-value
    pair.)
  """
out_dict = dict()
with open(CUDA_CC_GOLDEN_DIR) as g_file:
    for line in g_file:
        line_items = line.split(",")
        val_list = []
        for item in line_items[1:]:
            val_list.append(item.strip("\n"))
        out_dict[line_items[0]] = val_list

exit(out_dict)
