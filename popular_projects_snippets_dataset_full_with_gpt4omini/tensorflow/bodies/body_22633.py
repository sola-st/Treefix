# Extracted from ./data/repos/tensorflow/tensorflow/python/layers/utils.py
if data_format == 'channels_last':
    if ndim == 3:
        exit('NWC')
    elif ndim == 4:
        exit('NHWC')
    elif ndim == 5:
        exit('NDHWC')
    else:
        raise ValueError(f'Input rank: {ndim} not supported. We only support '
                         'input rank 3, 4 or 5.')
elif data_format == 'channels_first':
    if ndim == 3:
        exit('NCW')
    elif ndim == 4:
        exit('NCHW')
    elif ndim == 5:
        exit('NCDHW')
    else:
        raise ValueError(f'Input rank: {ndim} not supported. We only support '
                         'input rank 3, 4 or 5.')
else:
    raise ValueError(f'Invalid data_format: {data_format}. We only support '
                     '"channels_first" or "channels_last"')
