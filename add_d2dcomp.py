# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# % add_d2dcomp.m - October , 13 2010                        %
# % author: James K Guest, CE Dept, JHU                      %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
import numpy as np

def add_d2dcomp(dcomp, du, id, nnp, ndf):
#  %------------------------------------------------------------------------
# %  Creates complete displacement (ndf,nnp) by adding in d (free dof)
# %
# %  Variable Descriptions:
# %  Return:
# %     dcomp(ndf,nnp) = complete displacement vector in global coordinate system
# %  Given:
# %     dcomp(i,n) = displacement for dof i at global node n
# %     id(i,n) = global equation number for dof i at global node n
# %     nnp  = number of nodes
# %     ndf  = number of degrees of freedom per node
# %-------------------------------------------------
    for n in range(nnp):
        for i in range(ndf):
            # Check free dof
            if id[i, n] > 0:
                dcomp[i, n] = dcomp[i, n] + du[int(id[i, n])-1]
    return dcomp