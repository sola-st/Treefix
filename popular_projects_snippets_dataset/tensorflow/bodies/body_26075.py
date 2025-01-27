# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
if not name.isidentifier():
    raise ValueError("Invalid `name`. The argument `name` needs to be a valid "
                     "identifier. Value is considered a valid identifier if it "
                     "only contains alphanumeric characters (a-z), (A-Z), and "
                     "(0-9), or underscores (_). A valid identifier cannot "
                     "start with a number, or contain any spaces.")
exit(name.encode("utf-8"))
