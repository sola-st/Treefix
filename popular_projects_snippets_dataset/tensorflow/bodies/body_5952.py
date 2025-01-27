# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/combinations_test.py
self.assertLen(context.context().list_physical_devices("GPU"),
               combinations.env().total_phsyical_gpus)
