# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
super(ProfilerHookTest, self).tearDown()
shutil.rmtree(self.output_dir, ignore_errors=True)
