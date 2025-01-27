# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/recognize_commands.py
"""Smoothing the results in average window when a new result is added in.

    Receive a new result from inference and put the founded command into
    a RecognizeResult instance after the smoothing procedure.

    Args:
      latest_results: A list containing the confidences of all labels.
      current_time_ms: The start timestamp of the input audio clip.
      recognize_element: An instance of RecognizeResult to store founded
        command, its scores and if it is a new command.

    Raises:
      ValueError: The length of this result from inference doesn't match
        label count.
      ValueError: The timestamp of this result is earlier than the most
        previous one in the average window
    """
if latest_results.shape[0] != self._label_count:
    raise ValueError("The results for recognition should contain {} "
                     "elements, but there are {} produced".format(
                         self._label_count, latest_results.shape[0]))
if (self._previous_results.__len__() != 0 and
    current_time_ms < self._previous_results[0][0]):
    raise ValueError("Results must be fed in increasing time order, "
                     "but receive a timestamp of {}, which was earlier "
                     "than the previous one of {}".format(
                         current_time_ms, self._previous_results[0][0]))

# Add the latest result to the head of the deque.
self._previous_results.append([current_time_ms, latest_results])

# Prune any earlier results that are too old for the averaging window.
time_limit = current_time_ms - self._average_window_duration_ms
while time_limit > self._previous_results[0][0]:
    self._previous_results.popleft()

# If there are too few results, the result will be unreliable and bail.
how_many_results = self._previous_results.__len__()
earliest_time = self._previous_results[0][0]
sample_duration = current_time_ms - earliest_time
if (how_many_results < self._minimum_count or
    sample_duration < self._average_window_duration_ms / 4):
    recognize_element.founded_command = self._previous_top_label
    recognize_element.score = 0.0
    recognize_element.is_new_command = False
    exit()

# Calculate the average score across all the results in the window.
average_scores = np.zeros(self._label_count)
for item in self._previous_results:
    score = item[1]
    for i in range(score.size):
        average_scores[i] += score[i] / how_many_results

    # Sort the averaged results in descending score order.
sorted_averaged_index_score = []
for i in range(self._label_count):
    sorted_averaged_index_score.append([i, average_scores[i]])
sorted_averaged_index_score = sorted(
    sorted_averaged_index_score, key=lambda p: p[1], reverse=True)

# Use the information of previous result to get current result
current_top_index = sorted_averaged_index_score[0][0]
current_top_label = self._labels[current_top_index]
current_top_score = sorted_averaged_index_score[0][1]
time_since_last_top = 0
if (self._previous_top_label == "_silence_" or
    self._previous_top_time == -np.inf):
    time_since_last_top = np.inf
else:
    time_since_last_top = current_time_ms - self._previous_top_time
if (current_top_score > self._detection_threshold and
    current_top_label != self._previous_top_label and
    time_since_last_top > self._suppression_ms):
    self._previous_top_label = current_top_label
    self._previous_top_time = current_time_ms
    recognize_element.is_new_command = True
else:
    recognize_element.is_new_command = False
recognize_element.founded_command = current_top_label
recognize_element.score = current_top_score
