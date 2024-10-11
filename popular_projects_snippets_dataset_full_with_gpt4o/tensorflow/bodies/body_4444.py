# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/accuracy_utils.py
"""Calculate accuracy statistics when a new commands is founded.

    Given ground truth and corresponding predictions founded by
    model, figure out how many were correct. Take a tolerance time, so that only
    predictions up to a point in time are considered.

    Args:
        found_words: A list of all founded commands up to now.
        up_to_time_ms: End timestamp of this audio piece.
        time_tolerance_ms: The tolerance milliseconds before and after
          up_to_time_ms to match a ground truth.
    """
if up_to_time_ms == -1:
    latest_possible_time = np.inf
else:
    latest_possible_time = up_to_time_ms + time_tolerance_ms
self._how_many_gt = 0
for ground_truth in self._gt_occurrence:
    ground_truth_time = ground_truth[1]
    if ground_truth_time > latest_possible_time:
        break
    self._how_many_gt += 1
self._how_many_fp = 0
self._how_many_c = 0
self._how_many_w = 0
has_gt_matched = []
for found_word in found_words:
    found_label = found_word[0]
    found_time = found_word[1]
    earliest_time = found_time - time_tolerance_ms
    latest_time = found_time + time_tolerance_ms
    has_matched_been_found = False
    for ground_truth in self._gt_occurrence:
        ground_truth_time = ground_truth[1]
        if (ground_truth_time > latest_time or
            ground_truth_time > latest_possible_time):
            break
        if ground_truth_time < earliest_time:
            continue
        ground_truth_label = ground_truth[0]
        if (ground_truth_label == found_label and
            has_gt_matched.count(ground_truth_time) == 0):
            self._how_many_c += 1
        else:
            self._how_many_w += 1
        has_gt_matched.append(ground_truth_time)
        has_matched_been_found = True
        break
    if not has_matched_been_found:
        self._how_many_fp += 1
self._how_many_gt_matched = len(has_gt_matched)
