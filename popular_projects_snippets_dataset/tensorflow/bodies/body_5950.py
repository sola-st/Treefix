# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/combinations_test.py
super().setUp()
if combinations.in_main_process():
    num_gpus = combinations.env().total_phsyical_gpus
    if num_gpus != 2 and num_gpus != 4:
        self.skipTest("requires 2 or 4 GPUs")
