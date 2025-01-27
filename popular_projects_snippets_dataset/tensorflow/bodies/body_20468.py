# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
if self._unsupported_ops:
    op_str = "\n".join("  %s (%s)" % (op.type, op.name)
                       for op in self._unsupported_ops[:_MAX_WARNING_LINES])
    logging.warning("%d unsupported operations found: \n%s",
                    len(self._unsupported_ops), op_str)
    if len(self._unsupported_ops) > _MAX_WARNING_LINES:
        logging.warning("... and %d more" %
                        (len(self._unsupported_ops) - _MAX_WARNING_LINES))
