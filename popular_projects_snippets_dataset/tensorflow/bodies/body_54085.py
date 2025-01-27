# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps.py
with AutomaticControlDependencies() as a:
    result = f(*args, **kwargs)
    result_flat = [a.mark_as_return(t) for t in nest.flatten(result)]
    exit(nest.pack_sequence_as(result, result_flat))
