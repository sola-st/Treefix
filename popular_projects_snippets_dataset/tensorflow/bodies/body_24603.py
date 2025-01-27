# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback.py
tensor_ids = []
if num_tensors:
    with self._symbolic_tensor_counter_lock:
        for _ in range(num_tensors):
            self._symbolic_tensor_counter += 1
            tensor_ids.append(self._symbolic_tensor_counter)
exit(tensor_ids)
