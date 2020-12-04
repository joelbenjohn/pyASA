# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# % assemble_rxn.m - September 23, 2020                               % 
# % author: J Carroll,Civil Eng,JHU (derived from JK Guest,JHU)       %
# % assemble reactions from element forces (reduced storage)          %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
import numpy as np
from get_local_id import get_local_id
from addforce import addforce
from add_d2dcomp import add_d2dcomp
from number_eq import number_eq
def assemble_rxns(Fe, idb, nnp, ndf, nee, ien, nen, nel):
# %------------------------------------------------------------------------
# %  Extracts element displacement vector from complete displacement vector
# %
# %  Variable Descriptions:
# %  Return:
# %     Fe(nen*ndf) = element force vector in global coordinate system
# %  Given:
# %     dcomp(i,n) = displacement for dof i at global node n
# %     Ke = element stiffness matrix in global coordinate system
# %     Te = element transformation matrix
# %     ien = element connectivity array
# %     nen  = number of nodes per element
# %     ndf  = number of degrees of freedom per node
# %     A,E = area, Young's modulus for current element
# %------------------------------------------------------------------------
    idbr = 1 - idb
    [idr, neqr] = number_eq(idbr, nnp, ndf)
    LMr = np.zeros((nee, nel))
    for n in range(nel):
        LMr[:, n] = get_local_id(idr, ien[:, n], nen, ndf)
    LMr = np.array(LMr) 
    R = np.zeros(neqr)
    for n in range(nel):
        R = addforce(R, Fe[:, n], LMr[:, n], nee)
    Rcomp = add_d2dcomp(np.zeros((ndf, nnp)), R, idr, nnp, ndf)

    return Rcomp
# %%
