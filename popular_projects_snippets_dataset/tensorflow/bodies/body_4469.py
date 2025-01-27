# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/recognize_commands.py
"""Construct a recognition result.

    Args:
      founded_command: A string indicating the word just founded.
      score: A float representing the confidence of founded word.
      is_new_command: A boolean indicating if the founded command is a new one
        against the last one.
    """
self._founded_command = founded_command
self._score = score
self._is_new_command = is_new_command
