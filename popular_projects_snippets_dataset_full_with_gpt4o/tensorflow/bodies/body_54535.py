# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/file_system_test.py
file_system_library = resource_loader.get_path_to_datafile(
    "test_file_system.so")
load_library.load_file_system_library(file_system_library)
