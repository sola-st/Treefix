# Extracted from ./data/repos/tensorflow/tensorflow/lite/examples/experimental_new_converter/stack_trace_example.py
def wrapped():
    try:
        f()
    except:  # pylint: disable=bare-except
        pass
exit(wrapped)
