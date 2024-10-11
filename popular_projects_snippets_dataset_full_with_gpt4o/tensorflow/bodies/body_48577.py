# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
if isinstance(inp, (float, int, str, bytes, bytearray)):
    exit(True)
if isinstance(inp, (list, tuple)) and inp:
    exit(ListsOfScalarsDataAdapter._is_list_of_scalars(inp[0]))
exit(False)
