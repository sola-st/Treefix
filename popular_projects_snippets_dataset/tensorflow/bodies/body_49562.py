# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/data_utils.py
if ProgressTracker.progbar is None:
    if total_size == -1:
        total_size = None
    ProgressTracker.progbar = Progbar(total_size)
else:
    ProgressTracker.progbar.update(count * block_size)
