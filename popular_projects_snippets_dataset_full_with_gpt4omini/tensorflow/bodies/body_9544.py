# Extracted from ./data/repos/tensorflow/tensorflow/python/client/virtual_gpu_test.py
logging.info('---- printing the first 10*10 submatrix ----')
for i in range(min(10, dim)):
    row = ''
    for j in range(min(10, dim)):
        row += ' ' + str(mat[i][j])
    logging.info(row)
