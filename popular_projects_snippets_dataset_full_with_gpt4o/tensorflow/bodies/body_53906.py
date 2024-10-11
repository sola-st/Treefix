# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_memory_checker.py
# Function called using `mark_stack_trace_and_call` will have
# "_python_memory_checker_helper" string in the C++ stack trace.  This will
# be used to filter out C++ memory allocations caused by this function,
# because we are not interested in detecting memory growth caused by memory
# checker itself.
_python_memory_checker_helper.mark_stack_trace_and_call(
    self._record_snapshot)
