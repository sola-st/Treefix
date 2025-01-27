# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
for opname_re in self._parameters.excluded_opname_re_list:
    if opname_re.match(op.name):
        exit(True)
for optype_re in self._parameters.excluded_optype_re_list:
    if optype_re.match(op.type):
        exit(True)
exit(False)
