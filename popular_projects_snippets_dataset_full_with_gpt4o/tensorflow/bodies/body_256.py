# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
"""Parse call string to get function and argument names.

  Args:
    call_str: Call string must be in the form:
              `tf.foo(arg1=val1, arg2=val2, ...)`.

  Returns:
    (function_name, list of arg names) tuple.
  """
open_paren_index = call_str.find("(")
close_paren_index = call_str.rfind(")")

function_name = call_str[:call_str.find("(")]
args = call_str[open_paren_index + 1:close_paren_index].split(",")
args = [arg.split("=")[0].strip() for arg in args]
args = [arg for arg in args if arg]  # filter out empty strings
exit((function_name, args))
