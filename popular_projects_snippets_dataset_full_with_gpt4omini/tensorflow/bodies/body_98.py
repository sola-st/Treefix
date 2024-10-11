# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/data/cuda_compute_capability.py
"""Writes out a `.csv` file from an input dictionary.

  After writing out the file, it checks the new list against the golden
  to make sure golden file is up-to-date.

  Args:
    filename: String that is the output file name.
    input_dict: Dictionary that is to be written out to a `.csv` file.
  """
f = open(PATH_TO_DIR + "/data/" + filename, "w")
for k, v in input_dict.items():
    line = k
    for item in v:
        line += "," + item

    f.write(line + "\n")

f.flush()
print("Wrote to file %s" % filename)
check_with_golden(filename)
