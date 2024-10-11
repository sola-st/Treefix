# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/input_data.py
"""Prepares a list of the samples organized by set and label.

    The training loop needs a list of all the available data, organized by
    which partition it should belong to, and with ground truth labels attached.
    This function analyzes the folders below the `data_dir`, figures out the
    right
    labels for each file based on the name of the subdirectory it belongs to,
    and uses a stable hash to assign it to a data set partition.

    Args:
      silence_percentage: How much of the resulting data should be background.
      unknown_percentage: How much should be audio outside the wanted classes.
      wanted_words: Labels of the classes we want to be able to recognize.
      validation_percentage: How much of the data set to use for validation.
      testing_percentage: How much of the data set to use for testing.

    Returns:
      Dictionary containing a list of file information for each set partition,
      and a lookup map for each class to determine its numeric index.

    Raises:
      Exception: If expected files are not found.
    """
# Make sure the shuffling and picking of unknowns is deterministic.
random.seed(RANDOM_SEED)
wanted_words_index = {}
for index, wanted_word in enumerate(wanted_words):
    wanted_words_index[wanted_word] = index + 2
self.data_index = {'validation': [], 'testing': [], 'training': []}
unknown_index = {'validation': [], 'testing': [], 'training': []}
all_words = {}
# Look through all the subfolders to find audio samples
search_path = os.path.join(self.data_dir, '*', '*.wav')
for wav_path in gfile.Glob(search_path):
    _, word = os.path.split(os.path.dirname(wav_path))
    word = word.lower()
    # Treat the '_background_noise_' folder as a special case, since we expect
    # it to contain long audio samples we mix in to improve training.
    if word == BACKGROUND_NOISE_DIR_NAME:
        continue
    all_words[word] = True
    set_index = which_set(wav_path, validation_percentage, testing_percentage)
    # If it's a known class, store its detail, otherwise add it to the list
    # we'll use to train the unknown label.
    if word in wanted_words_index:
        self.data_index[set_index].append({'label': word, 'file': wav_path})
    else:
        unknown_index[set_index].append({'label': word, 'file': wav_path})
if not all_words:
    raise Exception('No .wavs found at ' + search_path)
for index, wanted_word in enumerate(wanted_words):
    if wanted_word not in all_words:
        raise Exception('Expected to find ' + wanted_word +
                        ' in labels but only found ' +
                        ', '.join(all_words.keys()))
    # We need an arbitrary file to load as the input for the silence samples.
    # It's multiplied by zero later, so the content doesn't matter.
silence_wav_path = self.data_index['training'][0]['file']
for set_index in ['validation', 'testing', 'training']:
    set_size = len(self.data_index[set_index])
    silence_size = int(math.ceil(set_size * silence_percentage / 100))
    for _ in range(silence_size):
        self.data_index[set_index].append({
            'label': SILENCE_LABEL,
            'file': silence_wav_path
        })
    # Pick some unknowns to add to each partition of the data set.
    random.shuffle(unknown_index[set_index])
    unknown_size = int(math.ceil(set_size * unknown_percentage / 100))
    self.data_index[set_index].extend(unknown_index[set_index][:unknown_size])
# Make sure the ordering is random.
for set_index in ['validation', 'testing', 'training']:
    random.shuffle(self.data_index[set_index])
# Prepare the rest of the result data structure.
self.words_list = prepare_words_list(wanted_words)
self.word_to_index = {}
for word in all_words:
    if word in wanted_words_index:
        self.word_to_index[word] = wanted_words_index[word]
    else:
        self.word_to_index[word] = UNKNOWN_WORD_INDEX
self.word_to_index[SILENCE_LABEL] = SILENCE_INDEX
