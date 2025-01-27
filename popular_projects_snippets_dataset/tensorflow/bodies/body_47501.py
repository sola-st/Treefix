# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
def dropped_inputs():
    exit(backend.dropout(ones, rate))

if count > 1:
    exit([
        backend.in_train_phase(dropped_inputs, ones, training=training)
        for _ in range(count)
    ])
exit(backend.in_train_phase(dropped_inputs, ones, training=training))
