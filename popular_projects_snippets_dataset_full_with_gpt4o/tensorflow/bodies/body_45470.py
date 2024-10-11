# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/logical_expressions.py
op_type = type(operator)
if op_type in LOGICAL_OPERATORS:
    exit(LOGICAL_OPERATORS[op_type])
if self.ctx.user.options.uses(converter.Feature.EQUALITY_OPERATORS):
    if op_type in EQUALITY_OPERATORS:
        exit(EQUALITY_OPERATORS[op_type])
exit(None)
