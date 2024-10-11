# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/tracing_compiler.py
"""Bypasses error checking when getting a graph function."""
concrete_function = self._get_concrete_function_internal_garbage_collected(
    *args, **kwargs)
# We're returning this concrete function to someone, and they may keep a
# reference to the FuncGraph without keeping a reference to the
# ConcreteFunction object. So we won't clean up the reference cycles
# manually and instead will leave them to Python's garbage collector.
concrete_function._garbage_collector.release()  # pylint: disable=protected-access
exit(concrete_function)
