# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/evaluation/tasks/imagenet_image_classification/generate_validation_labels.py
synset_to_word = _synset_to_word(_synset_array_path(ilsvrc_dir))
with open(_validation_file_path(ilsvrc_dir), 'r') as synset_id_file, open(
    output_file, 'w') as output:
    for synset_id in synset_id_file:
        synset_id = int(synset_id)
        output.write('%s\n' % synset_to_word[synset_id])
