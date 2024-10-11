# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/evaluation/tasks/imagenet_image_classification/generate_validation_labels.py
if not args.validation_labels_output:
    raise ValueError('Invalid path to output file.')
ilsvrc_dir = args.ilsvrc_devkit_dir
if not ilsvrc_dir or not path.isdir(ilsvrc_dir):
    raise ValueError('Invalid path to ilsvrc_dir')
if not path.exists(_validation_file_path(ilsvrc_dir)):
    raise ValueError('Invalid path to ilsvrc_dir, cannot find validation file.')
if not path.exists(_synset_array_path(ilsvrc_dir)):
    raise ValueError(
        'Invalid path to ilsvrc_dir, cannot find synset arrays file.')
