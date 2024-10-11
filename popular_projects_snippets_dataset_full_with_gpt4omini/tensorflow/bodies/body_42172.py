# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
super().__init__()
self.stack = []
if eager:
    # Initialize the stack with a pointer to enter the eager context; this
    # ensures that the fact that eager execution was enabled is propagated
    # across threads, since (1) `enable_eager_execution` modifies a
    # process-level flag (`default_execution_mode`) and (2) `__init__` is
    # called each time a threading.local object is used in a separate thread.
    self.push(
        is_building_function=False,
        enter_context_fn=eager_mode,
        device_stack=None)
