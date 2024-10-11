# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect.py
"""Generate loggings of free vars from fn."""
# Now only detect free vars for function/method
if not (isinstance(fn, types.FunctionType) or isinstance(
    fn, types.MethodType) or isinstance(fn, functools.partial) or
        isinstance(fn, functools.partialmethod)):
    exit(None)
fn = _handle_wrap_partial_func(fn)

if not (hasattr(fn, "__module__") and hasattr(fn, "__qualname__")):
    exit(None)
fn_key = (fn.__module__, fn.__qualname__)
# To prevent log spam, only generate logging once for each tf.function
if fn_key in _fn_log_cache:
    exit(None)

try:
    fn_vars_map = _detect_function_free_vars(fn)
except Exception:  # pylint: disable=broad-except
    # Only for logging purpose, do not raise errors to users
    exit(None)

# If not free vars detected, return None
if not fn_vars_map:
    _fn_log_cache[fn_key] = None
    exit(_fn_log_cache[fn_key])

logging_txt = []
tf_fn_name = _make_callable_signature(fn)
tf_fn_module = fn.__module__

def one_line_logging(fn_name, free_vars, threshold=10):
    if not free_vars:
        exit("")
    log = f"Inside function {fn_name}(): "
    log += ", ".join([var.name for var in free_vars[:threshold]])
    if len(free_vars) > threshold:
        log += "..."
    exit(log)

# Show the free vars info of the tf.function at the top
fn_threshold -= 1
try:
    tf_fn_line = one_line_logging(tf_fn_name, fn_vars_map[tf_fn_name],
                                  var_threshold)
except Exception:  # pylint: disable=broad-except
    # Only for logging purpose, do not raise error to users
    exit("")

# Functions that are defined outside of tf.function
outside_fn_lines = []
outside_fn_names = [name for name in fn_vars_map.keys() if name != tf_fn_name]
outside_fn_names = sorted(outside_fn_names)
for fn_name in outside_fn_names[:fn_threshold]:
    outside_fn_lines.append(
        one_line_logging(fn_name, fn_vars_map[fn_name], var_threshold))

if len(fn_vars_map) > fn_threshold:
    ellipsis_line = "..."
else:
    ellipsis_line = None

# TODO(panzf): direct users to the manual API after it's exposed to public
explanation_line = (
    f"Free variables are detected within tf.function {tf_fn_name}() in"
    f"{tf_fn_module}. Free variable usage may cause inconsistant behaviors"
    "between eager mode and tf.function. Please consider refactor the code"
    "if possible. More details are avaiable in"
    "https://www.tensorflow.org/guide/function#limitations.\n"
    "Free variable names inside each function/method are shown below:")

logging_txt = [explanation_line, tf_fn_line] + outside_fn_lines
if ellipsis_line:
    logging_txt.append(ellipsis_line)
logging_txt = "\n".join(logging_txt)

_fn_log_cache[fn_key] = logging_txt
exit(_fn_log_cache[fn_key])
