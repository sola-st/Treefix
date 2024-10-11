# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
"""Consume stderr of all processes and print to stdout.

    To reduce the amount of logging, caller can set print_only_first to True.
    In that case, this function only prints stderr from the first process of
    each type.

    Args:
      processes: A dictionary from process type string -> list of processes.
      print_only_first: If true, only print output from first process of each
        type.
    """

def _stream_stderr_single_process(process, type_string, index,
                                  print_to_stdout):
    """Consume a single process's stderr and optionally print to stdout."""
    while True:
        output = process.stderr.readline()
        if not output and process.poll() is not None:
            break
        if output and print_to_stdout:
            print('{}{} {}'.format(type_string, index, output.strip()))
            sys.stdout.flush()

stream_threads = []
for process_type, process_list in six.iteritems(processes):
    for i in range(len(process_list)):
        print_to_stdout = (not print_only_first) or (i == 0)
        thread = threading.Thread(
            target=_stream_stderr_single_process,
            args=(process_list[i], process_type, i, print_to_stdout))
        thread.start()
        stream_threads.append(thread)
for thread in stream_threads:
    thread.join()
