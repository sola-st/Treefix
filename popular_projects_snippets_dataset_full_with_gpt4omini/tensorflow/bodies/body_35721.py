# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/critical_section_test.py
# This would have caused a deadlock if not for logic in execute
# that inserts additional control dependencies onto the lock op:
#   * Loop body argument j is captured by fn()
#   * i is running in parallel to move forward the execution
#   * j is not being checked by the predicate function
#   * output of cs.execute() is returned as next j.
fn = lambda: j + 1
exit((i + 1, cs.execute(fn)))
