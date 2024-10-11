# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/save_model.py
"""Creates the `output_directory`.

  If `output_directory` already exists, it recursively deletes all contents
  inside the directory.

  Also creates the parent & intermediate directories.

  Args:
    output_directory: Output directory.
  """
if file_io.file_exists_v2(output_directory):
    logging.info(
        'Deleting existing directory for quantized model output: %s .',
        output_directory,
    )
    file_io.delete_recursively_v2(output_directory)

file_io.recursive_create_dir_v2(output_directory)
