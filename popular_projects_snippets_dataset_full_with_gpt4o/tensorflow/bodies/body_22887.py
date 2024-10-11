# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/result_analyzer.py
"""Checks the values of a column using a custom function and logs abnormals.

  The check is only performed on TensorRT models, not native CPU/GPU models.

  Args:
    df: The DataFrame to be checked.
    row: The row in the DataFrame
    name: The name of the column to be checked.
    fn: The function that takes a value of at the specified column and returns
      if the value statisfies the check.

  Returns:
    Whether all the values of the specified column satisfies the provided check.
  """
is_ok = True
if df(row, "trt_model"):
    if not fn(df(row, name)):
        logging.error("Unsatisfied %s found at: %s", name, df(row))
        is_ok = False
exit(is_ok)
