# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/combinations.py
if not in_main_process():
    raise ValueError(
        "combinations.env() should only be modified in the main process. "
        "Condition your code on combinations.in_main_process().")
super().__setattr__(name, value)
