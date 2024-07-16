# -*- coding: utf-8 -*-
import pickle
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FuncFormatter
import numpy as np

from cycler import cycler
import pdb

def duplicate_figure(fig):
    obj = pickle.dumps(fig)
    pickle.loads(obj)
    return plt.gcf()
    


def pre_settings():
    """Some plot settings."""
    
    # default_cycler = plt.rcParams['axes.prop_cycle']
    
    
    cycler0 = cycler(color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
                            '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
                            '#bcbd22', '#17becf'])
    # colors = cycler.by_key()['color']
    cycler1 = cycler(linestyle=['-', '--', '-.'])
    
    cycler2 = cycler1 * cycler0
    
    
    # pdb.set_trace()
    plt.rc('axes', prop_cycle=cycler2)
    figsize = (6.5*1.25, 4*1.25)
    
    plt.rcParams['figure.figsize'] = figsize
    # plt.rcParams['figure.dpi'] = 150
    plt.rcParams['figure.dpi'] = 100
    

def get_colors():
    return plt.rcParams["axes.prop_cycle"].by_key()["color"]



    
def sci_format(x, lim):
    return '{:.1e}'.format(x)


def pre_settings_igor():
    
    figsize = (5*1.15, 4*1.15)
    # figsize = (5, 4)
    plt.rcParams['font.family'] = 'arial'
    plt.rcParams['font.size'] = 10
    plt.rcParams['figure.figsize'] = figsize
    plt.rcParams['axes.labelweight'] = 'bold'
    plt.rcParams['axes.titleweight'] = 'bold'
    plt.rcParams['axes.formatter.use_mathtext'] = True
    plt.rcParams['axes.formatter.useoffset'] = False
    plt.rcParams['savefig.dpi'] = 300

    # plt.rcParams['text.usetex'] = True

    # matplotlib.rc('font', weight='bold')
    # matplotlib.rc('axes.formatter', useoffset=False)
    
    # plt.rcParams["font.weight"] = "bold"
    # plt.rcParams["axes.labelweight"] = "bold"
    
def post_settings_igor():
    
    ax = plt.gca()
    formatter = ScalarFormatter()
    formatter.set_powerlimits((-2, 4))
    
    formatter2 = ScalarFormatter()
    formatter2.set_powerlimits((-2, 4))



    plt.grid(visible=True, which='major', alpha=0.4)
    plt.grid(visible=True, which='minor', alpha=0.15)


    # Increase xmax limit to fit in a legend.
    xmin, xmax = ax.get_xlim()
    # ax.xaxis.get_ticklocs(minor=True)
    # ax.yaxis.get_ticklocs(minor=True)
    ax.minorticks_on()

    xtype = ax.get_xscale()
    ytype = ax.get_yscale()
    if xtype == 'linear':
        ax.xaxis.set_major_formatter(formatter,)

    if ytype == 'linear':
        ax.yaxis.set_major_formatter(formatter2,)
        
        
    plt.subplots_adjust(left=0.125,right=0.97, 
                        bottom=0.11, top=0.94, )

    
    
def post_settings():
    """Some plot settings."""
    ax = plt.gca()
    formatter = ScalarFormatter()
    formatter.set_powerlimits((-2, 4))
    
    
    formatter2 = ScalarFormatter()
    formatter2.set_powerlimits((-2, 4))
    
    
    # Activate grid
    plt.grid(visible=True, which='major')
    plt.grid(visible=True, which='minor', alpha=0.25)
    
    # Increase xmax limit to fit in a legend.
    xmin, xmax = ax.get_xlim()
    # ax.xaxis.get_ticklocs(minor=True)
    # ax.yaxis.get_ticklocs(minor=True)
    
    # ax.xaxis.set_major_formatter(labelOnlyBase=False)
    # ax.yaxis.set_major_formatter(labelOnlyBase=False)
    
    ax.minorticks_on()
    
    # Retrieve type of x-scale, either log or linear
    xtype = ax.get_xscale()
    ytype = ax.get_yscale()
    if xtype == 'linear':
        ax.xaxis.set_major_formatter(formatter, )
    if ytype == 'linear':
        ax.yaxis.set_major_formatter(formatter2, )

    # plt.xlim(xmin, xmax * 1.2)
    
    # Set number of tick marks
    # N = 10
    # ax.xaxis.set_major_locator(plt.MaxNLocator(N))
    # ax.xaxis.set_minor_locator(plt.MaxNLocator(N * 4))
    # ax.yaxis.set_major_locator(plt.MaxNLocator(N))
    # ax.yaxis.set_minor_locator(plt.MaxNLocator(N * 4))

def test_plot():
    x = np.linspace(0, 1, 1001)
    y1 = np.sin(2*np.pi*(x + 0.25)) * 1e-3
    y2 = np.sin(2*np.pi*(x + 0.50)) * 1e-3
    y3 = np.sin(2*np.pi*(x + 0.75)) * 1e-3
    y4 = np.sin(2*np.pi*(x + 0.90)) * 1e-3
    y5 = np.sin(2*np.pi*(x + 0.95)) * 1e-3
    x1 = x * 1e-5 + 1e-5
    
    pre_settings_igor()
    plt.figure()
    plt.plot(x1, y1, label='label1')
    plt.plot(x1, y2, label='label2')
    plt.plot(x1, y3, label='label3')
    plt.plot(x1, y4, label='label4')
    plt.plot(x1, y5, label='label5')
    plt.xlabel('X Label (units)')
    plt.ylabel('Y Label (units)')
    # plt.title('Plot title')
    plt.legend(title='Label')
    post_settings_igor()
    # plt.tight_layout()
    
    plt.figure()
    plt.plot(x*1000, y1, label='label1')
    plt.plot(x*1000, y2, label='label2')
    plt.plot(x*1000, y3, label='label3')
    plt.plot(x*1000, y4, label='label4')
    plt.plot(x*1000, y5, label='label5')   
    plt.xlabel('X Label (units)')
    plt.ylabel('Y Label (units)')
    # plt.title('Plot title')        
    plt.legend(title='test title')
    post_settings_igor()
    # plt.tight_layout()    
    
if __name__ == '__main__':
    test_plot()