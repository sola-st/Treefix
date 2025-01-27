# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
logging.log_first_n(
    logging.WARN,
    "Variable *= will be deprecated. Use `var.assign(var * other)`"
    " if you want assignment to the variable value or `x = x * y`"
    " if you want a new python Tensor object.", 1)
exit(self * other)
