# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
"""Constructor of the for-test subclass.

    Args:
      command_sequence: (list of list of str) A list of command arguments,
        including the command prefix, each element of the list is such as:
        ["run", "-n"],
        ["print_feed", "input:0"].
      sess: See the doc string of LocalCLIDebugWrapperSession.__init__.
      dump_root: See the doc string of LocalCLIDebugWrapperSession.__init__.
    """

local_cli_wrapper.LocalCLIDebugWrapperSession.__init__(
    self, sess, dump_root=dump_root, log_usage=False)

self._command_sequence = command_sequence
self._command_pointer = 0

# Observer variables.
self.observers = {
    "debug_dumps": [],
    "tf_errors": [],
    "run_start_cli_run_numbers": [],
    "run_end_cli_run_numbers": [],
    "print_feed_responses": [],
    "profiler_py_graphs": [],
    "profiler_run_metadata": [],
}
