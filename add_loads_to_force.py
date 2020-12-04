# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# % add_loads_to_force.m - October 13,  2010                 %
# % author: James K Guest, CE Dept, JHU                      %
# % Modified: 09/27/20, Joel Ben John                        %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def add_loads_to_force(F, f, id, nnp, ndf):
    # %------------------------------------------------------------------------
    # %  Adds the applied load nodal vector into global force vector using eqn numbers
    # %
    # %  Variable Descriptions:
    # %  Return:
    # %     F  = updated global force vector
    # %  Given:
    # %     F  = global force vector
    # %     f  = applied nodal loads (ndf,nnp)
    # %     id(i,n) = displacement equation number for dof i, node n 
    # %     nnp = number of nodal points
    # %     ndf = number degrees of freedom per node
    # %------------------------------------------------------------------------

    # % Loop over nodes and degrees of freedom
    for j in range(nnp):
        for i in range(ndf):
            # Get global equation number
            gen = int(id[i, j])-1
            # Check Global Equation Number
            if gen != 0:
                # Add nodal load to global force vector
                F[gen] = f[i, j]
    return F