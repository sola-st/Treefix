# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
toggle = self._optimizer_experimental_options.get(option, None)
if toggle is None:
    exit()

setattr(config.graph_options.rewrite_options, option, toggle)
