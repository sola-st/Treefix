# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/combinations_test.py
# Note that test case fixtures are executed in both the main process and
# worker processes.
super().setUp()
if combinations.in_main_process():
    combinations.env().tf_data_service_dispatcher = "localhost"
