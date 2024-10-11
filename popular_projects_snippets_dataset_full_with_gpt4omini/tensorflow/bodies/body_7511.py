# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
"""Main function to be called within `__main__` of a test file.

  Any test module that uses
  `tf.__internal__.distribute.multi_process_runner.run()`
  must call this instead of regular `test.main()` inside
  `if __name__ == '__main__':` block, or an error will be raised when
  `tf.__internal__.distribute.multi_process_runner.run()` is used. This method
  takes
  care of needed initialization for launching multiple subprocesses.

  Example:
  ```python
  class MyTestClass(tf.test.TestCase):
    def testSomething(self):
      # Testing code making use of
      # `tf.__internal__.distribute.multi_process_runner.run()`.

  if __name__ == '__main__':
    tf.__internal__.distribute.multi_process_runner.test_main()
  ```
  """
# Inject tearDownModule() to shut down all pool runners. Active pool runners
# will block the program from exiting. This is necessary for global pool
# runners. We tried atexit in the past, and it doesn't work in some
# deployment.
old_tear_down_module = getattr(sys.modules['__main__'], 'tearDownModule',
                               None)

def tear_down_module():
    _shutdown_all_pool_runners()
    if old_tear_down_module is not None:
        old_tear_down_module()

setattr(sys.modules['__main__'], 'tearDownModule', tear_down_module)
multi_process_lib.test_main()
