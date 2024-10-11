# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py

if multi_process_runner.is_oss() or sys.version_info >= (3, 7):
    self.skipTest('TODO(b/171004637): Failing in OSS and Python 3.7+')

def fn_expected_to_seg_fault():
    if multi_worker_test_base.get_task_type() == 'worker':
        time.sleep(10000)
    ctypes.string_at(0)  # Intentionally made seg fault.

with self.assertRaises(
    multi_process_runner.UnexpectedSubprocessExitError) as cm:
    multi_process_runner.run(
        fn_expected_to_seg_fault,
        multi_worker_test_base.create_cluster_spec(
            has_chief=True, num_workers=1),
        return_output=True)
self.assertIn('Subprocess chief-0 exited with exit code',
              str(cm.exception))
list_to_assert = cm.exception.mpr_result.stdout
self.assertTrue(
    any('Segmentation fault' in line for line in list_to_assert))
