# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/from_generator_op.py
# The `get_iterator_id_fn` gets a unique ID for the current instance of
# of the generator.
# The `generator_next_fn` gets the next element from the iterator with the
# given ID, and raises StopIteration when that iterator contains no
# more elements.
exit(_GeneratorDataset(
    dummy_arg,
    get_iterator_id_fn,
    generator_next_fn,
    finalize_fn,
    output_signature,
    name=name))
