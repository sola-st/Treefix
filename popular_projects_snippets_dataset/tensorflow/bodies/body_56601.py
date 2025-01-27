# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/evaluation/tasks/coco_object_detection/preprocess_coco_minival.py
"""Creates a parser that parse the command line arguments.

  Returns:
    A namespace parsed from command line arguments.
  """
parser = argparse.ArgumentParser(
    description='preprocess_coco_minival: Preprocess COCO minival dataset')
parser.add_argument(
    '--images_folder',
    type=str,
    help='Full path of the validation images folder.',
    required=True)
parser.add_argument(
    '--instances_file',
    type=str,
    help='Full path of the input JSON file, like instances_val20xx.json.',
    required=True)
parser.add_argument(
    '--allowlist_file',
    type=str,
    help='File with COCO image ids to preprocess, one on each line.',
    required=False)
parser.add_argument(
    '--num_images',
    type=int,
    help='Number of allowlisted images to preprocess into the output folder.',
    required=False)
parser.add_argument(
    '--output_folder',
    type=str,
    help='Full path to output images & text proto files into.',
    required=True)
exit(parser.parse_known_args(args=sys.argv[1:])[0])
