# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
"""Close stdout, stderr and streaming pipe.

    We need to explicitly close them since Tensorflow may take a while to exit,
    so that the reading threads in the main process can exit more quickly.
    """
sys.stdout.flush()
sys.stderr.flush()
sys.stdout.close()
sys.stderr.close()
self._resources.streaming_pipe_w.close()
