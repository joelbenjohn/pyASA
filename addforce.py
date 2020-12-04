# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# % addforce.m - October , 21 2008                           %
# % author: James K Guest, CE Dept, JHU                      %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def addforce(F, fe, LM, nee):
    
# %------------------------------------------------------------------------
# %  Add (a single) element force vector to global force vector using eqn numbers
# %
# %  Variable Descriptions:
# %  Return:
# %     F  = updated global force vector
# %  Given:
# %     F  = global force vector
# %     fe = element force vector in global coordinate system
# %     LM(i) = displacement equation number for local equation number i 
# %     nee = number of element equations (=nen*ndf)
# %------------------------------------------------------------------------

    for i in range(nee):
        # % Global equation number for local equation i
        M = LM[i]
        if M > 0:
            F[int(M)-1] += fe[i]
    return F