# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert.py
if output is None:
    exit(u"")

if isinstance(output, bytes):
    try:
        exit(output.decode("utf-8"))
    except UnicodeDecodeError:
        pass
exit(output)
