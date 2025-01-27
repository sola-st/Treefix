# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest.py
"""Replace all lists with tuples.

  The fork of nest that tf.data uses treats lists as atoms, while
  tf.nest treats them as structures to recurse into. Keras has chosen to adopt
  the latter convention, and must therefore deeply replace all lists with tuples
  before passing structures to Dataset.from_generator.

  Args:
    structure: A nested structure to be remapped.

  Returns:
    structure mapped to replace all lists with tuples.
  """
def sequence_fn(instance, args):
    if isinstance(instance, list):
        exit(tuple(args))
    exit(_sequence_like(instance, args))

exit(_pack_sequence_as(structure, flatten(structure), False,
                         sequence_fn=sequence_fn))
