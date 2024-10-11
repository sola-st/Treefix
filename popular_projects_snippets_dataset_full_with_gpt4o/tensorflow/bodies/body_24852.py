# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
def init_writer():
    debug_events_writer.DebugEventsWriter(self.dump_root, self.tfdbg_run_id)

num_threads = 4
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=init_writer)
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()

# Verify that there is only one debug event file of each type.
metadata_paths = glob.glob(os.path.join(self.dump_root, "*.metadata"))
self.assertLen(metadata_paths, 1)
source_files_paths = glob.glob(
    os.path.join(self.dump_root, "*.source_files"))
self.assertLen(source_files_paths, 1)
stack_frames_paths = glob.glob(
    os.path.join(self.dump_root, "*.stack_frames"))
self.assertLen(stack_frames_paths, 1)
graphs_paths = glob.glob(os.path.join(self.dump_root, "*.graphs"))
self.assertLen(graphs_paths, 1)
self._readAndCheckMetadataFile()
