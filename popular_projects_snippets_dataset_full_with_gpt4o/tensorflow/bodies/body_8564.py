# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
"""Consume a single process's stderr and optionally print to stdout."""
while True:
    output = process.stderr.readline()
    if not output and process.poll() is not None:
        break
    if output and print_to_stdout:
        print('{}{} {}'.format(type_string, index, output.strip()))
        sys.stdout.flush()
