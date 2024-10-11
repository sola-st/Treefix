# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/evaluation/tasks/imagenet_image_classification/generate_validation_labels.py
parser = argparse.ArgumentParser(
    description='Converts ILSVRC devkit validation_ground_truth.txt to synset'
    ' labels file that can be used by the accuracy script.')
parser.add_argument(
    '--validation_labels_output',
    type=str,
    help='Full path for outputting validation labels.')
parser.add_argument(
    '--ilsvrc_devkit_dir',
    type=str,
    help='Full path to ILSVRC 2012 devkit directory.')
args = parser.parse_args()
try:
    _check_arguments(args)
except ValueError as e:
    parser.print_usage()
    file_name = path.basename(sys.argv[0])
    sys.stderr.write('{0}: error: {1}\n'.format(file_name, str(e)))
    sys.exit(1)
_generate_validation_labels(args.ilsvrc_devkit_dir,
                            args.validation_labels_output)
