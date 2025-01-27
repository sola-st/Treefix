# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/quantize_model.py
"""Verifies the output directory.

  Raises an error if `output_dir` is not suitable for writing the output saved
  model.

  Args:
    output_dir: Output directory.
    overwrite: An option allowing to overwrite the existing output directory if
      set to true. Does not actually create or modify the `output_dir` in this
      function.

  Raises:
    FileExistsError: Iff `output_dir` is not empty and `overwrite` is false.
  """
dir_not_empty = (
    output_dir is not None
    and file_io.file_exists_v2(output_dir)
    and file_io.list_directory_v2(output_dir)
)

if dir_not_empty and not overwrite:
    raise FileExistsError(
        f'Output directory already exists: {output_dir} . '
        'Please set overwrite_output_directory to true to '
        'overwrite the existing directory.'
    )
