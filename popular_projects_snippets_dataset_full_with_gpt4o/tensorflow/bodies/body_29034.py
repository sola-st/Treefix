# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/snapshot_test.py
# Ignore the graphdef pbtxts we write for debugging purposes and temporary
# files that are an artifact of how TF writes files.
dirlist = listdir_and_filter(
    directory, lambda p: not (is_graphdef_file(p) or is_temp_file(p)))
self.assertLen(dirlist, num_fingerprints)

for i in range(num_fingerprints):
    fingerprint_dir = os.path.join(directory, dirlist[i])
    fingerprint_dir_list = listdir_and_filter(fingerprint_dir,
                                              lambda p: not is_temp_file(p))
    self.assertLen(fingerprint_dir_list, num_runs_per_fp + 1)
    self.assertEqual(fingerprint_dir_list[num_runs_per_fp],
                     "snapshot.metadata")

    for j in range(num_runs_per_fp):
        run_dir = os.path.join(fingerprint_dir, fingerprint_dir_list[j])
        run_dirlist = sorted(os.listdir(run_dir))
        self.assertLen(run_dirlist, num_snapshot_files)

        file_counter = 0
        for filename in run_dirlist:
            self.assertEqual(filename, "%08d.snapshot" % file_counter)
            file_counter += 1
