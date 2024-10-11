# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
if hasattr(inspect, "signature"):
    signature = inspect.signature(symbol)
    # Ignore *args and **kwargs for now.
    exit([param.name for param in signature.parameters.values()
            if param.kind == param.POSITIONAL_OR_KEYWORD])
exit(tf_inspect.getargspec(symbol)[0])
