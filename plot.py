import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.patches import Circle
import numpy as np
import Data
def undeformed():
    # Import Data
    data = Data.DATA
    nsd = data['nsd']; ndf = data['ndf']; nen = data['nen']; nel = data['nel']; nnp = data['nnp']
    xn = data['xn']; ien = data['ien']; E = data['E']; A = data['A']; idb = data['idb']
    f = data['f']; g = data['g']
    #Plot the elements
    fig, ax1 = plt.subplots(constrained_layout=True, figsize=(6, 6))
    scale = []
    for i in range(len(xn.T)):
        scale.append((xn.T[i, 0]**2 + xn.T[i, 1]**2)**0.5)
    scale = np.array(scale)
    size = np.max(scale)/15
    for i in range((len(ien.T))):
        nodei = int(ien.T[i, 0])-1
        nodej = int(ien.T[i, 1])-1
        xi = xn.T[nodei, 0]
        zi = xn.T[nodei, 1]
        xj = xn.T[nodej, 0]
        zj = xn.T[nodej, 1]
        theta = np.arctan2((zj - zi), (xj - xi))
        t = A[i]/np.max(A)*size/2
        points = np.array([[xi - np.sin(theta)*t/2, zi + np.cos(theta)*t/2],
                           [xj - np.sin(theta)*t/2, zj + np.cos(theta)*t/2],
                           [xj + np.sin(theta)*t/2, zj - np.cos(theta)*t/2],
                           [xi + np.sin(theta)*t/2, zi - np.cos(theta)*t/2]])
        plt.plot([xi, xj], [zi, zj], 'bo', markersize=0.5)
        polygon = Polygon(points, True, ec='b', fc=(1, 1, 0, 1), lw=0.5)
        ax1.add_artist(polygon)

    for i in range(len(xn.T)):
        if(idb[0, i] == 1 and idb[1, i] == 1):
            if(xn.T[i, 0]>np.min(xn.T[:, 0]) and xn.T[i, 0]<np.max(xn.T[:, 0]) and xn.T[i, 1]>=np.mean(xn.T[:, 1])):
                pointst = np.array([[xn.T[i, 0], xn.T[i, 1]], [xn.T[i, 0] + size/2, xn.T[i, 1]+ size], [xn.T[i, 0] - size/2, xn.T[i, 1]+ size]])
                polygon = Polygon(pointst, True, ec='k', fc='gray', lw=0.5)
                ax1.add_artist(polygon)
            if(xn.T[i, 0]>np.min(xn.T[:, 0]) and xn.T[i, 0]<np.max(xn.T[:, 0]) and xn.T[i, 1]<np.mean(xn.T[:, 1])):
                pointst = np.array([[xn.T[i, 0], xn.T[i, 1]], [xn.T[i, 0] + size/2, xn.T[i, 1]- size], [xn.T[i, 0] - size/2, xn.T[i, 1]- size]])
                polygon = Polygon(pointst, True, ec='k', fc='gray', lw=0.5)
                ax1.add_artist(polygon)
            if(xn.T[i, 0]== np.min(xn.T[:, 0]) or xn.T[i, 0]==np.max(xn.T[:, 0])):
                k = 1 if xn.T[i, 0] == np.max(xn.T[:, 0]) else -1
                pointst = np.array([[xn.T[i, 0], xn.T[i, 1]], [xn.T[i, 0] + k*size, xn.T[i, 1]+ size/2], [xn.T[i, 0] + k*size, xn.T[i, 1] - size/2]])
                polygon = Polygon(pointst, True, ec='k', fc='gray', lw=0.5)
                ax1.add_artist(polygon)
        if(idb[0, i] == 1 and idb[1, i] == 0):
            k = 1 if xn.T[i, 0] == np.max(xn.T[:, 0]) else -1
            pointst = np.array([[xn.T[i, 0], xn.T[i, 1]], [xn.T[i, 0] + k*size, xn.T[i, 1]+ size/2], [xn.T[i, 0] + k*size, xn.T[i, 1] - size/2]])
            polygon = Polygon(pointst, True, ec='k', fc='gray', lw=0.5)
            circle1 = Circle([xn.T[i, 0] + k*size*11/10, xn.T[i, 1]+ size/4], size/10, ec='k', fc='gray')
            circle2 = Circle([xn.T[i, 0] + k*size*11/10, xn.T[i, 1]- size/4], size/10, ec='k', fc='gray')
            ax1.add_artist(polygon)
            ax1.add_artist(circle1)
            ax1.add_artist(circle2)
        if(idb[0, i] == 0 and idb[1, i] == 1):
            k = 1 if xn.T[i, 1] == np.max(xn.T[:, 1]) else -1
            pointst = np.array([[xn.T[i, 0], xn.T[i, 1]], [xn.T[i, 0] + size/2, xn.T[i, 1]+ k*size], [xn.T[i, 0] - size/2, xn.T[i, 1] + k*size]])
            polygon = Polygon(pointst, True, ec='k', fc='gray', lw=0.5)
            circle1 = Circle([xn.T[i, 0] + size/4, xn.T[i, 1]+ k*size*11/10], size/10, ec='k', fc='gray')
            circle2 = Circle([xn.T[i, 0] - size/4, xn.T[i, 1] + k*size*11/10], size/10, ec='k', fc='gray')
            ax1.add_artist(polygon)
            ax1.add_artist(circle1)
            ax1.add_artist(circle2)

        if(f[0, i]!=0 or f[1, i]!=0):
            plt.arrow(xn.T[i, 0], xn.T[i, 1], size*f[0, i]/np.max(np.abs(f.flatten())), size*f[1, i]/np.max(np.abs(f.flatten())), width = size/4)
            plt.text(xn.T[i, 0]+size*f[0, i]/np.max(np.abs(f.flatten())), xn.T[i, 1]+size*f[1, i]/np.max(np.abs(f.flatten())),str(np.round(np.sqrt(f[0, i]**2+f[1, i]**2), 4)))
# width = np.sqrt((size*f[1, i]/np.max(f.flatten())**2)+(size*f[0, i]/np.max(f.flatten()**2)))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlim([np.min(xn.T[:, 0])-size*7, np.max(xn.T[:, 0])+size*7])
    plt.ylim([np.min(xn.T[:, 1])-size*7, np.max(xn.T[:, 1])+size*7])
    plt.axis('off')
    plt.title('Undeformed Shape', size = 16)
    plt.show()

def deformed(scale):
    # Import Data
    data = Data.DATA
    nsd = data['nsd']; ndf = data['ndf']; nen = data['nen']; nel = data['nel']; nnp = data['nnp']
    xn = data['xn']; ien = data['ien']; E = data['E']; A = data['A']; idb = data['idb']
    f = data['f']; g = data['g']; dcomp = data['dcomp']; Rcomp = data['Rcomp']; stress = data['stress']
    scale1 = []
    for i in range(len(xn.T)):
        scale1.append((xn.T[i, 0]**2 + xn.T[i, 1]**2)**0.5)
    scale1 = np.array(scale1)
    size = np.max(scale1)/15
    #Plot the elements
    fig, ax1 = plt.subplots(constrained_layout=True, figsize=(6, 6))
    for i in range((len(ien.T))):
        nodei = int(ien.T[i, 0])-1
        nodej = int(ien.T[i, 1])-1
        xi = xn.T[nodei, 0]
        zi = xn.T[nodei, 1]
        xj = xn.T[nodej, 0]
        zj = xn.T[nodej, 1]
        dxi = xn.T[nodei, 0] + dcomp.T[nodei, 0]*scale
        dzi = xn.T[nodei, 1] + dcomp.T[nodei, 1]*scale
        dxj = xn.T[nodej, 0] + dcomp.T[nodej, 0]*scale
        dzj = xn.T[nodej, 1] + dcomp.T[nodej, 1]*scale
        theta = np.arctan2((zj - zi), (xj - xi))
        t =  A[i]/np.max(A)*size/2
        points = np.array([[xi - np.sin(theta)*t/2, zi + np.cos(theta)*t/2],
                           [xj - np.sin(theta)*t/2, zj + np.cos(theta)*t/2],
                           [xj + np.sin(theta)*t/2, zj - np.cos(theta)*t/2],
                           [xi + np.sin(theta)*t/2, zi - np.cos(theta)*t/2]])
        plt.plot([xi, xj], [zi, zj], 'bo', markersize=0.5)
        points1 = np.array([[dxi - np.sin(theta)*t/2, dzi + np.cos(theta)*t/2],
                           [dxj - np.sin(theta)*t/2, dzj + np.cos(theta)*t/2],
                           [dxj + np.sin(theta)*t/2, dzj - np.cos(theta)*t/2],
                           [dxi + np.sin(theta)*t/2, dzi - np.cos(theta)*t/2]])
        plt.plot([dxi, dxj], [dzi, dzj], 'ro', markersize=0.5)
        polygon = Polygon(points, True, ec='k', fc='y', lw=0.5)
        polygon1 = Polygon(points1, True, ec='k', fc='r', lw=0.5)
        ax1.add_artist(polygon)
        ax1.add_artist(polygon1)
    for i in range(len(xn.T)):
        if(idb[0, i] == 1 and idb[1, i] == 1):
            if(xn.T[i, 0]>np.min(xn.T[:, 0]) and xn.T[i, 0]<np.max(xn.T[:, 0]) and xn.T[i, 1]>=np.mean(xn.T[:, 1])):
                pointst = np.array([[xn.T[i, 0], xn.T[i, 1]], [xn.T[i, 0] + size/2, xn.T[i, 1]+ size], [xn.T[i, 0] - size/2, xn.T[i, 1]+ size]])
                polygon = Polygon(pointst, True, ec='k', fc='gray', lw=0.5)
                ax1.add_artist(polygon)
            if(xn.T[i, 0]>np.min(xn.T[:, 0]) and xn.T[i, 0]<np.max(xn.T[:, 0]) and xn.T[i, 1]<np.mean(xn.T[:, 1])):
                pointst = np.array([[xn.T[i, 0], xn.T[i, 1]], [xn.T[i, 0] + size/2, xn.T[i, 1]- size], [xn.T[i, 0] - size/2, xn.T[i, 1]- size]])
                polygon = Polygon(pointst, True, ec='k', fc='gray', lw=0.5)
                ax1.add_artist(polygon)
            if(xn.T[i, 0]== np.min(xn.T[:, 0]) or xn.T[i, 0]==np.max(xn.T[:, 0])):
                k = 1 if xn.T[i, 0] == np.max(xn.T[:, 0]) else -1
                pointst = np.array([[xn.T[i, 0], xn.T[i, 1]], [xn.T[i, 0] + k*size, xn.T[i, 1]+ size/2], [xn.T[i, 0] + k*size, xn.T[i, 1] - size/2]])
                polygon = Polygon(pointst, True, ec='k', fc='gray', lw=0.5)
                ax1.add_artist(polygon)
        if(idb[0, i] == 1 and idb[1, i] == 0):
            k = 1 if xn.T[i, 0] == np.max(xn.T[:, 0]) else -1
            pointst = np.array([[xn.T[i, 0], xn.T[i, 1]], [xn.T[i, 0] + k*size, xn.T[i, 1]+ size/2], [xn.T[i, 0] + k*size, xn.T[i, 1] - size/2]])
            polygon = Polygon(pointst, True, ec='k', fc='gray', lw=0.5)
            circle1 = Circle([xn.T[i, 0] + k*size*11/10, xn.T[i, 1]+ size/4], size/10, ec='k', fc='gray')
            circle2 = Circle([xn.T[i, 0] + k*size*11/10, xn.T[i, 1]- size/4], size/10, ec='k', fc='gray')
            ax1.add_artist(polygon)
            ax1.add_artist(circle1)
            ax1.add_artist(circle2)
        if(idb[0, i] == 0 and idb[1, i] == 1):
            k = 1 if xn.T[i, 1] == np.max(xn.T[:, 1]) else -1
            pointst = np.array([[xn.T[i, 0], xn.T[i, 1]], [xn.T[i, 0] + size/2, xn.T[i, 1]+ k*size], [xn.T[i, 0] - size/2, xn.T[i, 1] + k*size]])
            polygon = Polygon(pointst, True, ec='k', fc='gray', lw=0.5)
            circle1 = Circle([xn.T[i, 0] + size/4, xn.T[i, 1]+ k*size*11/10], size/10, ec='k', fc='gray')
            circle2 = Circle([xn.T[i, 0] - size/4, xn.T[i, 1] + k*size*11/10], size/10, ec='k', fc='gray')
            ax1.add_artist(polygon)
            ax1.add_artist(circle1)
            ax1.add_artist(circle2)  
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlim([np.min(xn.T[:, 0])-size*7, np.max(xn.T[:, 0])+size*7])
    plt.ylim([np.min(xn.T[:, 1])-size*7, np.max(xn.T[:, 1])+size*7])
    plt.title('Deformed Shape', size = 16)
    plt.axis('off')
    plt.show()

def stress():
    # Import Data
    data = Data.DATA
    nsd = data['nsd']; ndf = data['ndf']; nen = data['nen']; nel = data['nel']; nnp = data['nnp']
    xn = data['xn']; ien = data['ien']; E = data['E']; A = data['A']; idb = data['idb']
    f = data['f']; g = data['g']; dcomp = data['dcomp']; Rcomp = data['Rcomp']; stress = data['stress']
    #Plot the elements
    fig, ax1 = plt.subplots(constrained_layout=True, figsize=(6, 6))
    scale = []
    for i in range(len(xn.T)):
        scale.append((xn.T[i, 0]**2 + xn.T[i, 1]**2)**0.5)
    scale = np.array(scale)
    size = np.max(scale)/15
    for i in range((len(ien.T))):
        nodei = int(ien.T[i, 0])-1
        nodej = int(ien.T[i, 1])-1
        xi = xn.T[nodei, 0]
        zi = xn.T[nodei, 1]
        xj = xn.T[nodej, 0]
        zj = xn.T[nodej, 1]
        theta = np.arctan2((zj - zi), (xj - xi))
        t = A[i]/np.max(A)*size/2
        stres1 = stress[i]/np.max(stress)*size*2
        points = np.array([[xi - np.sin(theta)*t/2, zi + np.cos(theta)*t/2],
                        [xj - np.sin(theta)*t/2, zj + np.cos(theta)*t/2],
                        [xj + np.sin(theta)*t/2, zj - np.cos(theta)*t/2],
                        [xi + np.sin(theta)*t/2, zi - np.cos(theta)*t/2]])
        points1 = np.array([[xi - np.sin(theta)*stres1/2, zi + np.cos(theta)*stres1/2],
                        [xj - np.sin(theta)*stres1/2, zj + np.cos(theta)*stres1/2],
                        [xj + np.sin(theta)*stres1/2, zj - np.cos(theta)*stres1/2],
                        [xi + np.sin(theta)*stres1/2, zi - np.cos(theta)*stres1/2]])
        plt.plot([xi, xj], [zi, zj], 'bo', markersize=0.5)
        polygon = Polygon(points, True, ec='k', fc='w', lw=0.5)
        poly = Polygon(points1, True, ec='r', fc='r' if stress[i]>0 else 'b', lw=0.5, alpha = 0.3)
        plt.text((xi+xj)/2, (zi+zj)/2, str(np.round(stress[i], 3)), color = 'b' if stress[i]>0 else 'r')
        ax1.add_artist(polygon)
        ax1.add_artist(poly)
        plt.gca().set_aspect('equal', adjustable='box')
    plt.xlim([np.min(xn.T[:, 0])-size*7, np.max(xn.T[:, 0])+size*7])
    plt.ylim([np.min(xn.T[:, 1])-size*7, np.max(xn.T[:, 1])+size*7])
    plt.axis('off')
    plt.title('Stress Diagram', size = 16)
    plt.show()