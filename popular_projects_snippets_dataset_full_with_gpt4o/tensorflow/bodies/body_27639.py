# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/index_shuffle_test.py
file_infos = []
file_infos.append({
    "path": "take_50",
    "num_elements": 100,
    "skip": 25,
    "take": 50
})
file_infos.append({
    "path": "skip_all",
    "num_elements": 100,
    "skip": -1,
})
file_infos.append({
    "path": "take_all",
    "num_elements": 100,
    "take": -1
})
file_infos.append({
    "path": "take_10",
    "num_elements": 100,
    "skip": 90,
    "take": 20
})
result = shuffle_ops._process_file_infos(file_infos)
self.assertEqual(result["files"],
                 ["take_50", "skip_all", "take_all", "take_10"])
self.assertEqual(result["num_elements"], 160)
inputs = [0, 49, 50, 51, 149, 150, 151, 159]
expected = [25, 74, 200, 201, 299, 390, 391, 399]
for i, expected in enumerate(expected):
    self.assertEqual(
        self.evaluate(
            shuffle_ops._adjust_index([inputs[i]], result["thresholds"],
                                      result["offsets"])), expected)
