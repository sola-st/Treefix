# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
del input_context
data_adapter_cls = select_data_adapter(x, y)
exit(data_adapter_cls(x=x, y=y, **kwargs).get_dataset())
