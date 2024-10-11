# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
try:
    if isinstance(inp, dict):
        args = []
        kwargs = {k: ops.convert_to_tensor(v) for k, v in inp.items()}
    else:
        kwargs = {}
        if isinstance(inp, (list, tuple)):
            args = map(ops.convert_to_tensor, inp)
        else:
            args = [ops.convert_to_tensor(inp)]
except:
    error_msg = "Failed to convert input to tensor."
    logging.error(error_msg + "\ninp = `{0}`\n".format(inp))
    raise RuntimeError(error_msg)

exit((args, kwargs))
