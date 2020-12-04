# %********************************************************************%
# % Ke_truss.m - Created October 5, 2006                               %
# % Author:    James K Guest, Civil Eng Dept, Johns Hopkins University %
# % Modified:  Joel Ben John, 12/03/20      
import numpy as np
def Ke_truss(E, A, xn, ien, nen, ndf, nsd):
# %------------------------------------------------------------------------
# %  Computes the truss element stiffness matrix
# % 
# %  Variable Descriptions:
# %  Return:
# %     ke = element stiffness matrix in local coordinate system
# %     Ke = element stiffness matrix in global coordinate system
# %     Te = element transformation matrix (transform global to local)
# %  Given:
# %     E,A = Young's modulus, area for current element
# %     xn = nodal coordinate array
# %     ien = element connectivity array
# %     nen  = number of nodes per element
# %     ndf  = number of degrees of freedom per node
# %     nsd  = number of spatial dimensions
# %------------------------------------------------------------------------

    # % Step 1: Identify the nodes the element is connected to
    n1 = int(ien[0])
    n2 = int(ien[1])
    # % Step 2: Form vector along axis of element using nodal coordinates
    vx = xn[0, n2-1] - xn[0, n1-1]; vy = 0; vz = 0
    if(nsd == 2):
        vy = xn[1, n2-1] - xn[1, n1-1]
    if nsd == 3:
        vy = xn[1, n2-1] - xn[1, n1-1]; vz = xn[2, n2-1] - xn[2, n1-1]
    # % Step 3: Compute the length of element using the vector
    L = np.sqrt(vx**2 + vy**2 + vz**2)
    # % Step 4: Local stiffness
    ke = E*A/L*np.array([[1, -1], [-1, 1]])
    # % Step 5: Transformation matrix: global to local coordinate system
    if nsd == 1:
        Te = 1 if vx>0 else -1
    elif nsd == 2:
        c = vx/L; s = vy/L
        Te = np.array([[c, s, 0, 0], [0, 0, c, s]])
    elif nsd == 3:
        c1=vx/L; c2=vy/L; c3=vz/L
        Te = np.array([[c1, c2, c3, 0, 0, 0], [0, 0, 0, c1, c2, c3]])
    # % Step 6: Element Stiffness in Global Coordinates Ke(i,j)
    Ke = np.transpose(Te)@ke@Te
    return Ke, ke, Te
