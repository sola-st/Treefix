# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
"""Register a tab-completion context.

    Register that, for each word in context_words, the potential tab-completions
    are the words in comp_items.

    A context word is a pre-existing, completed word in the command line that
    determines how tab-completion works for another, incomplete word in the same
    command line.
    Completion items consist of potential candidates for the incomplete word.

    To give a general example, a context word can be "drink", and the completion
    items can be ["coffee", "tea", "water"]

    Note: A context word can be empty, in which case the context is for the
     top-level commands.

    Args:
      context_words: A list of context words belonging to the context being
        registered. It is a list of str, instead of a single string, to support
        synonym words triggering the same tab-completion context, e.g.,
        both "drink" and the short-hand "dr" can trigger the same context.
      comp_items: A list of completion items, as a list of str.

    Raises:
      TypeError: if the input arguments are not all of the correct types.
    """

if not isinstance(context_words, list):
    raise TypeError("Incorrect type in context_list: Expected list, got %s" %
                    type(context_words))

if not isinstance(comp_items, list):
    raise TypeError("Incorrect type in comp_items: Expected list, got %s" %
                    type(comp_items))

# Sort the completion items on registration, so that later during
# get_completions calls, no sorting will be necessary.
sorted_comp_items = sorted(comp_items)

for context_word in context_words:
    self._comp_dict[context_word] = sorted_comp_items
