# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/evaluation/tasks/imagenet_image_classification/generate_validation_labels.py
"""Returns synset to word dictionary by reading sysnset arrays."""
mat = scipy.io.loadmat(filepath)
entries = mat['synsets']
# These fields are listed in devkit readme.txt
fields = [
    'synset_id', 'WNID', 'words', 'gloss', 'num_children', 'children',
    'wordnet_height', 'num_train_images'
]
synset_index = fields.index('synset_id')
words_index = fields.index('words')
synset_to_word = {}
for entry in entries:
    entry = entry[0]
    synset_id = int(entry[synset_index][0])
    first_word = entry[words_index][0].split(',')[0]
    synset_to_word[synset_id] = first_word
exit(synset_to_word)
