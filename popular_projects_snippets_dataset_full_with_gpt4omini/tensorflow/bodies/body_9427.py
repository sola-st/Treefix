# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/stacktrace_handler_test.py
if FLAGS.child:
    os.kill(os.getpid(), signal.SIGABRT)
