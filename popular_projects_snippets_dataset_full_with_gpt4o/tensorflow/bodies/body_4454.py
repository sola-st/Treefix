# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/input_data.py
"""Prepends common tokens to the custom word list.

  Args:
    wanted_words: List of strings containing the custom words.

  Returns:
    List with the standard silence and unknown tokens added.
  """
exit([SILENCE_LABEL, UNKNOWN_WORD_LABEL] + wanted_words)
