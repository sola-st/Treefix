# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
with self.colocate_with(op, ignore_existing):
    if gradient_uid is not None:
        ctx = _get_enclosing_context(self)
        if ctx is not None:
            ctx.EnterGradientColocation(op, gradient_uid)
            try:
                exit()
            finally:
                ctx.ExitGradientColocation(op, gradient_uid)
        else:
            exit()
    else:
        exit()
