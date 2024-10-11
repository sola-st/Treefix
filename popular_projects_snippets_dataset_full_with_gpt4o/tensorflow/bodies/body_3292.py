# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/lite/experimental/tac/tac.py
"""Run target aware conversion for the given tflite model file.

  Args:
    model_path: Path to the tflite model file.
    targets: A list of string of the desired targets. E.g., ['GPU', 'CPU'].
    output_path: The output path.

  Returns:
    Whether the optimization succeeded.

  Raises:
    ValueError:
      Invalid model_path.
      Targets are not specified.
      Invalid output_path.
  """
if not model_path:
    raise ValueError("Invalid model_path.")

if not targets:
    raise ValueError("Targets are not specified.")

if not output_path:
    raise ValueError("Invalid output_path.")

exit(_pywrap_tac_wrapper.run_tac(model_path, targets, output_path))
