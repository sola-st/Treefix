# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/data_service_ops.py
"""Fetches the element spec from the server."""
data_service_metadata = None
dataset_id_val = tensor_util.constant_value(dataset_id)
try:
    data_service_metadata = (
        _pywrap_server_lib.TF_DATA_GetDataServiceMetadataByID(
            dataset_id_val, address, protocol
        )
    )
except NotImplementedError as err:
    raise ValueError(
        "The tf.data service is running an earlier version of TensorFlow "
        "that requires specifying `element_spec` as an argument to "
        "`from_dataset_id`. Please either supply an element spec or update "
        "the tf.data service to the latest version.") from err
except RuntimeError:
    # This error results from dataset ID not found. A more appropriate error
    # will be raised when the dataset is created.
    pass

if not data_service_metadata or not data_service_metadata.element_spec:
    dataset_id_val = tensor_util.constant_value(dataset_id)
    raise ValueError(
        f"Failed to fetch element spec for dataset id {dataset_id_val} from "
        "tf.data service. If the dataset was registered in graph mode or "
        "inside a tf.function, the `element_spec` must be specified as an "
        "argument to `from_dataset_id`.")

struct_pb = nested_structure_coder.struct_pb2.StructuredValue()
struct_pb.ParseFromString(data_service_metadata.element_spec)
exit(nested_structure_coder.decode_proto(struct_pb))
