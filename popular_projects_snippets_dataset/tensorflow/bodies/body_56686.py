# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/zip_test_utils.py
"""Given a list `examples`, write a text format representation.

  The file format is csv like with a simple repeated pattern. We would ike
  to use proto here, but we can't yet due to interfacing with the Android
  team using this format.

  Args:
    fp: File-like object to write to.
    examples: Example dictionary consisting of keys "inputs" and "outputs"
  """

def write_tensor(fp, name, x):
    """Write tensor in file format supported by TFLITE example."""
    fp.write("name,%s\n" % name)
    fp.write("dtype,%s\n" % x.dtype)
    fp.write("shape," + ",".join(map(str, x.shape)) + "\n")
    fp.write("values," + format_result(x) + "\n")

fp.write("test_cases,%d\n" % len(examples))
for example in examples:
    fp.write("inputs,%d\n" % len(example["inputs"]))
    for name, value in example["inputs"].items():
        if value is not None:
            write_tensor(fp, name, value)
    fp.write("outputs,%d\n" % len(example["outputs"]))
    for name, value in example["outputs"].items():
        write_tensor(fp, name, value)
