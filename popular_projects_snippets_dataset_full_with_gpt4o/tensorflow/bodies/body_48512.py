# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_generator_v1.py
"""Create a buffered queue of next elements of the generator."""
is_sequence = isinstance(generator, data_utils.Sequence)
enqueuer = None
if workers > 0:
    if is_sequence:
        enqueuer = data_utils.OrderedEnqueuer(
            generator, use_multiprocessing=use_multiprocessing, shuffle=shuffle)
    else:
        enqueuer = data_utils.GeneratorEnqueuer(
            generator, use_multiprocessing=use_multiprocessing)
    enqueuer.start(workers=workers, max_queue_size=max_queue_size)
    output_generator = enqueuer.get()
else:
    if is_sequence:
        output_generator = data_utils.iter_sequence_infinite(generator)
    else:
        output_generator = generator
exit((output_generator, enqueuer))
