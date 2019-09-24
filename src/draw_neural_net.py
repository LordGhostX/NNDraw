#!/usr/bin/env python3

"""
Created by @author: craffel
Modified on Sun Jan 15, 2017 by anbrjohn
Remodified on Mon April 08, 2019 by lordghostX

Modifications: 
    -Changed parameters format
	-Changed neurons coloring
"""    

import matplotlib.pyplot as plt

def draw_neural_net(ax, layer_sizes=[1, 2, 1], layer_text=None, colors=["b", "r", "g"], fig_size=[.1, .9, .1, .9]):
	'''
    Draw a neural network cartoon using matplotilb.
    
    :usage:
        >>> fig = plt.figure()
        >>> draw_neural_net(fig.gca(), [3, 5, 5, 2, 1], ["input_1", "input_2", "input_3"])
    
    :parameters:
        - ax : matplotlib.axes.AxesSubplot
            The axes on which to plot the cartoon (get e.g. by plt.gca())
        - layer_sizes : list of int
            List of layer sizes, including input and output dimensionality
        - layer_text : list of str
            List of node annotations in top-down left-right order
		- colors: list of str
			List of colors to paint the input_layer, hidden_layers and output_layer nodes
		- fig_size : list of float
            index 0 : The center of the leftmost node(s) will be placed here
            index 1 : The center of the rightmost node(s) will be placed here
            index 2 : The center of the bottommost node(s) will be placed here
            index 3 : The center of the topmost node(s) will be placed here
    '''
	left, right, bottom, top = fig_size
	n_layers = len(layer_sizes)
	v_spacing = (top - bottom)/float(max(layer_sizes))
	h_spacing = (right - left)/float(len(layer_sizes) - 1)
	ax.axis('off')
	# Nodes
	input_layer = True
	for n, layer_size in enumerate(layer_sizes):
		layer_top = v_spacing*(layer_size - 1)/2. + (top + bottom)/2.
		for m in range(layer_size):
			x = n*h_spacing + left
			y = layer_top - m*v_spacing
			if n == len(layer_sizes) - 1:
				circle = plt.Circle((x,y), v_spacing/4., color=colors[2], ec='k', zorder=4)
			else:
				circle = plt.Circle((x,y), v_spacing/4., color=colors[int(not input_layer)], ec='k', zorder=4)
			ax.add_artist(circle)
			# Node annotations
			if layer_text:
				text = layer_text.pop(0)
				plt.annotate(text, xy=(x, y), zorder=5, ha='center', va='center')
		input_layer = False


    # Edges
	for n, (layer_size_a, layer_size_b) in enumerate(zip(layer_sizes[:-1], layer_sizes[1:])):
		layer_top_a = v_spacing*(layer_size_a - 1)/2. + (top + bottom)/2.
		layer_top_b = v_spacing*(layer_size_b - 1)/2. + (top + bottom)/2.
		for m in range(layer_size_a):
			for o in range(layer_size_b):
				line = plt.Line2D([n*h_spacing + left, (n + 1)*h_spacing + left], [layer_top_a - m*v_spacing, layer_top_b - o*v_spacing], c='k')
				ax.add_artist(line)