"""
a bunch of functions to build heatmaps. After calling functions, draw plot using:

                                draw_graph()
"""

import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class basic_heatmap():
    def __init__(self, X, row_labels=None, column_labels=None, figsize=(10,7),
                vmin=0, vmax=1, cmap=cm.seismic):
        """
        stores all the initial values in the class and then calls the basic graph.
        """
        self.X = X
        self.row_labels = row_labels
        self.column_labels = column_labels
        self.figsize = figsize
        self.vmin = vmin
        self.vmax = vmax
        self.cmap = cmap
        
        self.setup_graph()
        self.label_axes()
        
    def setup_graph(self):    
        self.fig = plt.figure(figsize=self.figsize)
        # setup first axis. NB the colspan and rowspan will need to be adjusted in 
        # any class extending this graph.
        self.ax = plt.subplot2grid(self.figsize,(0,0),rowspan=10, colspan=7)
        plt.pcolor(self.X, cmap=self.cmap)
    
    def label_axes(self):
        # put the major ticks at the middle of each cell
        self.ax.set_xticks(np.arange(self.X.shape[1])+0.5, minor=False)
        plt.sca(self.ax)
        plt.xticks(rotation=90)
    
        self.ax.set_yticks(np.arange(self.X.shape[0])+0.5, minor=False)

        # create a more natural, table-like display
        self.ax.invert_yaxis()
    
        if self.row_labels and self.X.shape[1] == len(self.row_labels):
            self.ax.set_xticklabels(self.row_labels, minor=False)
        if self.column_labels and self.X.shape[0] == len(self.column_labels):
            self.ax.set_yticklabels(self.column_labels, minor=False)

    def __repr__(self):
        return "%r %r %r %r" % (self.X, self.row_labels, self.column_labels, self.figsize)
    
    def __str__(self):
        if self.row_labels:
            rl = "%s...%s" % (self.row_labels[:3], self.row_labels[-3:])
        else:
            rl = "--none supplied--"
            
        if self.column_labels:
            cl = "%s...%s" % (self.column_labels[:3], self.column_labels[-3:])
        else:
            cl = "--none supplied--"
            
        return "array of shape: %s\nrows: %s\ncolumns %s\nfigsize %s" % (self.X.shape, rl, cl, self.figsize)
       
    def draw_graph(self):
        plt.tight_layout()
        self.fig.show()

class hm_scalebar(basic_heatmap):
    def setup_graph(self):
        self.fig = plt.figure(figsize=self.figsize)
        self.ax = plt.subplot2grid(self.figsize,(0,0), rowspan=self.figsize[0], 
                                    colspan=self.figsize[1] - 1)
        plt.pcolor(self.X, cmap=self.cmap)
        self.scalebar()
        
    def scalebar(self):    
        nrml = mpl.colors.Normalize(vmin=self.vmin, vmax=self.vmax)
        self.ax2 = plt.subplot2grid(self.figsize,(0,self.figsize[1] - 1), 
                                    rowspan=5, colspan=1)
        self.cb1 = mpl.colorbar.ColorbarBase(self.ax2, cmap=self.cmap, norm=nrml, 
                                            orientation='vertical')
        