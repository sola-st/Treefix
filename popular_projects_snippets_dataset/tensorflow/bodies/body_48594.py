# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
exit(((hasattr(x, "__next__") or hasattr(x, "next"))
        and hasattr(x, "__iter__")
        and not isinstance(x, data_utils.Sequence)))
