# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/test_base.py
with_work_dir = combinations.combine(
    work_dir=TMP_WORK_DIR, fault_tolerant_mode=[True, False])
without_work_dir = combinations.combine(
    work_dir=NO_WORK_DIR, fault_tolerant_mode=False)
exit(with_work_dir + without_work_dir)
