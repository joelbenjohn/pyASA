# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# % main_truss.m - October 9 2006                                           % 
# % author: JK Guest,Civil Eng,JHU (derived from JH Prevost,CEE,Princeton U)%
import Data
from number_eq import number_eq
from Ke_truss import Ke_truss
from get_local_id import get_local_id
from add_loads_to_force import add_loads_to_force
from addstiff import addstiff
from truss_forces import truss_forces
from add_d2dcomp import add_d2dcomp
from assemble_rxn import assemble_rxns
import numpy as np
def maintruss():
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # %                          DATA                            %
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    print(' *******             Reading Data             *******')
    data = Data.DATA
    nsd = data['nsd']; ndf = data['ndf']; nen = data['nen']; nel = data['nel']; nnp = data['nnp']
    xn = data['xn']; ien = data['ien']; E = data['E']; A = data['A']; idb = data['idb']
    f = data['f']; g = data['g']


    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # % Number the equations - build id table    %
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    print(' *******         Numbering Equations          *******')
    id, neq = number_eq(idb, nnp, ndf)

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # % Compute element stiffness matrices (Ke is in global coord system)   %
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    print(' *******  Forming Element Stiffness Matrices  *******')
    Ke = np.zeros((nen*ndf,nen*ndf,nel))
    ke = np.zeros((nen*1,nen*1,nel))
    Te = np.zeros((nen*1,nen*nsd,nel))
    for i in range(nel):
        Ke[:,:,i],ke[:,:,i],Te[:,:,i] = Ke_truss(E[i],A[i],xn,ien[:,i],nen,ndf,nsd)
        
        
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # % Organize equation number information to element level               %
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    nee = ndf*nen
    LM = np.zeros((nee, nel))
    for i in range(nel):
        LM[:, i] = get_local_id(id, ien[:, i], nen, ndf)

    if neq> 0:
        print(' *******    Assembling Global Force Vector    *******')
        F = np.zeros(neq)
        # % Insert applied loads into F 
        F = add_loads_to_force(F,f,id,nnp,ndf) 
        
    #     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #     % Assemble Global Stiffness Matrix                                  %
    #     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
        print(' *******  Assembling Global Stiffness Matrix  *******')
        K = np.zeros((neq,neq))
        for i in range(nel):
            K = addstiff(K,Ke[:,:,i],LM[:,i],nee)
                            
    #     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #     % Solve the system of equations                                     %
    #     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        print(' *******   Solving for Nodal Displacements    *******')
        du = np.linalg.inv(K)@F
    print(' *******                                      *******')
    print(' *******     STRUCTURAL ANALYSIS COMPLETE     *******')
    print(' *******                                      *******')
    print(' *******        Begin Post-Processing         *******')
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # %                     Post Processing                      %
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # %       AXIAL FORCES/STRESSES          %
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    print(' *******        Compute Element Forces        *******')
    # % element forces in global coordinates  
    Fe = np.zeros((ndf*nen,nel))
    # % element axial, stress, strain
    axial = np.zeros(nel);                  
    stress = np.zeros(nel);
    strain = np.zeros(nel);
    # % combine du and g then organize displacements by node number [dcomp size: ndf x nnp]
    dcomp = add_d2dcomp(g,du,id,nnp,ndf)
    for i in range(nel):
        Fe[:,i],axial[i],stress[i],strain[i] = truss_forces(dcomp,Ke[:,:,i],Te[:,:,i],ien[:,i],nen,ndf,A[i],E[i])

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # %              REACTIONS               %
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    print(' *******          Assemble Reactions          *******')
    Rcomp = assemble_rxns(Fe,idb,nnp,ndf,nee,ien,nen,nel);
        
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # %       PRINT RESULTS TO SCREEN        %
    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    print('Nodal Displacements')
    strnode = ' node          d1          d2          ' if nsd== 2 else ' node          d1          d2          d3'
    print(strnode)
    for n in range(nnp):
        if nsd == 3:
            print('{:5}  {:10.5}  {:10.5}  {:10.5}\n'.format(n,dcomp[0,n], dcomp[1,n], dcomp[2,n] ))
        elif nsd == 2:
            print('{:5}  {:10.5}  {:10.5}\n'.format(n,dcomp[0,n], dcomp[1,n]))
    print(' ')

    print('Nodal Reactions(N)')
    strreact = ' node          R1          R2          ' if nsd== 2 else ' node          R1          R2          R3'
    print(strreact)
    for n in range(nnp):
        if nsd == 3:
            print('{:5}  {:10.3}  {:10.3}  {10.3}\n'.format(n,Rcomp[:,n]));
        if nsd == 2:
            print('{:5}  {:10.3}  {:10.3}\n'.format(n,Rcomp[0,n], Rcomp[1,n]));
    print(' ')

    print('Element Axial force(N)/stress(MPa)/strain')
    print(' elem       force      stress      strain')
    for i in range(nel):
        print('{:5}  {:10.3}  {:10.3}  {:10.3}\n'.format(i,axial[i],stress[i],strain[i])); 
    print(' ')