# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
"""Avoid running self.__wrapped__ *= y, which mutates `self`."""
exit(self.__wrapped__ * y)
