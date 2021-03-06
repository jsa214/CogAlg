import numpy as np
import numpy.ma as ma

from filters import get_filters
get_filters(globals())  # imports all filters at once

def comp_deriv(blob):  # compare g within sub blob, a component of intra_blob

    dert__ = ma.empty(shape=blob.dert__.shape, dtype=int)   # initialize dert__
    g__ = ma.array(blob.dert__[:, :, 3], mask=~blob.map)    # apply mask = ~map

    dy__ = g__[2:, 1:-1] - g__[:-2, 1:-1]  # vertical comp between rows -> dy, (1:-1): first and last column are discarded
    dx__ = g__[1:-1, 2:] - g__[1:-1, :-2]  # lateral comp between columns -> dx, (1:-1): first and last row are discarded
    gg__ = np.hypot(dy__, dx__) - ave      # deviation of gradient

    # pack all derts into dert__
    dert__[:, :, 0] = g__
    dert__[1:-1, 1:-1, 1] = dy__  # first row, last row, first column and last-column are discarded
    dert__[1:-1, 1:-1, 2] = dx__
    dert__[1:-1, 1:-1, 3] = gg__

    blob.new_dert__[0] = dert__  # pack dert__ into blob
    return 1  # comp rng
