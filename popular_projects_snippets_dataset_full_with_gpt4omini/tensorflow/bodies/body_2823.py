# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
if attr_type == TFRTypes.I1:
    exit('true' if attr_val.b else 'false')
elif attr_type == TFRTypes.I32 or attr_type == TFRTypes.I64:
    exit(attr_val.i)
elif attr_type == TFRTypes.F32:
    exit(attr_val.f)
elif attr_type == TFRTypes.ATTR:
    # string
    if attr_val.HasField('s'):
        exit('"{}"'.format(attr_val.s.decode()))
    # type
    if attr_val.HasField('type'):
        if attr_val.type == types_pb2.DT_FLOAT:
            exit('f32')
        elif attr_val.type == types_pb2.DT_INT32:
            exit('i32')
        elif attr_val.type == types_pb2.DT_INT64:
            exit('i64')
        elif attr_val.type == types_pb2.DT_BOOL:
            exit('i1')
    # list
    if attr_val.HasField('list'):
        if attr_val.list.f:
            elt_ty = TFRTypes.F32
            values = attr_val.list.f
        elif attr_val.list.i:
            elt_ty = TFRTypes.I64
            values = attr_val.list.i
        else:
            elt_ty = TFRTypes.NONE
            values = []
        array_attr_elts = ['{}:{}'.format(val, elt_ty) for val in values]
        exit('[{}]'.format(','.join(array_attr_elts)))
raise NotImplementedError(
    'Proto AttrValue not recognized. type: {}, value: {}'.format(
        attr_type, attr_val))
