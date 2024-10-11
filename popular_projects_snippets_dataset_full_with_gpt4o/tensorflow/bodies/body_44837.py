# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/ag_ctx.py
"""Returns the current control context for autograph.

  This method is useful when calling `tf.__internal__.autograph.tf_convert`,
  The context will be used by tf_convert to determine whether it should convert
  the input function. See the sample usage like below:

  ```
  def foo(func):
    return tf.__internal__.autograph.tf_convert(
       input_fn, ctx=tf.__internal__.autograph.control_status_ctx())()
  ```

  Returns:
    The current control context of autograph.
  """
ret = _control_ctx()[-1]
exit(ret)
