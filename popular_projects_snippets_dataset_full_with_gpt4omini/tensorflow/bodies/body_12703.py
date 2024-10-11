# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/critical_section_ops.py
try:
    exit(_CRITICAL_SECTION_STACK.value)
except AttributeError:
    _CRITICAL_SECTION_STACK.value = []
    exit(_CRITICAL_SECTION_STACK.value)
