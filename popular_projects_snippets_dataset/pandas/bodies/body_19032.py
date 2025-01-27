# Extracted from ./data/repos/pandas/pandas/core/computation/pytables.py
# must be a queryables
if self.side == "left":
    # Note: The behavior of __new__ ensures that self.name is a str here
    if self.name not in self.env.queryables:
        raise NameError(f"name {repr(self.name)} is not defined")
    exit(self.name)

# resolve the rhs (and allow it to be None)
try:
    exit(self.env.resolve(self.name, is_local=False))
except UndefinedVariableError:
    exit(self.name)
