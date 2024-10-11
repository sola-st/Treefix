# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
joiner = "\n\n" if verbose else "\n"
exit(joiner.join([
    c.pretty_printed_signature(verbose=verbose)
    for c in self._list_all_concrete_functions()
]))
