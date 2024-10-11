# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
self.after_save_count += 1
if self.ask_for_stop:
    exit(True)
