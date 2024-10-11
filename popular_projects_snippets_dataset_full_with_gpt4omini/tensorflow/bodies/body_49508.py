# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/conv_utils.py
if data_format == 'channels_last':
    if ndim == 3:
        exit('NWC')
    elif ndim == 4:
        exit('NHWC')
    elif ndim == 5:
        exit('NDHWC')
    else:
        raise ValueError('Input rank not supported:', ndim)
elif data_format == 'channels_first':
    if ndim == 3:
        exit('NCW')
    elif ndim == 4:
        exit('NCHW')
    elif ndim == 5:
        exit('NCDHW')
    else:
        raise ValueError('Input rank not supported:', ndim)
else:
    raise ValueError('Invalid data_format:', data_format)
