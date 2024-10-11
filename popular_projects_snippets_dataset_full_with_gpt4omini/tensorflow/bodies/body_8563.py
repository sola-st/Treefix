# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
return_codes = []
for p in nest.flatten(worker_processes):
    try:
        # Calling p.wait() will hang if we don't consume its output.
        p.communicate()
    except ValueError:
        # The output of the process may have been consumed, in which case
        # calling `p.communicate()` will raise a ValueError.
        pass
    finally:
        return_codes.append(p.returncode)
for return_code in return_codes:
    self.assertEqual(return_code, 0)
