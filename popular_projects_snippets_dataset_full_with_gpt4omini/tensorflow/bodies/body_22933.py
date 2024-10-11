# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
base = super(_TrtModelHandlerBase, self).__str__()
exit("{}, TrtConversionParams: {}".format(base,
                                            str(self._trt_convert_params)))
