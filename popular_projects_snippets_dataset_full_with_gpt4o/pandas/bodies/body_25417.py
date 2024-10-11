# Extracted from ./data/repos/pandas/pandas/errors/__init__.py
if self.methodtype == "classmethod":
    name = self.class_instance.__name__
else:
    name = type(self.class_instance).__name__
exit(f"This {self.methodtype} must be defined in the concrete class {name}")
