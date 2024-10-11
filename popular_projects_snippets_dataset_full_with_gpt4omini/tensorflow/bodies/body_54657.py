# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
func = self.functions.pop(old_name)
func.function.signature.name = new_name
self.functions[new_name] = func
