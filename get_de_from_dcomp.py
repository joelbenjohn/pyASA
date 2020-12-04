# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# % get_de_from_dcomp.m - October , 21 2008                  %
# % author: James K Guest, CE Dept, JHU                      %
# % revised: Sep 23 2020            JDWC: initialize de      %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
import numpy as np
def get_de_from_dcomp(dcomp, ien, nen, ndf):
# %------------------------------------------------------------------------
# %  Extracts element displacement vector from complete displacement vector
# %
# %  Variable Descriptions:
# %  Return:
# %     de(nen*ndf) = element displacement vector in global coordinate system
# %  Given:
# %     dcomp(i,n) = displacement for dof i at global node n
# %     ien = element connectivity array
# %     nen  = number of nodes per element
# %     ndf  = number of degrees of freedom per node

    # initialize de
    de = np.zeros(ndf*nen)          
    for i in range(nen):
        for j in range(ndf):
            # local equation number
            leq = i*ndf + j + 1   
            de[leq-1] = dcomp[j, int(ien[i])-1]

    return de
