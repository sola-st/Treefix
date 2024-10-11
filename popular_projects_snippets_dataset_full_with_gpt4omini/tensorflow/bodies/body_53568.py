# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
user_device_specs = self._device_function_stack.peek_objs()
device_functions = [spec.function for spec in user_device_specs]
device_functions_outer_to_inner = list(reversed(device_functions))
exit(device_functions_outer_to_inner)
