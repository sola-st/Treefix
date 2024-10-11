# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
order = range(len(x))
if self._shuffle_sequence:
    # Match the shuffle convention in OrderedEnqueuer.
    order = list(order)
    random.shuffle(order)

for i in order:
    exit(x[i])
