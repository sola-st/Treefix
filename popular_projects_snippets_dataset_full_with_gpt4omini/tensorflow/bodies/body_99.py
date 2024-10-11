# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/data/cuda_compute_capability.py
"""Checks the newly created CUDA compute capability file with the golden.

  If differences are found, then it prints a list of all mismatches as
  a `WARNING`.

  Golden file must reside in `golden/` directory.

  Args:
    filename: String that is the name of the newly created file.
  """
path_to_file = PATH_TO_DIR + "/data/" + filename
if os.path.isfile(path_to_file) and os.path.isfile(CUDA_CC_GOLDEN_DIR):
    with open(path_to_file, "r") as f_new:
        with open(CUDA_CC_GOLDEN_DIR, "r") as f_golden:
            diff = difflib.unified_diff(
                f_new.readlines(),
                f_golden.readlines(),
                fromfile=path_to_file,
                tofile=CUDA_CC_GOLDEN_DIR
            )
            diff_list = []
            for line in diff:
                diff_list.append(line)

            if diff_list:
                print("WARNING: difference(s) found between new csv and golden csv.")
                print(diff_list)
            else:
                print("No difference found between new csv and golen csv.")
