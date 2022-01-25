#!/usr/bin/env python3
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter

dfat=pd.read_pickle('KENO//KENO_alltime.pkl')
dfat=dfat['winningNumbers']

def num_evo(iter_NE):
    global NE_dict, NE_list, NEn_dict, last_dicE, WKn_labels
    #KENO numbers
    numRange=list(range(1,81))
    #X-axis values
    xticks = list(range(len(iter_NE)))
    #create plot style
    plt.style.use('seaborn')
    #create dictionary of Counter()'s
    NE_dict = {}
    for tick in xticks:
        ticks = list(range(tick))
        numCount=Counter()
        for draw in iter_NE.iloc[ticks]:
            numCount.update(draw)
        NE_dict[tick] = numCount
    #create dictionary of Y values for each KENO number
    NEn_dict = {}
    for dnum in numRange:
        dnum_Y=[]
        for tick2 in xticks:
            dnum_Y.append(NE_dict[tick2][dnum])
        NEn_dict[dnum]=dnum_Y
    #plot all KENO numbers
    NE_list=list(NE_dict)
    last_dicE=NE_dict[NE_list[-1]]
    # winning numbers
    for WKnum in last_dicE.most_common(20):
        newwnl = []
        tally = 0
        last_n = 0
        for wnumo in NEn_dict[WKnum[0]]:
            if wnumo > last_n:
                last_n = wnumo
                tally += 1
                newwnl.append(tally)
            else:
                tally -= 1
                newwnl.append(tally)
        plt.plot(xticks, newwnl, label=str(WKnum[0]))
    # losing numbers
    for LKnum in last_dicE.most_common()[-20:]:
        newlnl = []
        tally = 0
        last_n = 0
        for lnumo in NEn_dict[LKnum[0]]:
            if lnumo > last_n:
                last_n = lnumo
                tally += 1
                newlnl.append(tally)
            else:
                tally -= 1
                newlnl.append(tally)
        plt.plot(xticks, newlnl, label=str(LKnum[0]))   
    # format graph and print
    plt.xlabel('Number of Games')
    plt.ylabel('Occurances')
    plt.title('Value Counts of KENO Numbers Over Time')
    plt.legend(loc='upper left', ncol=4)
    plt.savefig('Plots//'+iter_NE.name)

# plotx=dfat.tail(10)
# plotx.name='last_10'
# plot20=dfat.iloc[-20:-10]
# plot20.name='last_20'
# plot30=dfat.iloc[-30:-10]
# plot30.name='last_30'
# plot40=dfat.iloc[-40:-10]
# plot40.name='last_40'
# plot50=dfat.iloc[-50:-10]
# plot50.name='last_50'
# plot60=dfat.iloc[-60:-10]
# plot60.name='last_60'
# plot70=dfat.iloc[-70:-10]
# plot70.name='last_70'
# plot80=dfat.iloc[-80:-10]
# plot80.name='last_80'
# plot90=dfat.iloc[-90:-10]
# plot90.name='last_90'
# plot100=dfat.iloc[-100:-10]
# plot100.name='last_100'
# plot_list=[plotx, plot20, plot30, plot40, plot50, plot60, plot70, plot80, plot90, plot100]

# for x,i in enumerate(plot_list):
#     plt.figure(x+1)
#     num_evo(i)
# plt.show()

tempdf = dfat.tail(200)
tempdf.name = 'previous_200'
num_evo(tempdf)
plt.show()