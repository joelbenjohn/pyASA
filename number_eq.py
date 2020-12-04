# %********************************************************************%
# % number_eq.m - Created October 5, 2006                              %
# % Author:    James K Guest, Civil Eng Dept, Johns Hopkins University %
# % Modified:  12/03/20, Joel Ben John      
# %ASSUMES REDUCED STORAGE APPROACH
import numpy as np
def number_eq(idb, nnp, ndf):

# %------------------------------------------------------------------------
# %  Assigns equation numbers to unknown displacement degrees of freedom
# %     for global stiffness and force assembly 
# %
# %  ASSUMES REDUCED STORAGE APPROACH! 
# %  Need more output for Complete Storage Approach
# %
# %  Variable Descriptions:
# %  Return:
# %     id(i,n) = equation number corresponding to dof i of node n
# %     neq = total number of equations
# %  Given:
# %     idb(i,n) = boundary condition flag for dof i of node n
# %     nnp  = number of nodes
# %     ndf  = number of degrees of freedom per node
# %------------------------------------------------------------------------
#   initialize id
    id = np.zeros((ndf, nnp))
    count = 0
    for i in range(nnp):
        for j in range(ndf):
            if idb[j, i] == 0:
                count = count + 1
                id[j, i] = count
    neq = count
    return id, neq