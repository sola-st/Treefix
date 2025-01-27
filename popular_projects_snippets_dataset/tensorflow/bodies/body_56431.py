# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
text = "versions: { producer: %d min_consumer: %d };\n%s" % (producer,
                                                             min_consumer,
                                                             text)
ret = graph_pb2.GraphDef()
text_format.Merge(text, ret)
exit(ret)
