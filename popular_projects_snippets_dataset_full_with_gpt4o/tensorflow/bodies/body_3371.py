# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type.py
if optional and kind not in [
    self.POSITIONAL_ONLY, self.KEYWORD_ONLY, self.POSITIONAL_OR_KEYWORD
]:
    raise ValueError(
        "Parameter " + name +
        " is optional and its kind must be one of {POSITIONAL_ONLY, " +
        "KEYWORD_ONLY, POSITIONAL_OR_KEYWORD}. Got: " + str(kind))

if type_constraint and kind in [self.VAR_POSITIONAL, self.VAR_KEYWORD]:
    raise TypeError("Variable args/kwargs can not have type constraints.")

if not isinstance(type_constraint, (trace.TraceType, type(None))):
    raise TypeError(
        "Type constraints can only be an instance of a TraceType but got " +
        "type_constraint=" + str(type_constraint) + " for Parameter " + name)

super().__init__(
    name,
    kind,
    default=CAPTURED_DEFAULT_VALUE if optional else self.empty,
    annotation=type_constraint
    if type_constraint is not None else self.empty)
