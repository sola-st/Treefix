# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/remapper_test.py
super(RemapperTest, self).setUp()
# GeluApproximate fusion on GPU requires cublasLt.
os.environ['TF_USE_CUBLASLT'] = '1'
# GeluExact fusion and conv runtime fusion on GPU requires cuDNN frontend.
os.environ['TF_CUDNN_USE_FRONTEND'] = '1'
os.environ['TF_CUDNN_USE_RUNTIME_FUSION'] = '1'
