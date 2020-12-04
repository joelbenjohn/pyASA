# %************************************************************%
# % addstiff.m - Created October 21, 2008                      %
# % author:   James K Guest, CE Dept, Johns Hopkins University %
# % Modified: 12/03/20 , Joel Ben John                         %
# %************************************************************%
def addstiff(K, Ke, LM, nee):
    # %------------------------------------------------------------------------
    # %  Adds (a single) element stiffness matrix to global stiffness matrix using eqn numbers
    # % 
    # %  Variable Descriptions:
    # %  Return:
    # %     K  = updated global stiffness matrix
    # %  Given:
    # %     K  = global stiffness matrix
    # %     Ke = element stiffness matrix in global coordinate system
    # %     LM(i) = displacement equation number for local equation number i 
    # %     nee = number of element equations (=nen*ndf)
    # %------------------------------------------------------------------------
    for i in range(nee):
        for j in range(nee):
            if LM[i] != 0 and LM[j] != 0:
                K[int(LM[i])-1, int(LM[j])-1] += Ke[i, j]
    return K