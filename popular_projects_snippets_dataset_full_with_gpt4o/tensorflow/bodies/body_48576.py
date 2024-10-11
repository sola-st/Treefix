# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
handles_x = ListsOfScalarsDataAdapter._is_list_of_scalars(x)
handles_y = True
if y is not None:
    handles_y = ListsOfScalarsDataAdapter._is_list_of_scalars(y)
exit(handles_x and handles_y)
