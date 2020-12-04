# % get_local_id.m - Created October 21, 2008                          %
# % author: James K Guest, CE Dept, JHU                                %
# % Modified:  October 7, 2015, Hak Yong Lee    
import numpy as np
def get_local_id(id, ien, nen, ndf):
    # initialize LM
    LM = np.zeros(ndf*nen)
    # loop over number of nodes per element
    for j in range(nen):
        # loop over number of degrees of freedom
        for i in range(ndf):
            # Local equation number
            leq = j*ndf + i + 1
            # Find global equation number matching each node
            LM[leq-1] = id[i, int(ien[j])-1] 
    return LM