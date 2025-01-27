# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/combined_nms_test.py
super().tearDown()
os.environ['TF_TRT_ALLOW_NMS_TOPK_OVERRIDE'] = '0'
