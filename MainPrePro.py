
import numpy as np
import ipywidgets as widgets
from ipywidgets import Layout
import Data
def prevals():
    minp = [2, 2, 2, 3, 4]
    constraints = []
    flag = np.array([1, 0, 0, 0, 1, 0, 0, 0, 0, 0])
    props = np.array([[0, 29500, 29500, 0.3, 0.3, 29500 / (2 * (1 + 0.3))]])
    nodes2 =np.array([[1, 0, 3, 1, 1], [2, 4, 3, 1, 1], [3, 0, 0, 1, 1], [4, 4, 0, 1, 1]])
    ien2 = np.array([[1, 3, 4, 200, 400], [2, 1, 4, 200, 150], [3, 4, 2, 200, 200]])
    return minp, nodes2, ien2
class MainPrePro:
    def prevals(self, analysis, dims):
        if analysis == 'truss' and dims == 2:
            minp = [2, 2, 2, 3, 4]
            nodes =np.array([[1, 0, 3, 1, 1, 0, 0, 0, 0], [2, 4, 3, 1, 1, 0, 0, 0, 0], [3, 0, 0, 1, 1, 0, 0, 0, 0], [4, 4, 0, 0, 0, 20.71*10**3, -77.27*10**3, 0, 0]])
            ien = np.array([[1, 3, 4, 200, 400], [2, 1, 4, 200, 150], [3, 4, 2, 200, 200]])

        if analysis == 'truss' and dims == 3:
            minp = [3, 3, 2, 3, 4]
            nodes = np.array([[1, 0, 0, 6, 0, 0, 0, 0, -2.5, -4, 0,0, 0], [2, -1, -3, 0, 1, 1, 1, 0, 0, 0, 0,0, 0], [3, 2, 0, 0, 1, 1, 1 , 0, 0, 0, 0,0, 0], [4, -1, 3, 0, 1, 1, 1 , 0, 0, 0, 0,0, 0]])
            ien = np.array([[1, 1, 2, 200, 1000], [2, 1, 3, 200, 1000], [3, 1, 4, 200, 1000]])
        return minp, nodes, ien
    def Mesh(self, minp):
        self.meshtitle = widgets.Label( value = 'Mesh')
        self.meshtext = ['nsd', 'ndf', 'nen', 'nel', 'nnp']
        self.mlabel = widgets.HBox([widgets.Label(value=self.meshtext[j], layout = widgets.Layout(width='55px')) for j in range(len(self.meshtext)-2)])
        self.minp1 = widgets.HBox([widgets.IntText(value=self.minp[j], layout = widgets.Layout(width='55px'), disabled=True) for j in range(len(self.minp)-2)])
        self.msubmit = widgets.Button(description="Submit", layout= widgets.Layout(border = 'solid 1px black'))
        self.rmesh = widgets.VBox([self.mlabel, widgets.HBox([self.minp1])])
        return self.rmesh, self.msubmit
    
    def add_node(self, b):
        New_row = widgets.HBox(self.nitems[len(self.nitems)-1])
        self.noder0.children = self.noder0.children + (New_row,)
    def del_node(self, b):
        del_row = list(self.noder0.children)
        del_row = del_row[:-1]
        self.noder0.children = tuple(del_row)
    
    def nodes_widget(self, nodes, analysis, dims):
        self.nodeTitle = widgets.Label(value='Nodes')
        if analysis == 'truss' and dims == 2:
            self.nodetext = ['Node#','x','y', 'dofx', 'dofy', 'Fx', 'Fy', 'gx', 'gy']
        elif analysis == 'truss' and dims == 3:
            self.nodetext = ['Node#','x','y', 'z', 'dofx', 'dofy', 'dofz', 'Fx', 'Fy', 'Fz', 'gx', 'gy', 'gz']
        self.nodes = nodes
        self.node = [[] for i in range(len(self.nodes))]
        self.nitems = [[] for i in range(len(self.nodes))]
        ADDNODE = widgets.Button(description="Add Node", layout= widgets.Layout(border = 'solid 1px black'))
        DELNODE = widgets.Button(description="Remove Node", layout= widgets.Layout(border = 'solid 1px black'))
        self.nlabel= widgets.HBox([widgets.Label(value=self.nodetext[j], layout = widgets.Layout(width='57px')) for j in range(len(self.nodetext))])
        for i in range(len(self.nodes)):
            if(i<len(self.nodes)):
                for j in range(len(self.nodetext)):
                    self.nitems[i].append(widgets.FloatText(value=self.nodes[i, j], layout = widgets.Layout(width='57px')))
                self.node[i] = widgets.HBox(self.nitems[i])
        self.noder0 = widgets.VBox([self.node[j] for j in range(len(self.nodes))])
        self.brow = widgets.HBox([ADDNODE, DELNODE])
        self.rnode = widgets.VBox([self.nodeTitle, self.nlabel, self.noder0, self.brow], layout= widgets.Layout(border = 'solid 1px black'))
        ADDNODE.on_click(self.add_node)
        DELNODE.on_click(self.del_node)
        self.rnode
        return self.rnode, ADDNODE, DELNODE

    def elems_widget(self, ien):
        self.ienTitle = widgets.Label(value='Elements')
        self.ientext = ['Elem#','Node i','Node j','E(Gpa)', 'A(mm^2)']
        self.ien = ien
        self.ien1 = [[] for i in range(len(self.ien))]
        self.Citems = [[] for i in range(len(self.ien))]
        ADDien = widgets.Button(description="Add Element", layout= widgets.Layout(border = 'solid 1px black'))
        DELien = widgets.Button(description="Remove Element", layout= widgets.Layout(border = 'solid 1px black'))
        self.nlabel= widgets.HBox([widgets.Label(value=self.ientext[j], layout = widgets.Layout(width='57px')) for j in range(len(self.ientext))])
        for i in range(len(self.ien)):
            if(i<len(self.ien)):
                for j in range(len(self.ientext)):
                    self.Citems[i].append(widgets.FloatText(value=self.ien[i, j], layout = widgets.Layout(width='57px')))
                self.ien1[i] = widgets.HBox(self.Citems[i])
        self.ien1r0 = widgets.VBox([self.ien1[j] for j in range(len(self.ien))])
        self.brow = widgets.HBox([ADDien, DELien])
        self.rien1 = widgets.VBox([self.ienTitle, self.nlabel, self.ien1r0, self.brow], layout= widgets.Layout(border = 'solid 1px black'))
        ADDien.on_click(self.add_ien)
        DELien.on_click(self.del_ien)
        self.rien1
        return self.rien1, ADDien

    def add_ien(self, b):
        New_row = widgets.HBox(self.Citems[len(self.Citems)-1])
        self.ien1r0.children = self.ien1r0.children + (New_row,)

    def del_ien(self, b):
        del_row = list(self.ien1r0.children)
        del_row = del_row[:-1]
        self.ien1r0.children = tuple(del_row)

    def fsubmit(self, b):
        self.xn = np.zeros((self.dims, len(self.noder0.children)))
        self.idb = np.zeros((self.dims, len(self.noder0.children)))
        self.f = np.zeros((self.dims, len(self.noder0.children)))
        self.g = np.zeros((self.dims, len(self.noder0.children)))
        for j in range(len(self.noder0.children)):
            for i in range(self.dims):
                self.xn[i, j] = self.noder0.children[j].children[i+1].value
                self.idb[i, j] = self.noder0.children[j].children[i+1+self.dims].value
                self.f[i, j] = self.noder0.children[j].children[i+1+2*self.dims].value
                self.g[i, j] = self.noder0.children[j].children[i+1+3*self.dims].value
        self.ien = np.zeros((2, len(self.ien1r0.children)))
        self.A = np.zeros(len(self.ien1r0.children))
        self.E = np.zeros(len(self.ien1r0.children))
        for j in range(len(self.ien1r0.children)):
            for i in range(2):
                self.ien[i, j] = self.ien1r0.children[j].children[i+1].value
            self.E[j] = self.ien1r0.children[j].children[3].value
            self.A[j] = self.ien1r0.children[j].children[4].value
        self.nsd = self.dims
        self.ndf = self.minp[1]
        self.nen = self.minp[2]

        Data.DATA['xn'] = self.xn
        Data.DATA['idb'] = self.idb
        Data.DATA['ien'] = self.ien
        Data.DATA['E'] = self.E
        Data.DATA['A'] = self.A
        Data.DATA['f'] = self.f
        Data.DATA['g'] = self.g
        Data.DATA['nsd'] = self.nsd
        Data.DATA['ndf'] = self.ndf
        Data.DATA['nen'] = self.nen
        Data.DATA['nel'] = len(self.ien1r0.children)
        Data.DATA['nnp'] = len(self.noder0.children)
        
    def run(self, analysis, dims):
        self.minp, self.nodes, self.ien = self.prevals(analysis, dims)
        self.analysis = analysis; self.dims = dims
        self.rnode, self.ADDNODE, self.DELNODE = self.nodes_widget(self.nodes, self.analysis, self.dims)
        self.rien1, self.ADDNODE = self.elems_widget(self.ien)
        self.rmesh, self.msubmit = self.Mesh(self.minp)
        self.Submit = widgets.Button(description = 'Submit')
        self.page = widgets.VBox([self.rmesh, self.rnode, self.rien1, self.Submit])
        self.Submit.on_click(self.fsubmit)
        return self.page


    