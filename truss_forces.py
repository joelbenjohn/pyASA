# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# % truss_forces.m - September 23, 2020                               % 
# % author: J Carroll,Civil Eng,JHU (derived from JK Guest,JHU) 
# % Modified: 10/08/20, Joel Ben John  %
# % post processing of member forces for 2D and 3D trusses            %
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
from get_de_from_dcomp import get_de_from_dcomp
def truss_forces(dcomp, Ke, Te, ien, nen, ndf, A, E):

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

    # % Step 1: Get displacements for element
    de = get_de_from_dcomp(dcomp, ien, nen, ndf)
    
    # % Step 2: Compute element forces in global coord sys
    Fe = Ke@de    

    # % Step 3: Transform Fe to local coordinate system
    fe_local = Te@Fe

    # % Step 4: Compute axial force, stress, strain
    # % Use second local force for truss element
    axial = fe_local[1] 
    stress = axial/A;   strain = stress/E
    return Fe, axial, stress, strain
