# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/evaluation/tasks/coco_object_detection/preprocess_coco_minival.py
"""Dumps images & data from ground-truth objects into output_folder_path.

  The following are created in output_folder_path:
    images/: sub-folder for allowlisted validation images.
    ground_truth.pb: A binary proto file containing all ground-truth
    object-sets.

  Args:
    ground_truth_detections: A dict mapping image id to ground truth data.
      Output of _get_ground_truth_detections.
    images_folder_path: Validation images folder
    output_folder_path: folder to output files to.
  """
# Ensure output folders exist.
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)
output_images_folder = os.path.join(output_folder_path, 'images')
if not os.path.exists(output_images_folder):
    os.makedirs(output_images_folder)
output_proto_file = os.path.join(output_folder_path, 'ground_truth.pb')

ground_truth_data = evaluation_stages_pb2.ObjectDetectionGroundTruth()
for image_dict in ground_truth_detections.values():
    # Create an ObjectsSet proto for this file's ground truth.
    detection_result = ground_truth_data.detection_results.add()
    detection_result.image_id = image_dict['id']
    detection_result.image_name = image_dict['file_name']
    for detection_dict in image_dict['detections']:
        object_instance = detection_result.objects.add()
        object_instance.bounding_box.normalized_top = detection_dict['bbox'][0]
        object_instance.bounding_box.normalized_left = detection_dict['bbox'][1]
        object_instance.bounding_box.normalized_bottom = detection_dict['bbox'][2]
        object_instance.bounding_box.normalized_right = detection_dict['bbox'][3]
        object_instance.class_id = detection_dict['category_id']
    # Copy image.
    shutil.copy2(
        os.path.join(images_folder_path, image_dict['file_name']),
        output_images_folder)

# Dump proto.
with open(output_proto_file, 'wb') as proto_file:
    proto_file.write(ground_truth_data.SerializeToString())
