# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_generator_v1.py
model._validate_or_infer_batch_size(batch_size, steps, x)
exit(predict_generator(
    model,
    x,
    steps=steps,
    verbose=verbose,
    callbacks=callbacks,
    max_queue_size=max_queue_size,
    workers=workers,
    use_multiprocessing=use_multiprocessing))
