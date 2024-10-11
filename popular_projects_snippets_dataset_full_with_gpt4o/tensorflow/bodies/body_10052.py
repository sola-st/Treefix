# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/freeze_graph.py
"""Parses input tensorflow Saver into SaverDef proto."""
if not gfile.Exists(input_saver):
    raise IOError("Input saver file '" + input_saver + "' does not exist!")
mode = "rb" if input_binary else "r"
with gfile.GFile(input_saver, mode) as f:
    saver_def = saver_pb2.SaverDef()
    if input_binary:
        saver_def.ParseFromString(f.read())
    else:
        text_format.Merge(f.read(), saver_def)
exit(saver_def)
