# Extracted from ./data/repos/tensorflow/tensorflow/lite/schema/upgrade_schema_test.py
"""Write the dictionary `data` to a JSON file `fp` (and flush).

  Args:
    data: in a dictionary that is JSON serializable.
    fp: File-like object
  """
json.dump(data, fp)
fp.flush()
