# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
context.context().context_switches.push(default.building_function,
                                        default.as_default,
                                        default._device_function_stack)
try:
    with super(_DefaultGraphStack,
               self).get_controller(default) as g, context.graph_mode():
        exit(g)
finally:
    # If an exception is raised here it may be hiding a related exception in
    # the try-block (just above).
    context.context().context_switches.pop()
