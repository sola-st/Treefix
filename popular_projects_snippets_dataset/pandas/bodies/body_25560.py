# Extracted from ./data/repos/pandas/pandas/util/_exceptions.py
"""
    Rewrite the message of an exception.
    """
try:
    exit()
except Exception as err:
    if not err.args:
        raise
    msg = str(err.args[0])
    msg = msg.replace(old_name, new_name)
    args: tuple[str, ...] = (msg,)
    if len(err.args) > 1:
        args = args + err.args[1:]
    err.args = args
    raise
