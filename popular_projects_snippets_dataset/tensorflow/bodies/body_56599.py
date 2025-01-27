# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/evaluation/tasks/coco_object_detection/preprocess_coco_minival.py
"""Processes the annotations JSON file and returns ground truth data corresponding to allowlisted image IDs.

  Args:
    instances_file: COCO instances JSON file, usually named as
      instances_val20xx.json.
    allowlist_file: File containing COCO minival image IDs to allowlist for
      evaluation, one per line.
    num_images: Number of allowlisted images to pre-process. First num_images
      are chosen based on sorted list of filenames. If None, all allowlisted
      files are preprocessed.

  Returns:
    A dict mapping image id (int) to a per-image dict that contains:
      'filename', 'image' & 'height' mapped to filename & image dimensions
      respectively
      AND
      'detections' to a list of detection dicts, with each mapping:
        'category_id' to COCO category id (starting with 1) &
        'bbox' to a list of dimension-normalized [top, left, bottom, right]
        bounding-box values.
  """
# Read JSON data into a dict.
with open(instances_file, 'r') as annotation_dump:
    data_dict = ast.literal_eval(annotation_dump.readline())

image_data = collections.OrderedDict()

# Read allowlist.
if allowlist_file is not None:
    with open(allowlist_file, 'r') as allowlist:
        image_id_allowlist = set([int(x) for x in allowlist.readlines()])
else:
    image_id_allowlist = [image['id'] for image in data_dict['images']]

# Get image names and dimensions.
for image_dict in data_dict['images']:
    image_id = image_dict['id']
    if image_id not in image_id_allowlist:
        continue
    image_data_dict = {}
    image_data_dict['id'] = image_dict['id']
    image_data_dict['file_name'] = image_dict['file_name']
    image_data_dict['height'] = image_dict['height']
    image_data_dict['width'] = image_dict['width']
    image_data_dict['detections'] = []
    image_data[image_id] = image_data_dict

shared_image_ids = set()
for annotation_dict in data_dict['annotations']:
    image_id = annotation_dict['image_id']
    if image_id in image_data:
        shared_image_ids.add(image_id)

output_image_ids = sorted(shared_image_ids)
if num_images:
    if num_images <= 0:
        logging.warning(
            '--num_images is %d, hence outputing all annotated images.',
            num_images)
    elif num_images > len(shared_image_ids):
        logging.warning(
            '--num_images (%d) is larger than the number of annotated images.',
            num_images)
    else:
        output_image_ids = output_image_ids[:num_images]

for image_id in list(image_data):
    if image_id not in output_image_ids:
        del image_data[image_id]

  # Get detected object annotations per image.
for annotation_dict in data_dict['annotations']:
    image_id = annotation_dict['image_id']
    if image_id not in output_image_ids:
        continue

    image_data_dict = image_data[image_id]
    bbox = annotation_dict['bbox']
    # bbox format is [x, y, width, height]
    # Refer: http://cocodataset.org/#format-data
    top = bbox[1]
    left = bbox[0]
    bottom = top + bbox[3]
    right = left + bbox[2]
    if (top > image_data_dict['height'] or left > image_data_dict['width'] or
        bottom > image_data_dict['height'] or right > image_data_dict['width']):
        continue
    object_d = {}
    object_d['bbox'] = [
        top / image_data_dict['height'], left / image_data_dict['width'],
        bottom / image_data_dict['height'], right / image_data_dict['width']
    ]
    object_d['category_id'] = annotation_dict['category_id']
    image_data_dict['detections'].append(object_d)

exit(image_data)
