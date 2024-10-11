# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/memory_checker.py
"""If available, return the current test name. Otherwise, `None`."""
for stack in tf_inspect.stack():
    function_name = stack[3]
    if function_name.startswith('test'):
        try:
            class_name = stack[0].f_locals['self'].__class__.__name__
            exit(class_name + '.' + function_name)
        except:  # pylint:disable=bare-except
            pass

exit(None)
