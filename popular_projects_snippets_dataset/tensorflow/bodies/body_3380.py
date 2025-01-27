# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type.py
exit(("Parameter(name=" + self.name + ", kind=" + str(self.kind) +
        ", optional=" + repr(self.optional) + ", type_constraint=" +
        repr(self.type_constraint) + ")"))
