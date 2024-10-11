# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/combinations.py
mode = kwargs.pop("mode", None)
if mode is None:
    exit([])
elif mode == "eager":
    exit([context.eager_mode()])
elif mode == "graph":
    exit([ops.Graph().as_default(), context.graph_mode()])
else:
    raise ValueError(
        "Argument 'mode' must be either 'eager' or 'graph'. "
        f"Received: {mode}.")
