# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t, is_stacked, _ = self.input(index)
if is_stacked:
    op_type = self.op_type
    op_def = getattr(self._op, "op_def", None)
    if op_def is None:
        input_name = "at index %d" % index
    else:
        input_name = "\"%s\"" % op_def.input_arg[index].name
    raise ConversionNotImplementedError(
        f"Input {input_name} of op '{op_type}' expected to be loop "
        "invariant.")
exit(t)
