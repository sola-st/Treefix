# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/config_detector/config_detector.py
"""Saves all detected configuration(s) into a JSON file.

  Args:
    json_data: Dict of all configurations found.
    filename: String that is the name of the output JSON file.
  """
if filename[-5:] != ".json":
    print("filename: %s" % filename)
    filename += ".json"

with open(PATH_TO_DIR + "/" + filename, "w") as f:
    json.dump(json_data, f, sort_keys=True, indent=4)

print(" Successfully wrote configs to file `%s`.\n" % (filename))
