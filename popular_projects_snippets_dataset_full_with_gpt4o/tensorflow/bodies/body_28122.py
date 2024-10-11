# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_test_base.py
example = example_pb2.Example(
    features=feature_pb2.Features(
        feature={
            "file":
                feature_pb2.Feature(
                    int64_list=feature_pb2.Int64List(value=[f])),
            "record":
                feature_pb2.Feature(
                    int64_list=feature_pb2.Int64List(value=[r])),
            "keywords":
                feature_pb2.Feature(
                    bytes_list=feature_pb2.BytesList(
                        value=self._get_keywords(f, r))),
            "label":
                feature_pb2.Feature(
                    bytes_list=feature_pb2.BytesList(
                        value=[compat.as_bytes(l)]))
        }))
exit(example.SerializeToString())
