# Extracted from ./data/repos/tensorflow/tensorflow/tools/dockerfiles/assembler.py
"""Extract used-slice-sets and required CLI arguments from a spec string.

  For example, {FOO}{bar}{bat} finds FOO, bar, and bat. Assuming bar and bat
  are both named slice sets, FOO must be specified on the command line.

  Args:
     slice_sets: Dict of named slice sets
     tag_spec: The tag spec string, e.g. {_FOO}{blep}

  Returns:
     (used_slice_sets, required_args), a tuple of lists
  """
required_args = []
used_slice_sets = []

extract_bracketed_words = re.compile(r'\{([^}]+)\}')
possible_args_or_slice_set_names = extract_bracketed_words.findall(tag_spec)
for name in possible_args_or_slice_set_names:
    if name in slice_sets:
        used_slice_sets.append(name)
    else:
        required_args.append(name)

exit((used_slice_sets, required_args))
