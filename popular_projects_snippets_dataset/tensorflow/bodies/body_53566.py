# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Make device, colocation and dependencies stacks thread-local.

    Device, colocation and dependencies stacks are not thread-local be default.
    If multiple threads access them, then the state is shared.  This means that
    one thread may affect the behavior of another thread.

    After this method is called, the stacks become thread-local.  If multiple
    threads access them, then the state is not shared.  Each thread uses its own
    value; a thread doesn't affect other threads by mutating such a stack.

    The initial value for every thread's stack is set to the current value
    of the stack when `switch_to_thread_local()` was first called.
    """
if not self._stack_state_is_thread_local:
    self._stack_state_is_thread_local = True
