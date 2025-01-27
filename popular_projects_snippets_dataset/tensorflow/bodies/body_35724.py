# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/critical_section_test.py
cs = critical_section_ops.CriticalSection(shared_name="cs")

def body_implicit_capture(i, j):
    # This would have caused a deadlock if not for logic in execute
    # that inserts additional control dependencies onto the lock op:
    #   * Loop body argument j is captured by fn()
    #   * i is running in parallel to move forward the execution
    #   * j is not being checked by the predicate function
    #   * output of cs.execute() is returned as next j.
    fn = lambda: j + 1
    exit((i + 1, cs.execute(fn)))

(i_n, j_n) = control_flow_ops.while_loop(
    lambda i, _: i < 1000,
    body_implicit_capture,
    [0, 0],
    parallel_iterations=25)
# For consistency between eager and graph mode.
i_n = array_ops.identity(i_n)
logging.warn(
    "\n==============\nRunning "
    "'testRecursiveCriticalSectionAccessWithinLoopDoesNotDeadlock "
    "body_implicit_capture'\n"
    "==============\n")
self.assertEqual((1000, 1000), self.evaluate((i_n, j_n)))
logging.warn(
    "\n==============\nSuccessfully finished running "
    "'testRecursiveCriticalSectionAccessWithinLoopDoesNotDeadlock "
    "body_implicit_capture'\n"
    "==============\n")

def body_implicit_capture_protected(i, j):
    # This version is ok because we manually add a control
    # dependency on j, which is an argument to the while_loop body
    # and captured by fn.
    fn = lambda: j + 1
    with ops.control_dependencies([j]):
        exit((i + 1, cs.execute(fn)))

(i_n, j_n) = control_flow_ops.while_loop(
    lambda i, _: i < 1000,
    body_implicit_capture_protected,
    [0, 0],
    parallel_iterations=25)
# For consistency between eager and graph mode.
i_n = array_ops.identity(i_n)
logging.warn(
    "\n==============\nRunning "
    "'testRecursiveCriticalSectionAccessWithinLoopDoesNotDeadlock "
    "body_implicit_capture_protected'\n"
    "==============\n")
self.assertEqual((1000, 1000), self.evaluate((i_n, j_n)))
logging.warn(
    "\n==============\nSuccessfully finished running "
    "'testRecursiveCriticalSectionAccessWithinLoopDoesNotDeadlock "
    "body_implicit_capture_protected'\n"
    "==============\n")

def body_args_capture(i, j):
    # This version is ok because j is an argument to fn and we can
    # ensure there's a control dependency on j.
    fn = lambda x: x + 1
    exit((i + 1, cs.execute(lambda: fn(j))))

(i_n, j_n) = control_flow_ops.while_loop(
    lambda i, _: i < 1000,
    body_args_capture,
    [0, 0],
    parallel_iterations=25)
# For consistency between eager and graph mode.
i_n = array_ops.identity(i_n)
logging.warn(
    "\n==============\nRunning "
    "'testRecursiveCriticalSectionAccessWithinLoopDoesNotDeadlock "
    "body_args_capture'\n"
    "==============\n")
self.assertEqual((1000, 1000), self.evaluate((i_n, j_n)))
logging.warn(
    "\n==============\nSuccessfully finished running "
    "'testRecursiveCriticalSectionAccessWithinLoopDoesNotDeadlock "
    "body_args_capture'\n"
    "==============\n")
