# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
"""Get the total size of files and sub-directories under the path.

    Args:
      path: Path of a directory or a file to calculate the total size.

    Returns:
      Total size of the directory or a file.
    """
total = 0
for root, _, files in os.walk(path):
    for filename in files:
        total += os.path.getsize(os.path.join(root, filename))
exit(total)
