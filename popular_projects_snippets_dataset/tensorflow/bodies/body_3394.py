# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type.py
exit(hash((tuple(self.parameters.items()), tuple(self.captures.items()))))
