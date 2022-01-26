#!/usr/bin/env python3
import os
if os.name == 'posix':
    os.system("printf '\e[8;30;86t'")    
else:
    os.system('mode con: cols=122 lines=30')    
print('\n Welcome to the KENO predicter.')
print('\n Importing libraries...')
import pandas as pd
import time
import numpy as np
import datetime
import requests
from datetime import date
pd.options.mode.chained_assignment=None

print(' Loading current datasets...')
dfat=pd.read_pickle('KENO//KENO_alltime.pkl')
dfpred=pd.read_pickle('KENO//dfpred.pkl')
    
print(' Creating global variables...')
initpred_cols=['drawNumber', 'prediction', 'previousGameN', 'predictionType', 'totalSpots']
pred_typesL=['N-N','N-N/2','N-N/3','N-N/4','N/maxt+N/mina','top1td','top1td-N/3','top2td','top2td-N/3','top3td','top3td-N/3']
predX_typesL=['xN-N', 'xN-N/2', 'xN-N/3', 'xN-N/4', 'xN/maxt+N/mina', 'xtop1td', 'xtop1td-N/3', 'xtop2td', 'xtop2td-N/3', 'xtop3td', 'xtop3td-N/3']

def keno_update(start_d, end_d):
    global dfat, dfnvc, dfatX1, dfatX2, dfatX3, dfatX4, dfatX5, dfatX6, dfatX7, dfatX8, dfatX9, dfatX10, dfatX11, dfatX12, dfatX13, dfatX14, dfatX15, dfatX16, dfatX17, dfatX18, dfatX19, dfatX20, dfatXCL
    for i in pd.date_range(start=start_d,end=end_d):
        r=requests.get('https://www.masslottery.com/rest/keno/getDrawsByDateRange?startDate='+str(i)+'&endDate='+str(i))
        i_daystr=str(i).split(' ')[0]
        print(' Getting '+str(i_daystr)+'...')
        rj=r.json()
        rj=rj['draws']
        rjdf=pd.DataFrame(data=rj)
        fir_l=[]
        sec_l=[]
        thi_l=[]
        fou_l=[]
        fif_l=[]
        six_l=[]
        sev_l=[]
        eig_l=[]
        nin_l=[]
        ten_l=[]
        ele_l=[]
        twe_l=[]
        tht_l=[]
        frt_l=[]
        fft_l=[]
        sxt_l=[]
        svt_l=[]
        eit_l=[]
        nnt_l=[]
        twt_l=[]
        for x,i in enumerate(rjdf['winningNumbers']):
            fir_l.append(rjdf['winningNumbers'][x][0])
            sec_l.append(rjdf['winningNumbers'][x][1])
            thi_l.append(rjdf['winningNumbers'][x][2])
            fou_l.append(rjdf['winningNumbers'][x][3])
            fif_l.append(rjdf['winningNumbers'][x][4])
            six_l.append(rjdf['winningNumbers'][x][5])
            sev_l.append(rjdf['winningNumbers'][x][6])
            eig_l.append(rjdf['winningNumbers'][x][7])
            nin_l.append(rjdf['winningNumbers'][x][8])
            ten_l.append(rjdf['winningNumbers'][x][9])
            ele_l.append(rjdf['winningNumbers'][x][10])
            twe_l.append(rjdf['winningNumbers'][x][11])
            tht_l.append(rjdf['winningNumbers'][x][12])
            frt_l.append(rjdf['winningNumbers'][x][13])
            fft_l.append(rjdf['winningNumbers'][x][14])
            sxt_l.append(rjdf['winningNumbers'][x][15])
            svt_l.append(rjdf['winningNumbers'][x][16])
            eit_l.append(rjdf['winningNumbers'][x][17])
            nnt_l.append(rjdf['winningNumbers'][x][18])
            twt_l.append(rjdf['winningNumbers'][x][19])            
        rjdf['first']=fir_l
        rjdf['second']=sec_l
        rjdf['third']=thi_l
        rjdf['fourth']=fou_l
        rjdf['fifth']=fif_l
        rjdf['sixth']=six_l
        rjdf['seventh']=sev_l
        rjdf['eighth']=eig_l
        rjdf['ninth']=nin_l
        rjdf['tenth']=ten_l
        rjdf['eleventh']=ele_l
        rjdf['twelfth']=twe_l
        rjdf['thirteenth']=tht_l
        rjdf['fourteenth']=frt_l
        rjdf['fifteenth']=fft_l
        rjdf['sixteenth']=sxt_l
        rjdf['seventeenth']=svt_l
        rjdf['eighteenth']=eit_l
        rjdf['nineteenth']=nnt_l
        rjdf['twentieth']=twt_l
        rjn1=rjdf[['drawNumber','drawDate','winningNumbers','first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth','thirteenth','fourteenth','fifteenth','sixteenth','seventeenth','eighteenth','nineteenth','twentieth','bonus']]
        rjn1.reset_index(inplace=True,drop=True)
        if len(rjn1)==300:
            df22=pd.read_csv('KENO//2022.csv')
            if (len(df22[df22['drawDate']==rjn1['drawDate'].iloc[0]])==0):
                rjn1.to_csv('KENO//'+str(date.today().year)+'.csv',mode='a')
        dfat=pd.concat([dfat,rjn1])
    print(' Updating datasets...')
    dfat.reset_index(drop=True,inplace=True)
    dfatX1=dfat['first'].value_counts()
    dfatX2=dfat['second'].value_counts()
    dfatX3=dfat['third'].value_counts()
    dfatX4=dfat['fourth'].value_counts()
    dfatX5=dfat['fifth'].value_counts()
    dfatX6=dfat['sixth'].value_counts()
    dfatX7=dfat['seventh'].value_counts()
    dfatX8=dfat['eighth'].value_counts()
    dfatX9=dfat['ninth'].value_counts()
    dfatX10=dfat['tenth'].value_counts()
    dfatX11=dfat['eleventh'].value_counts()
    dfatX12=dfat['twelfth'].value_counts()
    dfatX13=dfat['thirteenth'].value_counts()
    dfatX14=dfat['fourteenth'].value_counts()
    dfatX15=dfat['fifteenth'].value_counts()
    dfatX16=dfat['sixteenth'].value_counts()
    dfatX17=dfat['seventeenth'].value_counts()
    dfatX18=dfat['eighteenth'].value_counts()
    dfatX19=dfat['nineteenth'].value_counts()
    dfatX20=dfat['twentieth'].value_counts()
    dfatXCL=[dfatX1, dfatX2, dfatX3, dfatX4, dfatX5, dfatX6, dfatX7, dfatX8, dfatX9, dfatX10, dfatX11, dfatX12, dfatX13, dfatX14, dfatX15, dfatX16, dfatX17, dfatX18, dfatX19, dfatX20]
    dfnat=sum(dfatXCL)
    dfnvc=pd.DataFrame(columns=['Occurances'],data=dfnat)
    dfnvc.sort_values('Occurances', ascending=False, inplace=True)
    dfnvc['Normalized']=(dfnvc['Occurances']-dfnvc['Occurances'].mean())/dfnvc['Occurances'].std()
    dfnvc['Normalized/N.max()']=dfnvc['Normalized']/dfnvc['Normalized'].max()
    dfnvc['Normalized/N.min()']=dfnvc['Normalized']/dfnvc['Normalized'].min()       

def load_years():
    global df93,df94,df95,df96,df97,df98,df99,df00,df01,df02,df03,df04,df05,df06,df07,df08,df09,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19,df20
    print('\n Importing yearly datasets...')
    df93=pd.read_csv('KENO//1993.csv')
    df94=pd.read_csv('KENO//1994.csv')
    df95=pd.read_csv('KENO//1995.csv')
    df96=pd.read_csv('KENO//1996.csv')
    df97=pd.read_csv('KENO//1997.csv')
    df98=pd.read_csv('KENO//1998.csv')
    df99=pd.read_csv('KENO//1999.csv')
    df00=pd.read_csv('KENO//2000.csv')
    df01=pd.read_csv('KENO//2001.csv')
    df02=pd.read_csv('KENO//2002.csv')
    df03=pd.read_csv('KENO//2003.csv')
    df04=pd.read_csv('KENO//2004.csv')
    df05=pd.read_csv('KENO//2005.csv')
    df06=pd.read_csv('KENO//2006.csv')
    df07=pd.read_csv('KENO//2007.csv')
    df08=pd.read_csv('KENO//2008.csv')
    df09=pd.read_csv('KENO//2009.csv')
    df10=pd.read_csv('KENO//2010.csv')
    df11=pd.read_csv('KENO//2011.csv')
    df12=pd.read_csv('KENO//2012.csv')
    df13=pd.read_csv('KENO//2013.csv')
    df14=pd.read_csv('KENO//2014.csv')
    df15=pd.read_csv('KENO//2015.csv')
    df16=pd.read_csv('KENO//2016.csv')
    df17=pd.read_csv('KENO//2017.csv')
    df18=pd.read_csv('KENO//2018.csv')
    df19=pd.read_csv('KENO//2019.csv')
    df20=pd.read_csv('KENO//2020.csv')
    print('\n Datasets successfully imported.')

def start_update():
    global dfat 
    today_d=str(date.today()) 
    latest_d=dfat['drawDate'].iloc[-1]
    if today_d == latest_d:
        if 0<len(dfat[dfat['drawDate']==today_d])<300:
            dfat=dfat[dfat['drawDate']!=today_d]
            keno_update(today_d,today_d)
        else:
            dfat=dfat[dfat['drawDate']!=latest_d]
            keno_update(latest_d,latest_d)
    if today_d > latest_d:
        try:
            dfat=dfat[dfat['drawDate']!=latest_d]
            keno_update(latest_d,today_d)
        except:
            dfat=dfat[dfat['drawDate']!=latest_d]
            keno_update(latest_d,latest_d)

def draw_pred(c_ch, num_p):
    global dfpred
    pred_draw_num=dfat['drawNumber'].iloc[-1]
    dftd=dfat.tail(c_ch)
    dftdX1t=dftd['first'].value_counts()
    dftdX1=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX1t.index:
        dftdX1.loc[dind,'Occurances']=dftdX1t[dind]
    dftdX2t=dftd['second'].value_counts()
    dftdX2=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX2t.index:
        dftdX2.loc[dind,'Occurances']=dftdX2t[dind]
    dftdX3t=dftd['third'].value_counts()
    dftdX3=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX3t.index:
        dftdX3.loc[dind,'Occurances']=dftdX3t[dind]
    dftdX4t=dftd['fourth'].value_counts()
    dftdX4=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX4t.index:
        dftdX4.loc[dind,'Occurances']=dftdX4t[dind]
    dftdX5t=dftd['fifth'].value_counts()
    dftdX5=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX5t.index:
        dftdX5.loc[dind,'Occurances']=dftdX5t[dind]
    dftdX6t=dftd['sixth'].value_counts()
    dftdX6=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX6t.index:
        dftdX6.loc[dind,'Occurances']=dftdX6t[dind]
    dftdX7t=dftd['seventh'].value_counts()
    dftdX7=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX7t.index:
        dftdX7.loc[dind,'Occurances']=dftdX7t[dind]
    dftdX8t=dftd['eighth'].value_counts()
    dftdX8=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX8t.index:
        dftdX8.loc[dind,'Occurances']=dftdX8t[dind]
    dftdX9t=dftd['ninth'].value_counts()
    dftdX9=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX9t.index:
        dftdX9.loc[dind,'Occurances']=dftdX9t[dind]
    dftdX10t=dftd['tenth'].value_counts()
    dftdX10=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX10t.index:
        dftdX10.loc[dind,'Occurances']=dftdX10t[dind]
    dftdX11t=dftd['eleventh'].value_counts()
    dftdX11=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX11t.index:
        dftdX11.loc[dind,'Occurances']=dftdX11t[dind]
    dftdX12t=dftd['twelfth'].value_counts()
    dftdX12=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX12t.index:
        dftdX12.loc[dind,'Occurances']=dftdX12t[dind]
    dftdX13t=dftd['thirteenth'].value_counts()
    dftdX13=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX13t.index:
        dftdX13.loc[dind,'Occurances']=dftdX13t[dind]
    dftdX14t=dftd['fourteenth'].value_counts()
    dftdX14=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX14t.index:
        dftdX14.loc[dind,'Occurances']=dftdX14t[dind]
    dftdX15t=dftd['fifteenth'].value_counts()
    dftdX15=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX15t.index:
        dftdX15.loc[dind,'Occurances']=dftdX15t[dind]
    dftdX16t=dftd['sixteenth'].value_counts()
    dftdX16=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX16t.index:
        dftdX16.loc[dind,'Occurances']=dftdX16t[dind]
    dftdX17t=dftd['seventeenth'].value_counts()
    dftdX17=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX17t.index:
        dftdX17.loc[dind,'Occurances']=dftdX17t[dind]
    dftdX18t=dftd['eighteenth'].value_counts()
    dftdX18=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX18t.index:
        dftdX18.loc[dind,'Occurances']=dftdX18t[dind]
    dftdX19t=dftd['nineteenth'].value_counts()
    dftdX19=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX19t.index:
        dftdX19.loc[dind,'Occurances']=dftdX19t[dind]
    dftdX20t=dftd['twentieth'].value_counts()
    dftdX20=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX20t.index:
        dftdX20.loc[dind,'Occurances']=dftdX20t[dind]
    dftdXCL=[dftdX1, dftdX2, dftdX3, dftdX4, dftdX5, dftdX6, dftdX7, dftdX8, dftdX9, dftdX10, dftdX11, dftdX12, dftdX13, dftdX14, dftdX15, dftdX16, dftdX17, dftdX18, dftdX19, dftdX20]

    dfntvc=sum(dftdXCL)
    dfntvc.sort_values('Occurances', ascending=False, inplace=True)
    dfntvc['Normalized']=(dfntvc['Occurances']-dfntvc['Occurances'].mean())/dfntvc['Occurances'].std()
    dfntvc['Normalized/N.max()']=dfntvc['Normalized']/dfntvc['Normalized'].max()
    dfntvc['Normalized/N.min()']=dfntvc['Normalized']/dfntvc['Normalized'].min()
    dfntvc1=dfntvc.copy()
    dfntvc1.iloc[0]=dfntvc1['Occurances'].mean()
    dfntvc1['Normalized']=(dfntvc1['Occurances']-dfntvc1['Occurances'].mean())/dfntvc1['Occurances'].std()
    dfntvc1['Normalized/N.max()']=dfntvc1['Normalized']/dfntvc1['Normalized'].max()
    dfntvc1['Normalized/N.min()']=dfntvc1['Normalized']/dfntvc1['Normalized'].min()
    dfntvc2=dfntvc.copy()
    dfntvc2.iloc[:2]=dfntvc2['Occurances'].mean()
    dfntvc2['Normalized']=(dfntvc2['Occurances']-dfntvc2['Occurances'].mean())/dfntvc2['Occurances'].std()
    dfntvc2['Normalized/N.max()']=dfntvc2['Normalized']/dfntvc2['Normalized'].max()
    dfntvc2['Normalized/N.min()']=dfntvc2['Normalized']/dfntvc2['Normalized'].min()
    dfntvc3=dfntvc.copy()
    dfntvc3.iloc[:3]=dfntvc3['Occurances'].mean()
    dfntvc3['Normalized']=(dfntvc3['Occurances']-dfntvc3['Occurances'].mean())/dfntvc3['Occurances'].std()
    dfntvc3['Normalized/N.max()']=dfntvc3['Normalized']/dfntvc3['Normalized'].max()
    dfntvc3['Normalized/N.min()']=dfntvc3['Normalized']/dfntvc3['Normalized'].min()

    tdat_p=pd.DataFrame()
    tdat_p['N.Total']=dfntvc['Normalized']-dfnvc['Normalized']
    tdat_p['N.td-N/2.at']=dfntvc['Normalized']-(dfnvc['Normalized']/2)
    tdat_p['N.td-N/3.at']=dfntvc['Normalized']-(dfnvc['Normalized']/3)
    tdat_p['N.td-N/4.at']=dfntvc['Normalized']-(dfnvc['Normalized']/4)
    tdat_p['N/max.td+N/min.at']=dfntvc['Normalized/N.max()']/2+(dfnvc['Normalized/N.min()'])/3
    tdat_p['top1td']=dfntvc1['Normalized']-(dfnvc['Normalized'])
    tdat_p['top1td-N/3']=dfntvc1['Normalized']-(dfnvc['Normalized']/3)
    tdat_p['top2td']=dfntvc2['Normalized']-(dfnvc['Normalized'])
    tdat_p['top2td-N/3']=dfntvc2['Normalized']-(dfnvc['Normalized']/3)
    tdat_p['top3td']=dfntvc3['Normalized']-(dfnvc['Normalized'])
    tdat_p['top3td-N/3']=dfntvc3['Normalized']-(dfnvc['Normalized']/3)
    tdat_p=tdat_p.sort_values(by=['N.Total'], ascending=False)                            
    pred_list=[]
    for i in tdat_p.head(num_p).index:
        pred_list.append(i)   
    tdat_p=tdat_p.sort_values(by=['N.td-N/2.at'], ascending=False)
    pred_list2=[]
    for j in tdat_p.head(num_p).index:
        pred_list2.append(j)
    tdat_p=tdat_p.sort_values(by=['N.td-N/3.at'], ascending=False)
    pred_list3=[]
    for j in tdat_p.head(num_p).index:
        pred_list3.append(j)
    tdat_p=tdat_p.sort_values(by=['N.td-N/4.at'], ascending=False)
    pred_list4=[]
    for j in tdat_p.head(num_p).index:
        pred_list4.append(j)
    tdat_p=tdat_p.sort_values(by=['N/max.td+N/min.at'], ascending=False)
    pred_list5=[]
    for j in tdat_p.head(num_p).index:
        pred_list5.append(j)        
    tdat_p=tdat_p.sort_values(by=['top1td'], ascending=False)                            
    pred_list6=[]
    for i in tdat_p.head(num_p).index:
        pred_list6.append(i)   
    tdat_p=tdat_p.sort_values(by=['top1td-N/3'], ascending=False)                            
    pred_list7=[]
    for i in tdat_p.head(num_p).index:
        pred_list7.append(i)   
    tdat_p=tdat_p.sort_values(by=['top2td'], ascending=False)                            
    pred_list8=[]
    for i in tdat_p.head(num_p).index:
        pred_list8.append(i)   
    tdat_p=tdat_p.sort_values(by=['top2td-N/3'], ascending=False)                            
    pred_list9=[]
    for i in tdat_p.head(num_p).index:
        pred_list9.append(i)   
    tdat_p=tdat_p.sort_values(by=['top3td'], ascending=False)                            
    pred_list10=[]
    for i in tdat_p.head(num_p).index:
        pred_list10.append(i)   
    tdat_p=tdat_p.sort_values(by=['top3td-N/3'], ascending=False)                            
    pred_list11=[]
    for i in tdat_p.head(num_p).index:
        pred_list11.append(i)
    pred1row=[pred_draw_num,pred_list,c_ch,'N-N',num_p]
    pred2row=[pred_draw_num,pred_list2,c_ch,'N-N/2',num_p]
    pred3row=[pred_draw_num,pred_list3,c_ch,'N-N/3',num_p]
    pred4row=[pred_draw_num,pred_list4,c_ch,'N-N/4',num_p]
    pred5row=[pred_draw_num,pred_list5,c_ch,'N/maxt+N/mina',num_p]
    pred6row=[pred_draw_num,pred_list6,c_ch,'top1td',num_p]
    pred7row=[pred_draw_num,pred_list7,c_ch,'top1td-N/3',num_p]
    pred8row=[pred_draw_num,pred_list8,c_ch,'top2td',num_p]
    pred9row=[pred_draw_num,pred_list9,c_ch,'top2td-N/3',num_p]
    pred10row=[pred_draw_num,pred_list10,c_ch,'top3td',num_p]
    pred11row=[pred_draw_num,pred_list11,c_ch,'top3td-N/3',num_p]
    temp_dfpred=pd.DataFrame([pred1row,pred2row,pred3row,pred4row,pred5row, pred6row, pred7row, pred8row, pred9row, pred10row, pred11row], columns=initpred_cols)
    
    dfpred=dfpred.append(temp_dfpred)
    dfpred.reset_index(drop=True,inplace=True)
    
def draw_predX(c_chX,num_pX):
    global dfpred
    pred_draw_num=dfat['drawNumber'].iloc[-1]
    dftd=dfat.tail(c_chX)
    dftdX1t=dftd['first'].value_counts()
    dftdX1=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX1t.index:
        dftdX1.loc[dind,'Occurances']=dftdX1t[dind]
    dftdX2t=dftd['second'].value_counts()
    dftdX2=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX2t.index:
        dftdX2.loc[dind,'Occurances']=dftdX2t[dind]
    dftdX3t=dftd['third'].value_counts()
    dftdX3=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX3t.index:
        dftdX3.loc[dind,'Occurances']=dftdX3t[dind]
    dftdX4t=dftd['fourth'].value_counts()
    dftdX4=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX4t.index:
        dftdX4.loc[dind,'Occurances']=dftdX4t[dind]
    dftdX5t=dftd['fifth'].value_counts()
    dftdX5=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX5t.index:
        dftdX5.loc[dind,'Occurances']=dftdX5t[dind]
    dftdX6t=dftd['sixth'].value_counts()
    dftdX6=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX6t.index:
        dftdX6.loc[dind,'Occurances']=dftdX6t[dind]
    dftdX7t=dftd['seventh'].value_counts()
    dftdX7=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX7t.index:
        dftdX7.loc[dind,'Occurances']=dftdX7t[dind]
    dftdX8t=dftd['eighth'].value_counts()
    dftdX8=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX8t.index:
        dftdX8.loc[dind,'Occurances']=dftdX8t[dind]
    dftdX9t=dftd['ninth'].value_counts()
    dftdX9=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX9t.index:
        dftdX9.loc[dind,'Occurances']=dftdX9t[dind]
    dftdX10t=dftd['tenth'].value_counts()
    dftdX10=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX10t.index:
        dftdX10.loc[dind,'Occurances']=dftdX10t[dind]
    dftdX11t=dftd['eleventh'].value_counts()
    dftdX11=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX11t.index:
        dftdX11.loc[dind,'Occurances']=dftdX11t[dind]
    dftdX12t=dftd['twelfth'].value_counts()
    dftdX12=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX12t.index:
        dftdX12.loc[dind,'Occurances']=dftdX12t[dind]
    dftdX13t=dftd['thirteenth'].value_counts()
    dftdX13=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX13t.index:
        dftdX13.loc[dind,'Occurances']=dftdX13t[dind]
    dftdX14t=dftd['fourteenth'].value_counts()
    dftdX14=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX14t.index:
        dftdX14.loc[dind,'Occurances']=dftdX14t[dind]
    dftdX15t=dftd['fifteenth'].value_counts()
    dftdX15=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX15t.index:
        dftdX15.loc[dind,'Occurances']=dftdX15t[dind]
    dftdX16t=dftd['sixteenth'].value_counts()
    dftdX16=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX16t.index:
        dftdX16.loc[dind,'Occurances']=dftdX16t[dind]
    dftdX17t=dftd['seventeenth'].value_counts()
    dftdX17=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX17t.index:
        dftdX17.loc[dind,'Occurances']=dftdX17t[dind]
    dftdX18t=dftd['eighteenth'].value_counts()
    dftdX18=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX18t.index:
        dftdX18.loc[dind,'Occurances']=dftdX18t[dind]
    dftdX19t=dftd['nineteenth'].value_counts()
    dftdX19=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX19t.index:
        dftdX19.loc[dind,'Occurances']=dftdX19t[dind]
    dftdX20t=dftd['twentieth'].value_counts()
    dftdX20=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX20t.index:
        dftdX20.loc[dind,'Occurances']=dftdX20t[dind]
    dftdXCL=[dftdX1, dftdX2, dftdX3, dftdX4, dftdX5, dftdX6, dftdX7, dftdX8, dftdX9, dftdX10, dftdX11, dftdX12, dftdX13, dftdX14, dftdX15, dftdX16, dftdX17, dftdX18, dftdX19, dftdX20]
    splX=np.linspace(0,20,num_pX+1,dtype=int)
    dfatXD={}
    dftdXD={}
    dftd1XD={}
    dftd2XD={}
    dftd3XD={}
    for spli in range(len(splX)):
        if splX[spli] != splX[-1]:
            dfatXDt=pd.DataFrame(columns=['Occurances'],index=dfnvc.index).fillna(0)
            dfatXDtd=sum(dfatXCL[splX[spli]:splX[spli+1]])
            for dind in dfatXDtd.index:
                dfatXDt.loc[dind,'Occurances']=dfatXDtd[dind]
            dfatXDt['Normalized']=(dfatXDt['Occurances']-dfatXDt['Occurances'].mean())/dfatXDt['Occurances'].std()
            dfatXDt['Normalized/N.max()']=dfatXDt['Normalized']/dfatXDt['Normalized'].max()
            dfatXDt['Normalized/N.min()']=dfatXDt['Normalized']/dfatXDt['Normalized'].min()
            dfatXDt.sort_values('Occurances', ascending=False, inplace=True)
            dftdXDt=sum(dftdXCL[splX[spli]:splX[spli+1]])
            dftdXDt.sort_values('Occurances', ascending=False, inplace=True)
            dftdXDt1=dftdXDt.copy()
            dftdXDt1.iloc[0,0]=dftdXDt['Occurances'].mean()
            dftdXDt1.sort_values('Occurances', ascending=False, inplace=True)
            dftdXDt2=dftdXDt.copy()
            dftdXDt2.iloc[:2,0]=dftdXDt['Occurances'].mean()
            dftdXDt2.sort_values('Occurances', ascending=False, inplace=True)
            dftdXDt3=dftdXDt.copy()
            dftdXDt3.iloc[:3,0]=dftdXDt['Occurances'].mean()
            dftdXDt3.sort_values('Occurances', ascending=False, inplace=True)
            dftdXDt['Normalized']=(dftdXDt['Occurances']-dftdXDt['Occurances'].mean())/dftdXDt['Occurances'].std()
            dftdXDt['Normalized/N.max()']=dftdXDt['Normalized']/dftdXDt['Normalized'].max()
            dftdXDt['Normalized/N.min()']=dftdXDt['Normalized']/dftdXDt['Normalized'].min()            
            dftdXDt1['Normalized']=(dftdXDt1['Occurances']-dftdXDt1['Occurances'].mean())/dftdXDt1['Occurances'].std()
            dftdXDt1['Normalized/N.max()']=dftdXDt1['Normalized']/dftdXDt1['Normalized'].max()
            dftdXDt1['Normalized/N.min()']=dftdXDt1['Normalized']/dftdXDt1['Normalized'].min()            
            dftdXDt2['Normalized']=(dftdXDt2['Occurances']-dftdXDt2['Occurances'].mean())/dftdXDt2['Occurances'].std()
            dftdXDt2['Normalized/N.max()']=dftdXDt2['Normalized']/dftdXDt2['Normalized'].max()
            dftdXDt2['Normalized/N.min()']=dftdXDt2['Normalized']/dftdXDt2['Normalized'].min()            
            dftdXDt3['Normalized']=(dftdXDt3['Occurances']-dftdXDt3['Occurances'].mean())/dftdXDt3['Occurances'].std()
            dftdXDt3['Normalized/N.max()']=dftdXDt3['Normalized']/dftdXDt3['Normalized'].max()
            dftdXDt3['Normalized/N.min()']=dftdXDt3['Normalized']/dftdXDt3['Normalized'].min()            
            dfatXD[spli]=dfatXDt
            dftdXD[spli]=dftdXDt
            dftd1XD[spli]=dftdXDt1
            dftd2XD[spli]=dftdXDt2
            dftd3XD[spli]=dftdXDt3
    dfpredXt=pd.DataFrame(columns=pred_typesL)
    for key in dfatXD:
        dfatXDk=dfatXD[key]
        dftdXDk=dftdXD[key]
        dftd1XDk=dftd1XD[key]
        dftd2XDk=dftd2XD[key]
        dftd3XDk=dftd3XD[key]
        dfpXt=pd.DataFrame()
        dfpXt['N-N']=dftdXDk['Normalized']-dfatXDk['Normalized']
        dfpXt['N-N/2']=dftdXDk['Normalized']-(dfatXDk['Normalized']/2)
        dfpXt['N-N/3']=dftdXDk['Normalized']-(dfatXDk['Normalized']/3)
        dfpXt['N-N/4']=dftdXDk['Normalized']-(dfatXDk['Normalized']/4)
        dfpXt['N/maxt+N/mina']=dftdXDk['Normalized/N.max()']/2+(dfatXDk['Normalized/N.min()'])/3
        dfpXt['top1td']=dftd1XDk['Normalized']-(dfatXDk['Normalized'])
        dfpXt['top1td-N/3']=dftd1XDk['Normalized']-(dfatXDk['Normalized']/3)
        dfpXt['top2td']=dftd2XDk['Normalized']-(dfatXDk['Normalized'])
        dfpXt['top2td-N/3']=dftd2XDk['Normalized']-(dfatXDk['Normalized']/3)
        dfpXt['top3td']=dftd3XDk['Normalized']-(dfatXDk['Normalized'])
        dfpXt['top3td-N/3']=dftd3XDk['Normalized']-(dfatXDk['Normalized']/3)
        for pt in pred_typesL:
            dfpXt.sort_values(pt, ascending=False, inplace=True)
            not_done=True
            nd_num=0
            while not_done:
                if dfpXt[pt].index[nd_num] not in list(dfpredXt[pt]):
                    dfpredXt.loc[key,pt]=dfpXt[pt].index[nd_num]
                    not_done=False
                else:
                    nd_num+=1
                    continue
    predX1row=[pred_draw_num,list(dfpredXt['N-N']),c_chX,'xN-N',num_pX]
    predX2row=[pred_draw_num,list(dfpredXt['N-N/2']),c_chX,'xN-N/2',num_pX]
    predX3row=[pred_draw_num,list(dfpredXt['N-N/3']),c_chX,'xN-N/3',num_pX]
    predX4row=[pred_draw_num,list(dfpredXt['N-N/4']),c_chX,'xN-N/4',num_pX]
    predX5row=[pred_draw_num,list(dfpredXt['N/maxt+N/mina']),c_chX,'xN/maxt+N/mina',num_pX]
    predX6row=[pred_draw_num,list(dfpredXt['top1td']),c_chX,'xtop1td',num_pX]
    predX7row=[pred_draw_num,list(dfpredXt['top1td-N/3']),c_chX,'xtop1td-N/3',num_pX]
    predX8row=[pred_draw_num,list(dfpredXt['top2td']),c_chX,'xtop2td',num_pX]
    predX9row=[pred_draw_num,list(dfpredXt['top2td-N/3']),c_chX,'xtop2td-N/3',num_pX]
    predX10row=[pred_draw_num,list(dfpredXt['top3td']),c_chX,'xtop3td',num_pX]
    predX11row=[pred_draw_num,list(dfpredXt['top3td-N/3']),c_chX,'xtop3td-N/3',num_pX]
    temp_dfpredX=pd.DataFrame([predX1row,predX2row,predX3row,predX4row,predX5row, predX6row, predX7row, predX8row, predX9row, predX10row, predX11row], columns=initpred_cols)
    dfpred=dfpred.append(temp_dfpredX)
    dfpred.reset_index(drop=True,inplace=True)



def draw_predZ(c_chZ,num_pZ):
    global dfpred, dfpredZt, temp_dfpredX
    pred_draw_num=dfat['drawNumber'].iloc[-1]
    dftd=dfat.tail(c_chZ)
    dftdX1t=dftd['first'].value_counts()
    dftdX1=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX1t.index:
        dftdX1.loc[dind,'Occurances']=dftdX1t[dind]
    dftdX2t=dftd['second'].value_counts()
    dftdX2=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX2t.index:
        dftdX2.loc[dind,'Occurances']=dftdX2t[dind]
    dftdX3t=dftd['third'].value_counts()
    dftdX3=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX3t.index:
        dftdX3.loc[dind,'Occurances']=dftdX3t[dind]
    dftdX4t=dftd['fourth'].value_counts()
    dftdX4=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX4t.index:
        dftdX4.loc[dind,'Occurances']=dftdX4t[dind]
    dftdX5t=dftd['fifth'].value_counts()
    dftdX5=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX5t.index:
        dftdX5.loc[dind,'Occurances']=dftdX5t[dind]
    dftdX6t=dftd['sixth'].value_counts()
    dftdX6=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX6t.index:
        dftdX6.loc[dind,'Occurances']=dftdX6t[dind]
    dftdX7t=dftd['seventh'].value_counts()
    dftdX7=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX7t.index:
        dftdX7.loc[dind,'Occurances']=dftdX7t[dind]
    dftdX8t=dftd['eighth'].value_counts()
    dftdX8=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX8t.index:
        dftdX8.loc[dind,'Occurances']=dftdX8t[dind]
    dftdX9t=dftd['ninth'].value_counts()
    dftdX9=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX9t.index:
        dftdX9.loc[dind,'Occurances']=dftdX9t[dind]
    dftdX10t=dftd['tenth'].value_counts()
    dftdX10=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX10t.index:
        dftdX10.loc[dind,'Occurances']=dftdX10t[dind]
    dftdX11t=dftd['eleventh'].value_counts()
    dftdX11=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX11t.index:
        dftdX11.loc[dind,'Occurances']=dftdX11t[dind]
    dftdX12t=dftd['twelfth'].value_counts()
    dftdX12=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX12t.index:
        dftdX12.loc[dind,'Occurances']=dftdX12t[dind]
    dftdX13t=dftd['thirteenth'].value_counts()
    dftdX13=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX13t.index:
        dftdX13.loc[dind,'Occurances']=dftdX13t[dind]
    dftdX14t=dftd['fourteenth'].value_counts()
    dftdX14=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX14t.index:
        dftdX14.loc[dind,'Occurances']=dftdX14t[dind]
    dftdX15t=dftd['fifteenth'].value_counts()
    dftdX15=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX15t.index:
        dftdX15.loc[dind,'Occurances']=dftdX15t[dind]
    dftdX16t=dftd['sixteenth'].value_counts()
    dftdX16=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX16t.index:
        dftdX16.loc[dind,'Occurances']=dftdX16t[dind]
    dftdX17t=dftd['seventeenth'].value_counts()
    dftdX17=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX17t.index:
        dftdX17.loc[dind,'Occurances']=dftdX17t[dind]
    dftdX18t=dftd['eighteenth'].value_counts()
    dftdX18=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX18t.index:
        dftdX18.loc[dind,'Occurances']=dftdX18t[dind]
    dftdX19t=dftd['nineteenth'].value_counts()
    dftdX19=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX19t.index:
        dftdX19.loc[dind,'Occurances']=dftdX19t[dind]
    dftdX20t=dftd['twentieth'].value_counts()
    dftdX20=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX20t.index:
        dftdX20.loc[dind,'Occurances']=dftdX20t[dind]
    dftdXCL=[dftdX1, dftdX2, dftdX3, dftdX4, dftdX5, dftdX6, dftdX7, dftdX8, dftdX9, dftdX10, dftdX11, dftdX12, dftdX13, dftdX14, dftdX15, dftdX16, dftdX17, dftdX18, dftdX19, dftdX20]
    
    #previous games value count
    dfntvc=sum(dftdXCL)
    dfntvc.sort_values('Occurances', ascending=False, inplace=True)
    dfntvc['Normalized']=(dfntvc['Occurances']-dfntvc['Occurances'].mean())/dfntvc['Occurances'].std()
    dfntvc['Normalized/N.max()']=dfntvc['Normalized']/dfntvc['Normalized'].max()
    dfntvc['Normalized/N.min()']=dfntvc['Normalized']/dfntvc['Normalized'].min()

    splX=np.linspace(0,20,num_pZ+1,dtype=int)
    dfatXD={}
    dftdXD={}
    for spli in range(len(splX)):
        if splX[spli] != splX[-1]:
            dfatXDt=pd.DataFrame(columns=['Occurances'],index=dfnvc.index).fillna(0)
            dfatXDtd=sum(dfatXCL[splX[spli]:splX[spli+1]])
            for dind in dfatXDtd.index:
                dfatXDt.loc[dind,'Occurances']=dfatXDtd[dind]
            dfatXDt['Normalized']=(dfatXDt['Occurances']-dfatXDt['Occurances'].mean())/dfatXDt['Occurances'].std()
            dfatXDt['Normalized/N.max()']=dfatXDt['Normalized']/dfatXDt['Normalized'].max()
            dfatXDt['Normalized/N.min()']=dfatXDt['Normalized']/dfatXDt['Normalized'].min()
            dfatXDt.sort_values('Occurances', ascending=False, inplace=True)
            dftdXDt=sum(dftdXCL[splX[spli]:splX[spli+1]])
            dftdXDt.sort_values('Occurances', ascending=False, inplace=True)
            dftdXDt['Normalized']=(dftdXDt['Occurances']-dftdXDt['Occurances'].mean())/dftdXDt['Occurances'].std()
            dftdXDt['Normalized/N.max()']=dftdXDt['Normalized']/dftdXDt['Normalized'].max()
            dftdXDt['Normalized/N.min()']=dftdXDt['Normalized']/dftdXDt['Normalized'].min()            
            dfatXD[spli]=dfatXDt
            dftdXD[spli]=dftdXDt
    ############
    dfpZt_cols=['zA4','zlNN-at','zlN-2at','zN-2at']
    dfpredZt=pd.DataFrame(columns=dfpZt_cols)
    for key in dfatXD:
        dfatZDk=dfatXD[key]
        dftdZDk=dftdXD[key]
        dfpZt=pd.DataFrame()
        dfpZt['zA4']=dftdZDk['Normalized']+dfntvc['Normalized']-dfatZDk['Normalized']-dfnvc['Normalized']
        dfpZt['zlNN-at']=dftdZDk['Normalized']+dfntvc['Normalized']-dfnvc['Normalized']
        dfpZt['zlN-2at']=dftdZDk['Normalized']-dfatZDk['Normalized']-dfnvc['Normalized']
        dfpZt['zN-2at']=dfntvc['Normalized']-dfatZDk['Normalized']-dfnvc['Normalized']
        for pt in dfpZt_cols:
            dfpZt.sort_values(pt, ascending=False, inplace=True)
            not_done=True
            nd_num=0
            while not_done:
                if dfpZt[pt].index[nd_num] not in list(dfpredZt[pt]):
                    dfpredZt.loc[key,pt]=dfpZt[pt].index[nd_num]
                    not_done=False
                else:
                    nd_num+=1
                    continue
    predZ1row=[pred_draw_num,list(dfpredZt['zA4']),c_chZ,'zA4',num_pZ]
    predZ2row=[pred_draw_num,list(dfpredZt['zlNN-at']),c_chZ,'zlNN-at',num_pZ]
    predZ3row=[pred_draw_num,list(dfpredZt['zlN-2at']),c_chZ,'zlN-2at',num_pZ]
    predZ4row=[pred_draw_num,list(dfpredZt['zN-2at']),c_chZ,'zN-2at',num_pZ]

    temp_dfpredZ=pd.DataFrame([predZ1row,predZ2row,predZ3row,predZ4row], columns=initpred_cols)
    #dfpred=dfpred.append(temp_dfpredZ)
    #dfpred.reset_index(drop=True,inplace=True)
    




def draw_predALL(c_ch,num_p):
    global dfpred
    #draw_pred
    pred_draw_num=dfat['drawNumber'].iloc[-1]
    dftd=dfat.tail(c_ch)
    dftdX1t=dftd['first'].value_counts()
    dftdX1=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX1t.index:
        dftdX1.loc[dind,'Occurances']=dftdX1t[dind]
    dftdX2t=dftd['second'].value_counts()
    dftdX2=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX2t.index:
        dftdX2.loc[dind,'Occurances']=dftdX2t[dind]
    dftdX3t=dftd['third'].value_counts()
    dftdX3=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX3t.index:
        dftdX3.loc[dind,'Occurances']=dftdX3t[dind]
    dftdX4t=dftd['fourth'].value_counts()
    dftdX4=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX4t.index:
        dftdX4.loc[dind,'Occurances']=dftdX4t[dind]
    dftdX5t=dftd['fifth'].value_counts()
    dftdX5=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX5t.index:
        dftdX5.loc[dind,'Occurances']=dftdX5t[dind]
    dftdX6t=dftd['sixth'].value_counts()
    dftdX6=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX6t.index:
        dftdX6.loc[dind,'Occurances']=dftdX6t[dind]
    dftdX7t=dftd['seventh'].value_counts()
    dftdX7=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX7t.index:
        dftdX7.loc[dind,'Occurances']=dftdX7t[dind]
    dftdX8t=dftd['eighth'].value_counts()
    dftdX8=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX8t.index:
        dftdX8.loc[dind,'Occurances']=dftdX8t[dind]
    dftdX9t=dftd['ninth'].value_counts()
    dftdX9=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX9t.index:
        dftdX9.loc[dind,'Occurances']=dftdX9t[dind]
    dftdX10t=dftd['tenth'].value_counts()
    dftdX10=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX10t.index:
        dftdX10.loc[dind,'Occurances']=dftdX10t[dind]
    dftdX11t=dftd['eleventh'].value_counts()
    dftdX11=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX11t.index:
        dftdX11.loc[dind,'Occurances']=dftdX11t[dind]
    dftdX12t=dftd['twelfth'].value_counts()
    dftdX12=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX12t.index:
        dftdX12.loc[dind,'Occurances']=dftdX12t[dind]
    dftdX13t=dftd['thirteenth'].value_counts()
    dftdX13=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX13t.index:
        dftdX13.loc[dind,'Occurances']=dftdX13t[dind]
    dftdX14t=dftd['fourteenth'].value_counts()
    dftdX14=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX14t.index:
        dftdX14.loc[dind,'Occurances']=dftdX14t[dind]
    dftdX15t=dftd['fifteenth'].value_counts()
    dftdX15=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX15t.index:
        dftdX15.loc[dind,'Occurances']=dftdX15t[dind]
    dftdX16t=dftd['sixteenth'].value_counts()
    dftdX16=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX16t.index:
        dftdX16.loc[dind,'Occurances']=dftdX16t[dind]
    dftdX17t=dftd['seventeenth'].value_counts()
    dftdX17=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX17t.index:
        dftdX17.loc[dind,'Occurances']=dftdX17t[dind]
    dftdX18t=dftd['eighteenth'].value_counts()
    dftdX18=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX18t.index:
        dftdX18.loc[dind,'Occurances']=dftdX18t[dind]
    dftdX19t=dftd['nineteenth'].value_counts()
    dftdX19=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX19t.index:
        dftdX19.loc[dind,'Occurances']=dftdX19t[dind]
    dftdX20t=dftd['twentieth'].value_counts()
    dftdX20=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
    for dind in dftdX20t.index:
        dftdX20.loc[dind,'Occurances']=dftdX20t[dind]
    dftdXCL=[dftdX1, dftdX2, dftdX3, dftdX4, dftdX5, dftdX6, dftdX7, dftdX8, dftdX9, dftdX10, dftdX11, dftdX12, dftdX13, dftdX14, dftdX15, dftdX16, dftdX17, dftdX18, dftdX19, dftdX20]

    dfntvc=sum(dftdXCL)
    dfntvc.sort_values('Occurances', ascending=False, inplace=True)
    dfntvc['Normalized']=(dfntvc['Occurances']-dfntvc['Occurances'].mean())/dfntvc['Occurances'].std()
    dfntvc['Normalized/N.max()']=dfntvc['Normalized']/dfntvc['Normalized'].max()
    dfntvc['Normalized/N.min()']=dfntvc['Normalized']/dfntvc['Normalized'].min()
    dfntvc1=dfntvc.copy()
    dfntvc1.iloc[0]=dfntvc1['Occurances'].mean()
    dfntvc1['Normalized']=(dfntvc1['Occurances']-dfntvc1['Occurances'].mean())/dfntvc1['Occurances'].std()
    dfntvc1['Normalized/N.max()']=dfntvc1['Normalized']/dfntvc1['Normalized'].max()
    dfntvc1['Normalized/N.min()']=dfntvc1['Normalized']/dfntvc1['Normalized'].min()
    dfntvc2=dfntvc.copy()
    dfntvc2.iloc[:2]=dfntvc2['Occurances'].mean()
    dfntvc2['Normalized']=(dfntvc2['Occurances']-dfntvc2['Occurances'].mean())/dfntvc2['Occurances'].std()
    dfntvc2['Normalized/N.max()']=dfntvc2['Normalized']/dfntvc2['Normalized'].max()
    dfntvc2['Normalized/N.min()']=dfntvc2['Normalized']/dfntvc2['Normalized'].min()
    dfntvc3=dfntvc.copy()
    dfntvc3.iloc[:3]=dfntvc3['Occurances'].mean()
    dfntvc3['Normalized']=(dfntvc3['Occurances']-dfntvc3['Occurances'].mean())/dfntvc3['Occurances'].std()
    dfntvc3['Normalized/N.max()']=dfntvc3['Normalized']/dfntvc3['Normalized'].max()
    dfntvc3['Normalized/N.min()']=dfntvc3['Normalized']/dfntvc3['Normalized'].min()

    tdat_p=pd.DataFrame()
    tdat_p['N.Total']=dfntvc['Normalized']-dfnvc['Normalized']
    tdat_p['N.td-N/2.at']=dfntvc['Normalized']-(dfnvc['Normalized']/2)
    tdat_p['N.td-N/3.at']=dfntvc['Normalized']-(dfnvc['Normalized']/3)
    tdat_p['N.td-N/4.at']=dfntvc['Normalized']-(dfnvc['Normalized']/4)
    tdat_p['N/max.td+N/min.at']=dfntvc['Normalized/N.max()']/2+(dfnvc['Normalized/N.min()'])/3
    tdat_p['top1td']=dfntvc1['Normalized']-(dfnvc['Normalized'])
    tdat_p['top1td-N/3']=dfntvc1['Normalized']-(dfnvc['Normalized']/3)
    tdat_p['top2td']=dfntvc2['Normalized']-(dfnvc['Normalized'])
    tdat_p['top2td-N/3']=dfntvc2['Normalized']-(dfnvc['Normalized']/3)
    tdat_p['top3td']=dfntvc3['Normalized']-(dfnvc['Normalized'])
    tdat_p['top3td-N/3']=dfntvc3['Normalized']-(dfnvc['Normalized']/3)
    tdat_p=tdat_p.sort_values(by=['N.Total'], ascending=False)                            
    pred_list=[]
    for i in tdat_p.head(num_p).index:
        pred_list.append(i)   
    tdat_p=tdat_p.sort_values(by=['N.td-N/2.at'], ascending=False)
    pred_list2=[]
    for j in tdat_p.head(num_p).index:
        pred_list2.append(j)
    tdat_p=tdat_p.sort_values(by=['N.td-N/3.at'], ascending=False)
    pred_list3=[]
    for j in tdat_p.head(num_p).index:
        pred_list3.append(j)
    tdat_p=tdat_p.sort_values(by=['N.td-N/4.at'], ascending=False)
    pred_list4=[]
    for j in tdat_p.head(num_p).index:
        pred_list4.append(j)
    tdat_p=tdat_p.sort_values(by=['N/max.td+N/min.at'], ascending=False)
    pred_list5=[]
    for j in tdat_p.head(num_p).index:
        pred_list5.append(j)        
    tdat_p=tdat_p.sort_values(by=['top1td'], ascending=False)                            
    pred_list6=[]
    for i in tdat_p.head(num_p).index:
        pred_list6.append(i)   
    tdat_p=tdat_p.sort_values(by=['top1td-N/3'], ascending=False)                            
    pred_list7=[]
    for i in tdat_p.head(num_p).index:
        pred_list7.append(i)   
    tdat_p=tdat_p.sort_values(by=['top2td'], ascending=False)                            
    pred_list8=[]
    for i in tdat_p.head(num_p).index:
        pred_list8.append(i)   
    tdat_p=tdat_p.sort_values(by=['top2td-N/3'], ascending=False)                            
    pred_list9=[]
    for i in tdat_p.head(num_p).index:
        pred_list9.append(i)   
    tdat_p=tdat_p.sort_values(by=['top3td'], ascending=False)                            
    pred_list10=[]
    for i in tdat_p.head(num_p).index:
        pred_list10.append(i)   
    tdat_p=tdat_p.sort_values(by=['top3td-N/3'], ascending=False)                            
    pred_list11=[]
    for i in tdat_p.head(num_p).index:
        pred_list11.append(i)
    pred1row=[pred_draw_num,pred_list,c_ch,'N-N',num_p]
    pred2row=[pred_draw_num,pred_list2,c_ch,'N-N/2',num_p]
    pred3row=[pred_draw_num,pred_list3,c_ch,'N-N/3',num_p]
    pred4row=[pred_draw_num,pred_list4,c_ch,'N-N/4',num_p]
    pred5row=[pred_draw_num,pred_list5,c_ch,'N/maxt+N/mina',num_p]
    pred6row=[pred_draw_num,pred_list6,c_ch,'top1td',num_p]
    pred7row=[pred_draw_num,pred_list7,c_ch,'top1td-N/3',num_p]
    pred8row=[pred_draw_num,pred_list8,c_ch,'top2td',num_p]
    pred9row=[pred_draw_num,pred_list9,c_ch,'top2td-N/3',num_p]
    pred10row=[pred_draw_num,pred_list10,c_ch,'top3td',num_p]
    pred11row=[pred_draw_num,pred_list11,c_ch,'top3td-N/3',num_p]
    temp_dfpred=pd.DataFrame([pred1row,pred2row,pred3row,pred4row,pred5row, pred6row, pred7row, pred8row, pred9row, pred10row, pred11row], columns=initpred_cols)

    #draw_predX
    c_chX=c_ch
    num_pX=num_p    
    splX=np.linspace(0,20,num_pX+1,dtype=int)
    dfatXD={}
    dftdXD={}
    dftd1XD={}
    dftd2XD={}
    dftd3XD={}
    for spli in range(len(splX)):
        if splX[spli] != splX[-1]:
            dfatXDt=pd.DataFrame(columns=['Occurances'],index=dfnvc.index).fillna(0)
            dfatXDtd=sum(dfatXCL[splX[spli]:splX[spli+1]])
            for dind in dfatXDtd.index:
                dfatXDt.loc[dind,'Occurances']=dfatXDtd[dind]
            dfatXDt['Normalized']=(dfatXDt['Occurances']-dfatXDt['Occurances'].mean())/dfatXDt['Occurances'].std()
            dfatXDt['Normalized/N.max()']=dfatXDt['Normalized']/dfatXDt['Normalized'].max()
            dfatXDt['Normalized/N.min()']=dfatXDt['Normalized']/dfatXDt['Normalized'].min()
            dfatXDt.sort_values('Occurances', ascending=False, inplace=True)

            dftdXDt=sum(dftdXCL[splX[spli]:splX[spli+1]])
            dftdXDt.sort_values('Occurances', ascending=False, inplace=True)
            dftdXDt1=dftdXDt.copy()
            dftdXDt1.iloc[0,0]=dftdXDt['Occurances'].mean()
            dftdXDt1.sort_values('Occurances', ascending=False, inplace=True)
            dftdXDt2=dftdXDt.copy()
            dftdXDt2.iloc[:2,0]=dftdXDt['Occurances'].mean()
            dftdXDt2.sort_values('Occurances', ascending=False, inplace=True)
            dftdXDt3=dftdXDt.copy()
            dftdXDt3.iloc[:3,0]=dftdXDt['Occurances'].mean()
            dftdXDt3.sort_values('Occurances', ascending=False, inplace=True)

            dftdXDt['Normalized']=(dftdXDt['Occurances']-dftdXDt['Occurances'].mean())/dftdXDt['Occurances'].std()
            dftdXDt['Normalized/N.max()']=dftdXDt['Normalized']/dftdXDt['Normalized'].max()
            dftdXDt['Normalized/N.min()']=dftdXDt['Normalized']/dftdXDt['Normalized'].min()            
            dftdXDt1['Normalized']=(dftdXDt1['Occurances']-dftdXDt1['Occurances'].mean())/dftdXDt1['Occurances'].std()
            dftdXDt1['Normalized/N.max()']=dftdXDt1['Normalized']/dftdXDt1['Normalized'].max()
            dftdXDt1['Normalized/N.min()']=dftdXDt1['Normalized']/dftdXDt1['Normalized'].min()            
            dftdXDt2['Normalized']=(dftdXDt2['Occurances']-dftdXDt2['Occurances'].mean())/dftdXDt2['Occurances'].std()
            dftdXDt2['Normalized/N.max()']=dftdXDt2['Normalized']/dftdXDt2['Normalized'].max()
            dftdXDt2['Normalized/N.min()']=dftdXDt2['Normalized']/dftdXDt2['Normalized'].min()            
            dftdXDt3['Normalized']=(dftdXDt3['Occurances']-dftdXDt3['Occurances'].mean())/dftdXDt3['Occurances'].std()
            dftdXDt3['Normalized/N.max()']=dftdXDt3['Normalized']/dftdXDt3['Normalized'].max()
            dftdXDt3['Normalized/N.min()']=dftdXDt3['Normalized']/dftdXDt3['Normalized'].min()            
            dfatXD[spli]=dfatXDt
            dftdXD[spli]=dftdXDt
            dftd1XD[spli]=dftdXDt1
            dftd2XD[spli]=dftdXDt2
            dftd3XD[spli]=dftdXDt3
    dfpredXt=pd.DataFrame(columns=pred_typesL)
    for key in dfatXD:
        dfatXDk=dfatXD[key]
        dftdXDk=dftdXD[key]
        dftd1XDk=dftd1XD[key]
        dftd2XDk=dftd2XD[key]
        dftd3XDk=dftd3XD[key]
        dfpXt=pd.DataFrame()
        dfpXt['N-N']=dftdXDk['Normalized']-dfatXDk['Normalized']
        dfpXt['N-N/2']=dftdXDk['Normalized']-(dfatXDk['Normalized']/2)
        dfpXt['N-N/3']=dftdXDk['Normalized']-(dfatXDk['Normalized']/3)
        dfpXt['N-N/4']=dftdXDk['Normalized']-(dfatXDk['Normalized']/4)
        dfpXt['N/maxt+N/mina']=dftdXDk['Normalized/N.max()']/2+(dfatXDk['Normalized/N.min()'])/3
        dfpXt['top1td']=dftd1XDk['Normalized']-(dfatXDk['Normalized'])
        dfpXt['top1td-N/3']=dftd1XDk['Normalized']-(dfatXDk['Normalized']/3)
        dfpXt['top2td']=dftd2XDk['Normalized']-(dfatXDk['Normalized'])
        dfpXt['top2td-N/3']=dftd2XDk['Normalized']-(dfatXDk['Normalized']/3)
        dfpXt['top3td']=dftd3XDk['Normalized']-(dfatXDk['Normalized'])
        dfpXt['top3td-N/3']=dftd3XDk['Normalized']-(dfatXDk['Normalized']/3)
        for pt in pred_typesL:
            dfpXt.sort_values(pt, ascending=False, inplace=True)
            not_done=True
            nd_num=0
            while not_done:
                if dfpXt[pt].index[nd_num] not in list(dfpredXt[pt]):
                    dfpredXt.loc[key,pt]=dfpXt[pt].index[nd_num]
                    not_done=False
                else:
                    nd_num+=1
                    continue
    predX1row=[pred_draw_num,list(dfpredXt['N-N']),c_chX,'xN-N',num_pX]
    predX2row=[pred_draw_num,list(dfpredXt['N-N/2']),c_chX,'xN-N/2',num_pX]
    predX3row=[pred_draw_num,list(dfpredXt['N-N/3']),c_chX,'xN-N/3',num_pX]
    predX4row=[pred_draw_num,list(dfpredXt['N-N/4']),c_chX,'xN-N/4',num_pX]
    predX5row=[pred_draw_num,list(dfpredXt['N/maxt+N/mina']),c_chX,'xN/maxt+N/mina',num_pX]
    predX6row=[pred_draw_num,list(dfpredXt['top1td']),c_chX,'xtop1td',num_pX]
    predX7row=[pred_draw_num,list(dfpredXt['top1td-N/3']),c_chX,'xtop1td-N/3',num_pX]
    predX8row=[pred_draw_num,list(dfpredXt['top2td']),c_chX,'xtop2td',num_pX]
    predX9row=[pred_draw_num,list(dfpredXt['top2td-N/3']),c_chX,'xtop2td-N/3',num_pX]
    predX10row=[pred_draw_num,list(dfpredXt['top3td']),c_chX,'xtop3td',num_pX]
    predX11row=[pred_draw_num,list(dfpredXt['top3td-N/3']),c_chX,'xtop3td-N/3',num_pX]
    temp_dfpredX=pd.DataFrame([predX1row,predX2row,predX3row,predX4row,predX5row, predX6row, predX7row, predX8row, predX9row, predX10row, predX11row], columns=initpred_cols)

    #draw_predZ
    c_chZ=c_chX
    num_pZ=num_pX
    dfpZt_cols=['zA4','zlNN-at','zlN-2at','zN-2at']
    dfpredZt=pd.DataFrame(columns=dfpZt_cols)
    for key in dfatXD:
        dfatZDk=dfatXD[key]
        dftdZDk=dftdXD[key]
        dfpZt=pd.DataFrame()
        dfpZt['zA4']=dftdZDk['Normalized']+dfntvc['Normalized']-dfatZDk['Normalized']-dfnvc['Normalized']
        dfpZt['zlNN-at']=dftdZDk['Normalized']+dfntvc['Normalized']-dfnvc['Normalized']
        dfpZt['zlN-2at']=dftdZDk['Normalized']-dfatZDk['Normalized']-dfnvc['Normalized']
        dfpZt['zN-2at']=dfntvc['Normalized']-dfatZDk['Normalized']-dfnvc['Normalized']
        for pt in dfpZt_cols:
            dfpZt.sort_values(pt, ascending=False, inplace=True)
            not_done=True
            nd_num=0
            while not_done:
                if dfpZt[pt].index[nd_num] not in list(dfpredZt[pt]):
                    dfpredZt.loc[key,pt]=dfpZt[pt].index[nd_num]
                    not_done=False
                else:
                    nd_num+=1
                    continue
    predZ1row=[pred_draw_num,list(dfpredZt['zA4']),c_chZ,'zA4',num_pZ]
    predZ2row=[pred_draw_num,list(dfpredZt['zlNN-at']),c_chZ,'zlNN-at',num_pZ]
    predZ3row=[pred_draw_num,list(dfpredZt['zlN-2at']),c_chZ,'zlN-2at',num_pZ]
    predZ4row=[pred_draw_num,list(dfpredZt['zN-2at']),c_chZ,'zN-2at',num_pZ]
    temp_dfpredZ=pd.DataFrame([predZ1row,predZ2row,predZ3row,predZ4row], columns=initpred_cols)
    
    #dfpred concat
    dfpred=pd.concat([dfpred,temp_dfpred,temp_dfpredX,temp_dfpredZ])
    dfpred.reset_index(drop=True,inplace=True)
    
def pred_draw3(c_histn):
    global dfpred
    pred_draw_num=dfat['drawNumber'].iloc[-1]
    pred=[]
    for i in dfnvc.tail(c_histn).index:
        pred.append(i)
    pred3row=[pred_draw_num,pred,len(dfat),'drAT',c_histn]
    tempdfpred3=pd.DataFrame([pred3row],columns=initpred_cols)
    dfpred=dfpred.append(tempdfpred3)
    dfpred.reset_index(drop=True,inplace=True)

def pred_draw4(c_ch,c_histn,today_d):
    global dfpred
    dftd=dfat[dfat['drawDate']==today_d]
    sin_num_list3=[]
    for i in dftd['winningNumbers'].tail(c_ch):
        for j in i:
            sin_num_list3.append(j)
    dfntdt=pd.DataFrame({'Numbers':sin_num_list3})
    dftdvct=pd.DataFrame(data=dfntdt.value_counts())
    dftdvct.rename(columns=str, inplace=True)
    dftdvct.rename(columns={'0':'Occurances'}, inplace=True)
    dftdvct['Normalized']=(dftdvct['Occurances']-dftdvct['Occurances'].mean())/dftdvct['Occurances'].std()
    dftdvct['Normalized/N.max()']=dftdvct['Normalized']/dftdvct['Normalized'].max()
    dftdvct['Normalized/N.min()']=dftdvct['Normalized']/dftdvct['Normalized'].min()
    pred2=[]
    for i in dftdvct.head(c_histn).index:
        pred2.append(i[0])
    pred_draw_num=dfat['drawNumber'].iloc[-1]
    pred4row=[pred_draw_num,pred2,len(dftd),'drTD',c_histn]
    tempdfpred4=pd.DataFrame([pred4row],columns=initpred_cols)
    dfpred=dfpred.append(tempdfpred4)
    dfpred.reset_index(drop=True,inplace=True)

def pred_gen(prev_l,spot_l):
    for prev_n in prev_l:
        for spot_n in spot_l:
            draw_predALL(prev_n,spot_n)

def check_dfpred():
    global dfpred
    keno_payouts=pd.read_csv('KENO//KENO_payouts.csv', index_col='Picked')
    pred_cols=['drawNumber', 'prediction', 'previousGameN', 'predictionType', 'totalSpots', 'correct1', 'numbersHit1', 'correct2', 'numbersHit2', 'correct3', 'numbersHit3', 'correct4', 'numbersHit4', 'correct5', 'numbersHit5', 'correct6', 'numbersHit6', 'correct7', 'numbersHit7', 'correct8', 'numbersHit8', 'correct9', 'numbersHit9', 'correct10', 'numbersHit10', 'winningGamesN', 'profit']
    new_dfpred=dfpred.to_dict('series')    
    new_dfpred_ind=new_dfpred['profit'][new_dfpred['profit'].isna()].index
    for colnd in new_dfpred:
        new_dfpred[colnd]=new_dfpred[colnd].iloc[new_dfpred_ind]
        new_dfpred[colnd].reset_index(drop=True,inplace=True)
    if len(new_dfpred['profit'])>0:
        df_ptemp=pd.DataFrame(columns=pred_cols)        
        for draw in new_dfpred['drawNumber'].value_counts().index:
            temp_dfat=dfat[dfat['drawNumber']>draw].drop(columns=['first', 'second', 'third',
            'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth',
            'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth',
            'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth', 'twentieth',
            'bonus'])
            temp_dfat=temp_dfat.head(10)
            temp_dfpred=new_dfpred.copy()
            temp_dfpred_ind=temp_dfpred['drawNumber'][temp_dfpred['drawNumber']==draw].index
            for coltdf in temp_dfpred:
                temp_dfpred[coltdf]=temp_dfpred[coltdf].iloc[temp_dfpred_ind]
                temp_dfpred[coltdf].reset_index(drop=True,inplace=True)
            #temp_dfpred=pd.DataFrame(data=temp_dfpred)
            temp_dfat=temp_dfat.to_dict('series')
            for p_ind,prediction in enumerate(temp_dfpred['prediction']):
                for w_ind,winner in enumerate(temp_dfat['winningNumbers']):
                    hit_val=[]
                    hit_num=0
                    for digit in prediction:
                        if digit in winner:
                            hit_val.append(digit)
                            hit_num+=1
                    temp_col1='correct'+str(w_ind+1)
                    temp_col2='numbersHit'+str(w_ind+1)
                    temp_dfpred[temp_col1].iloc[p_ind]=hit_num
                    temp_dfpred[temp_col2].iloc[p_ind]=hit_val
                    if w_ind==9:
                        g1=(keno_payouts[str(temp_dfpred['correct1'].iloc[p_ind])].loc[temp_dfpred['totalSpots'].iloc[p_ind]])-1
                        g2=keno_payouts[str(temp_dfpred['correct2'].iloc[p_ind])].loc[temp_dfpred['totalSpots'].iloc[p_ind]]-1
                        g3=keno_payouts[str(temp_dfpred['correct3'].iloc[p_ind])].loc[temp_dfpred['totalSpots'].iloc[p_ind]]-1
                        g4=keno_payouts[str(temp_dfpred['correct4'].iloc[p_ind])].loc[temp_dfpred['totalSpots'].iloc[p_ind]]-1
                        g5=keno_payouts[str(temp_dfpred['correct5'].iloc[p_ind])].loc[temp_dfpred['totalSpots'].iloc[p_ind]]-1
                        g6=keno_payouts[str(temp_dfpred['correct6'].iloc[p_ind])].loc[temp_dfpred['totalSpots'].iloc[p_ind]]-1
                        g7=keno_payouts[str(temp_dfpred['correct7'].iloc[p_ind])].loc[temp_dfpred['totalSpots'].iloc[p_ind]]-1
                        g8=keno_payouts[str(temp_dfpred['correct8'].iloc[p_ind])].loc[temp_dfpred['totalSpots'].iloc[p_ind]]-1
                        g9=keno_payouts[str(temp_dfpred['correct9'].iloc[p_ind])].loc[temp_dfpred['totalSpots'].iloc[p_ind]]-1
                        g10=keno_payouts[str(temp_dfpred['correct10'].iloc[p_ind])].loc[temp_dfpred['totalSpots'].iloc[p_ind]]-1
                        gt=[g1,g2,g3,g4,g5,g6,g7,g8,g9,g10]
                        temp_dfpred['profit'].iloc[p_ind]=sum(gt)
                        gamespw=[]
                        for gs,gamep in enumerate(gt):
                            if gamep>-1:
                                gamespw.append('g'+str(gs+1))
                        temp_dfpred['winningGamesN'].iloc[p_ind]=gamespw
            temp_dfpred=pd.DataFrame(data=temp_dfpred)
            df_ptemp=df_ptemp.append(temp_dfpred)
        dfpred=dfpred[dfpred['profit'].isna()==False]
        dfpred=dfpred.append(df_ptemp)
        dfpred.reset_index(drop=True,inplace=True)        
    else:
        print('\n You have no new predictions. Predictions can be generated at the welcome screen.')
        
def save_all():
    print('\n\n Saving datasets...')                
    dfat.to_pickle('KENO//KENO_alltime.pkl')
    print(' ...')
    dfat.to_csv('KENO//KENO_alltime.csv')
    print(' ...')
    dfpred.to_pickle('KENO//dfpred.pkl')
    print('\n Saved.')

def save_all_pickle():
    print(' Saving datasets...')
    dfat.to_pickle('KENO//KENO_alltime.pkl')
    print(' ...')
    dfpred.to_pickle('KENO//dfpred.pkl')

def welcome_screen(choice, today_d):
    global dfpred, dfat
    os.system('cls' if os.name == 'nt' else 'clear')
    dftd=dfat[dfat['drawDate']==today_d]
    dftd.reset_index(drop=True,inplace=True)
    def_spot_l=[6,7,12]
    def_prev_l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,25,50,100,200,300,600,900,1200,1500,1800,2100]

    ### DEFAULT/BOOT OPTION
    if choice == '0':
        if os.name == 'posix':
            os.system("printf '\e[8;30;86t'")    
        else:
            os.system('mode con: cols=122 lines=30')  
        dftd=dfat[dfat['drawDate']==today_d]
        dftd.reset_index(drop=True,inplace=True)
        print('\n           ***** KENO Predictor *****')
        print('\n           Number of draws today: '+str(len(dftd)))
        print('           Last draw number:  '+str(dfat['drawNumber'].iloc[-1]))
        boot='''
        1.  Check results of recent games.
        2.  Check highest occuring number in recent games.
        3.  Complete history prediction.
        4.  Today's draws prediction.
        5.  Complete all-time versus complete today's draws prediction.
        6.  Complete all-time versus custom today's draws prediction.
        7.  Draw Order complete history prediction.
        8.  Draw Order recent history prediction.
        9.  Draw Order complete and recent history prediction.
        10. Combination of multiple prediction types prediction.        
        11. Generate a series of predictions and store them.
        12. Check predictions that are yet to draw 10 games.
        13. Update keno database.
        14. Update results from predictions.
        15. Save datasets.
        16. Start automatic mode. (updates and predicts every 4 minutes)

                                    \n
        '''
        print(boot)
        choice=input('  Please enter your selection: ')
        os.system('cls' if os.name == 'nt' else 'clear')
    ### OPTION 1
    if choice == '1':
        tg_opt='\n 1. Just today.\n 2. All time.\n\n 0. Return to welcome screen.\n'
        print(tg_opt)
        t_games=input('\n Enter type of search. ')
        if t_games == '0':
            return welcome_screen('0',today_d)
        elif t_games == '2':
            n_games=input('\n What number of recent draws? ')
            try:
                n_gint=int(n_games)
                for i in dfat['winningNumbers'].tail(n_gint):
                    print(i)
                next_c=input('\n Enter 1 to get different results, otherwise press enter to return to welcome screen: ')
                if next_c == '1':
                    return welcome_screen('1',today_d)
                else:
                    return welcome_screen('0',today_d)
            except:
                inc_inp=input(' Unrecognized value entered. Enter 1 to try again. Otherwise press enter to return to welcome screen. ')
                if inc_inp == '1':
                    return welcome_screen('1',today_d)
                else:
                    return welcome_screen('0',today_d)
        elif t_games == '1':
            today_n=len(dftd)
            print('\n There have been '+str(today_n)+' total games today.\n')
            num_ch=input('\n How many of today\'s games would you like to see? ')
            print(' ')
            try:
                num_cint=int(num_ch)
                for i in dftd['winningNumbers'].tail(num_cint):
                    print(i)
                next_c=input('\n Enter 1 to get different results, otherwise press enter to return to welcome screen: ')
                if next_c == '1':
                    return welcome_screen('1',today_d)
                else:
                    return welcome_screen('0',today_d)
            except:
                inc_inp=input(' Unrecognized value entered. Enter 1 to try again. Otherwise press enter to return to welcome screen. ')
                if inc_inp == '1':
                    return welcome_screen('1',today_d)
                else:
                    return welcome_screen('0',today_d)
        else:
            input(' Value entered doesn\'t exist. Press enter to continue...')
            return welcome_screen('1',today_d)
    ### OPTION 2
    if choice == '2':
        print('\n Number of games today: '+str(len(dftd)))
        n_games=input('\n Number of recent draws you\'d like to see highest number occurances for? ')
        try:
            n_gint=int(n_games)
            gnum_t=-20*n_gint
            atnum_ch=[]
            for i in dfat['winningNumbers'].tail(n_gint):
                for j in i:
                    atnum_ch.append(j)
            atdf=pd.DataFrame(data=atnum_ch)
            atdfvc=pd.DataFrame(data=atdf[0].value_counts())
            print('\n 20 Highest occuring numbers are:\n')
            for i in atdfvc.head(20).index:
                print(' Number: '+str(i)+'   Occurances: '+str(atdfvc[0][i]))
            next_c=input('\n Enter 1 to get different results, otherwise press enter to return to welcome screen: ')
            if next_c == '1':
                return welcome_screen('2',today_d)
            else:
                return welcome_screen('0',today_d)
        except:
            inc_inp=input(' Unrecognized value entered. Enter 1 to try again. Otherwise press enter to return to welcome screen. ')
            if inc_inp == '1':
                return welcome_screen('2',today_d)
            else:
                return welcome_screen('0',today_d)
    ### OPTION 3
    if choice == '3':
        c_histn=input('\n How many numbers would you like to play? ')
        try:
            c_histn=int(c_histn)
            pred_draw3(c_histn)
            temppred=dfpred[['prediction','predictionType']].tail(1)
            print('\n\n', str(c_histn),'spot prediction:\n')
            for i,j in temppred.values:
                print('\n Prediction:',str(i),'   Prediction Type:',str(j))
            again_ch=input('\n\n Enter 1 for another prediction. Otherwise press enter to return to welcome screen.')
            if again_ch=='1':
                return welcome_screen('3',today_d)
            else:
                return welcome_screen('0',today_d)
        except:
            inc_inp=input('Unrecognized value entered. Enter 1 to try again. Otherwise press enter to return to welcome screen. ')
            if inc_inp == '1':
                return welcome_screen('3',today_d)
            else:
                return welcome_screen('0',today_d)
    ### OPTION 4
    if choice == '4':
        print('\n Number of games today: '+str(len(dftd))+'\n')
        c_ch=input(' How many of the todays most recent draws would you like to use? ')
        try:
            c_ch=int(c_ch)
            if 0<c_ch<=len(dftd):
                c_histn=input(' How many numbers would you like to play? ')
                try:
                    c_histn=int(c_histn)
                    pred_draw4(c_ch,c_histn,today_d)
                    temppred=dfpred[['prediction','predictionType']].tail(1)
                    print('\n\n', str(c_histn),'spot prediction:\n')
                    for i,j in temppred.values:
                        print('\n Prediction:',str(i),'   Prediction Type:',str(j))
                    again_ch=input('\n\n Enter 1 to do another, otherwise press enter to return to welcome screen.')
                    if again_ch=='1':
                        return welcome_screen('4',today_d)
                    else:
                        return welcome_screen('0',today_d)
                except:
                    inc_inp=input(' Unrecognized value entered. Enter 1 to try again. Otherwise press enter to return to welcome screen. ')
                    if inc_inp == '1':
                        return welcome_screen('4',today_d)
                    else:
                        return welcome_screen('0',today_d)
            else:
                inc_inp=input(' Number of games entered is either too large or too small. Enter 1 to try again. Otherwise press enter to return to welcome screen. ')
                if inc_inp == '1':
                    return welcome_screen('4',today_d)
                else:
                    return welcome_screen('0',today_d)
        except:
                inc_inp=input(' Unrecognized value entered. Enter 1 to try again. Otherwise press enter to return to welcome screen. ')
                if inc_inp == '1':
                    return welcome_screen('4',today_d)
                else:
                    return welcome_screen('0',today_d)
    ### OPTION 5
    if choice == '5':
        num_p=input('\n How many numbers would you like to play? ')
        try:
            num_p=int(num_p)
            if 0<num_p<13:
                c_ch=len(dftd)
                draw_pred(c_ch,num_p)
                temppred=dfpred[['prediction','predictionType']].tail(11)
                print('\n\n', str(num_p),'spot prediction:\n')
                for i,j in temppred.values:
                    print('\n Prediction:',str(i),'   Prediction Type:',str(j))

                again_ch=input('\n\n Enter 1 for another prediction, otherwise press enter to return to welcome_screen. ')
                if again_ch=='1':
                    return welcome_screen('5',today_d)
                else:
                    return welcome_screen('0',today_d)
            else:
                inc_inp=input(' Must enter a value from 1-12. Enter 1 to try again. Otherwise press enter to return to welcome screen.')
                if inc_inp == '1':
                    return welcome_screen('5',today_d)
                else:
                    return welcome_screen('0',today_d)
        except:
            inc_inp=input(' Value entered not a number. Enter 1 to try again. Otherwise press enter to return to welcome screen. ')
            if inc_inp == '1':
                return welcome_screen('5',today_d)
            else:
                return welcome_screen('0',today_d)
    ### OPTION 6
    if choice == '6':
        print('\n Number of games today: '+str(len(dftd))+'\n')
        c_ch=input(' How many of the most recent draws would you like to use? ')
        try:
            c_ch=int(c_ch)
            if 0<c_ch<=len(dfat):                
                num_p=input('\n How many numbers would you like to play? ')
                try:
                    num_p=int(num_p)
                    if 0<num_p<13:
                        draw_pred(c_ch,num_p)
                        temppred=dfpred[['prediction','predictionType']].tail(11)
                        print('\n\n', str(num_p),'spot prediction:\n')
                        for i,j in temppred.values:
                            print('\n Prediction:',str(i),'   Prediction Type:',str(j))
                        again_ch=input('\n\n Enter 1 for another prediction, otherwise press enter to return to welcome_screen. ')
                        if again_ch=='1':
                            return welcome_screen('6',today_d)
                        else:
                            return welcome_screen('0',today_d)
                    else:
                        inc_inp=input(' Must enter a value from 1-12. Enter 1 to try again. Otherwise press enter to return to welcome screen.')
                        if inc_inp == '1':
                            return welcome_screen('6',today_d)
                        else:
                            return welcome_screen('0',today_d)
                except:
                    inc_inp=input(' Value entered not a number. Enter 1 to try again. Otherwise press enter to return to welcome screen. ')
                    if inc_inp == '1':
                        return welcome_screen('6',today_d)
                    else:
                        return welcome_screen('0',today_d)                
            else:
                inc_inp=input(' Number of games entered is either too large or too small. Enter 1 to try again. Otherwise press enter to return to welcome screen. ')
                if inc_inp == '1':
                    return welcome_screen('6',today_d)
                else:
                    return welcome_screen('0',today_d)
        except:
            inc_inp=input(' Value entered not a number. Enter 1 to try again. Otherwise press enter to return to welcome screen. ')
            if inc_inp == '1':
                return welcome_screen('6',today_d)
            else:
                return welcome_screen('0',today_d)
    ### OPTION 7
    if choice == '7':
        c_atX=input('\n\n How many numberss would you like to play? ')
        try:
            c_atX=int(c_atX)
            splX7=np.linspace(0,20,c_atX+1,dtype=int)
            dfatXL=[]
            for spli in range(len(splX7)):
                if splX7[spli] != splX7[-1]:
                    dfatXDt=pd.DataFrame(columns=['Occurances'],index=dfnvc.index).fillna(0)
                    dfatXDtd=sum(dfatXCL[splX7[spli]:splX7[spli+1]])
                    for dind in dfatXDtd.index:
                        dfatXDt.loc[dind,'Occurances']=dfatXDtd[dind]
                    dfatXDt['Normalized']=(dfatXDt['Occurances']-dfatXDt['Occurances'].mean())/dfatXDt['Occurances'].std()
                    dfatXDt['Normalized/N.max()']=dfatXDt['Normalized']/dfatXDt['Normalized'].max()
                    dfatXDt['Normalized/N.min()']=dfatXDt['Normalized']/dfatXDt['Normalized'].min()
                    dfatXDt.sort_values('Occurances', ascending=True, inplace=True)
                    lp_n=0
                    while(True):
                        if dfatXDt['Occurances'].index[lp_n] not in dfatXL:
                            dfatXL.append(dfatXDt['Occurances'].index[lp_n])
                            break
                        else:
                            lp_n+=1
            print('\n\n Your prediction: ',str(dfatXL).strip('][').replace(', ',' - '))
            inc_inp=input('\n\n Enter 1 for another prediction. Otherwise press enter to return to welcome screen. ')
            if inc_inp == '1':
                return welcome_screen('7',today_d)
            else:
                return welcome_screen('0',today_d)
        except:
            inc_inp=input('\n Unrecognized value entered. Enter 1 to try again. Otherwise press enter to return to welcome screen. ')
            if inc_inp == '1':
                return welcome_screen('7',today_d)
            else:
                return welcome_screen('0',today_d)
    ### OPTION 8
    if choice == '8':
        c_tdX=input('\n\n How many numbers would you like to play? ')
        try:
            c_tdX=int(c_tdX)
            dftdX1t=dftd['first'].value_counts()
            dftdX1=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
            for dind in dftdX1t.index:
                dftdX1.loc[dind,'Occurances']=dftdX1t[dind]
            dftdX2t=dftd['second'].value_counts()
            dftdX2=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
            for dind in dftdX2t.index:
                dftdX2.loc[dind,'Occurances']=dftdX2t[dind]
            dftdX3t=dftd['third'].value_counts()
            dftdX3=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
            for dind in dftdX3t.index:
                dftdX3.loc[dind,'Occurances']=dftdX3t[dind]
            dftdX4t=dftd['fourth'].value_counts()
            dftdX4=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
            for dind in dftdX4t.index:
                dftdX4.loc[dind,'Occurances']=dftdX4t[dind]
            dftdX5t=dftd['fifth'].value_counts()
            dftdX5=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
            for dind in dftdX5t.index:
                dftdX5.loc[dind,'Occurances']=dftdX5t[dind]
            dftdX6t=dftd['sixth'].value_counts()
            dftdX6=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
            for dind in dftdX6t.index:
                dftdX6.loc[dind,'Occurances']=dftdX6t[dind]
            dftdX7t=dftd['seventh'].value_counts()
            dftdX7=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
            for dind in dftdX7t.index:
                dftdX7.loc[dind,'Occurances']=dftdX7t[dind]
            dftdX8t=dftd['eighth'].value_counts()
            dftdX8=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
            for dind in dftdX8t.index:
                dftdX8.loc[dind,'Occurances']=dftdX8t[dind]
            dftdX9t=dftd['ninth'].value_counts()
            dftdX9=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
            for dind in dftdX9t.index:
                dftdX9.loc[dind,'Occurances']=dftdX9t[dind]
            dftdX10t=dftd['tenth'].value_counts()
            dftdX10=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
            for dind in dftdX10t.index:
                dftdX10.loc[dind,'Occurances']=dftdX10t[dind]
            dftdX11t=dftd['eleventh'].value_counts()
            dftdX11=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
            for dind in dftdX11t.index:
                dftdX11.loc[dind,'Occurances']=dftdX11t[dind]
            dftdX12t=dftd['twelfth'].value_counts()
            dftdX12=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
            for dind in dftdX12t.index:
                dftdX12.loc[dind,'Occurances']=dftdX12t[dind]
            dftdX13t=dftd['thirteenth'].value_counts()
            dftdX13=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
            for dind in dftdX13t.index:
                dftdX13.loc[dind,'Occurances']=dftdX13t[dind]
            dftdX14t=dftd['fourteenth'].value_counts()
            dftdX14=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
            for dind in dftdX14t.index:
                dftdX14.loc[dind,'Occurances']=dftdX14t[dind]
            dftdX15t=dftd['fifteenth'].value_counts()
            dftdX15=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
            for dind in dftdX15t.index:
                dftdX15.loc[dind,'Occurances']=dftdX15t[dind]
            dftdX16t=dftd['sixteenth'].value_counts()
            dftdX16=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
            for dind in dftdX16t.index:
                dftdX16.loc[dind,'Occurances']=dftdX16t[dind]
            dftdX17t=dftd['seventeenth'].value_counts()
            dftdX17=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
            for dind in dftdX17t.index:
                dftdX17.loc[dind,'Occurances']=dftdX17t[dind]
            dftdX18t=dftd['eighteenth'].value_counts()
            dftdX18=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
            for dind in dftdX18t.index:
                dftdX18.loc[dind,'Occurances']=dftdX18t[dind]
            dftdX19t=dftd['nineteenth'].value_counts()
            dftdX19=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
            for dind in dftdX19t.index:
                dftdX19.loc[dind,'Occurances']=dftdX19t[dind]
            dftdX20t=dftd['twentieth'].value_counts()
            dftdX20=pd.DataFrame(index=dfnvc.index, columns=['Occurances']).fillna(0)
            for dind in dftdX20t.index:
                dftdX20.loc[dind,'Occurances']=dftdX20t[dind]
            dftdXCL=[dftdX1, dftdX2, dftdX3, dftdX4, dftdX5, dftdX6, dftdX7, dftdX8, dftdX9, dftdX10, dftdX11, dftdX12, dftdX13, dftdX14, dftdX15, dftdX16, dftdX17, dftdX18, dftdX19, dftdX20]

            splX8=np.linspace(0,20,c_tdX+1,dtype=int)
            dftdXL=[]
            for spli in range(len(splX8)):
                if splX8[spli] != splX8[-1]:
                    dftdXDt=sum(dftdXCL[splX8[spli]:splX8[spli+1]])
                    dftdXDt.sort_values('Occurances', ascending=False, inplace=True)
                    lp_n=0
                    while(True):
                        if dftdXDt['Occurances'].index[lp_n] not in dftdXL:
                            dftdXL.append(dftdXDt['Occurances'].index[lp_n])
                            break
                        else:
                            lp_n+=1
            print('\n\n Your prediction: ',str(dftdXL).strip('][').replace(', ',' - '))
            inc_inp=input('\n\n Enter 1 for another prediction. Otherwise press enter to return to welcome screen. ')
            if inc_inp == '1':
                return welcome_screen('8',today_d)
            else:
                return welcome_screen('0',today_d)
        except:
            inc_inp=input('\n Unrecognized value entered. Enter 1 to try again. Otherwise press enter to return to welcome screen. ')
            if inc_inp == '1':
                return welcome_screen('8',today_d)
            else:
                return welcome_screen('0',today_d)
    ### OPTION 9
    if choice == '9':
        print('\n Number of games today: '+str(len(dftd))+'\n')
        c_ch=input(' How many of the most recent draws would you like to use? ')
        try:
            c_ch=int(c_ch)
            if 0<c_ch<=len(dfat):                
                num_p=input('\n How many numbers would you like to play? ')
                try:
                    num_p=int(num_p)
                    if 0<num_p<13:
                        draw_predX(c_ch,num_p)
                        temppred=dfpred[['prediction','predictionType']].tail(11)
                        print('\n\n', str(num_p),'spot prediction:\n')
                        for i,j in temppred.values:
                            print('\n Prediction:',str(i),'   Prediction Type:',str(j))
                        again_ch=input('\n\n Enter 1 for another prediction, otherwise press enter to return to welcome_screen. ')
                        if again_ch=='1':
                            return welcome_screen('9',today_d)
                        else:
                            return welcome_screen('0',today_d)
                    else:
                        inc_inp=input(' Must enter a value from 1-12. Enter 1 to try again. Otherwise press enter to return to welcome screen.')
                        if inc_inp == '1':
                            return welcome_screen('9',today_d)
                        else:
                            return welcome_screen('0',today_d)
                except:
                    inc_inp=input(' Value entered not a number. Enter 1 to try again. Otherwise press enter to return to welcome screen. ')
                    if inc_inp == '1':
                        return welcome_screen('9',today_d)
                    else:
                        return welcome_screen('0',today_d)                
            else:
                inc_inp=input(' Number of games entered is either too large or too small. Enter 1 to try again. Otherwise press enter to return to welcome screen. ')
                if inc_inp == '1':
                    return welcome_screen('9',today_d)
                else:
                    return welcome_screen('0',today_d)
        except:
            inc_inp=input(' Value entered not a number. Enter 1 to try again. Otherwise press enter to return to welcome screen. ')
            if inc_inp == '1':
                return welcome_screen('9',today_d)
            else:
                return welcome_screen('0',today_d)
    ### OPTION 10
    if choice == '10':
        print('\n Number of games today: '+str(len(dftd))+'\n')
        c_ch=input(' How many of the most recent draws would you like to use? ')
        try:
            c_ch=int(c_ch)
            if 0<c_ch<=len(dfat):                
                num_p=input('\n How many numbers would you like to play? ')
                try:
                    num_p=int(num_p)
                    if 0<num_p<13:
                        draw_predZ(c_ch,num_p)
                        temppred=dfpred[['prediction','predictionType']].tail(4)
                        print('\n\n', str(num_p),'spot prediction:\n')
                        for i,j in temppred.values:
                            print('\n Prediction:',str(i),'   Prediction Type:',str(j))
                        again_ch=input('\n\n Enter 1 for another prediction, otherwise press enter to return to welcome_screen. ')
                        if again_ch=='1':
                            return welcome_screen('10',today_d)
                        else:
                            return welcome_screen('0',today_d)
                    else:
                        inc_inp=input(' Must enter a value from 1-12. Enter 1 to try again. Otherwise press enter to return to welcome screen.')
                        if inc_inp == '1':
                            return welcome_screen('10',today_d)
                        else:
                            return welcome_screen('0',today_d)
                except:
                    inc_inp=input(' Value entered not a number. Enter 1 to try again. Otherwise press enter to return to welcome screen. ')
                    if inc_inp == '1':
                        return welcome_screen('10',today_d)
                    else:
                        return welcome_screen('0',today_d)                
            else:
                inc_inp=input(' Number of games entered is either too large or too small. Enter 1 to try again. Otherwise press enter to return to welcome screen. ')
                if inc_inp == '1':
                    return welcome_screen('10',today_d)
                else:
                    return welcome_screen('0',today_d)
        except:
            inc_inp=input(' Value entered not a number. Enter 1 to try again. Otherwise press enter to return to welcome screen. ')
            if inc_inp == '1':
                return welcome_screen('10',today_d)
            else:
                return welcome_screen('0',today_d)
    
    ### OPTION 11 generate a bunch of 12 number predictions
    if choice == '11':
        pred_gen(def_prev_l,def_spot_l)
        input('\n\n Predictions have been generated and stored. Press Enter to return to welcome screen.')
        return welcome_screen('0',today_d)    
    ### OPTION 12
    if choice == '12':
        pred_size=len(dfpred[dfpred['profit'].isna()])
        dfnpreds=dfpred[['drawNumber','prediction','predictionType']].tail(pred_size)
        if len(dfnpreds)>0:
            print('\n All predictions listed have yet to finish 10 game cycle:\n')
            for i,j,k in dfnpreds.values:
                print(' ',i,' - ',str(j),' - ',k)
            input('\n Press Enter to return to welcome screen.')
            return welcome_screen('0',today_d)
        else:
            input('\n\n No unfinished predictions currently stored. Press enter to return to welcome screen.')
            return welcome_screen('0',today_d)
    ### OPTION 13
    if choice == '13':
        print(' ')
        start_update()
        input('\n Databases updated. Press enter to return to welcome screen. ')
        return welcome_screen('0',today_d)    
    ### OPTION 14
    if choice == '14':
        check_dfpred()
        dfpredtr=dfpred[dfpred['profit'].isna()==False]
        if len(dfpredtr)>=500000:
            preddirL=os.listdir('KENO')
            tmpdir=[]
            for i in preddirL:
                if i.startswith('dfpred'):
                    tmpdir.append(i)
            dirnum=str(int(len(tmpdir)))            
            dfpredtr.to_pickle('KENO//dfpred'+dirnum+'.pkl')
            dfpred=dfpred[dfpred['profit'].isna()]
            dfpred.reset_index(drop=True,inplace=True)
            dfpred.to_pickle('KENO//dfpred.pkl')
        print('\n The prediction database has been updated.')
        print(' There are still',str(len(dfpred[dfpred['profit'].isna()])),'predictions with games remaining.')
        input('\n Press Enter to return to welcome screen')
        return welcome_screen('0',today_d)    
    ### OPTION 15
    if choice == '15':        
        print('\n Saving datasets...')
        dfat.to_pickle('KENO//KENO_alltime.pkl')
        print(' ...')
        dfpred.to_pickle('KENO//dfpred.pkl')
        print(' Done.')
        input('\n Press enter to continue to welcome screen.')
        return welcome_screen('0',today_d)
    ### OPTION 16
    if choice == '16':
        if os.name == 'posix':
            os.system("printf '\e[8;20;38t'")    
        else:
            os.system('mode con: cols=38 lines=20')
        num_loops=1
        lastdraw=dfat['drawNumber'].iloc[-1]
        try:
            while(True):
                start=time.time()
                cur_time=time.ctime().split()[3]            
                os.system('cls' if os.name == 'nt' else 'clear')            
                print('\n\n      Automatic mode enabled...')
                print('\n\n Update initialized.')
                start_update()
                if (dfat['drawNumber'].iloc[-1]==lastdraw)&(num_loops>1):
                    if '01:00:00'<=cur_time<'05:00:00':
                        print(' Updating previous predictions...')
                        check_dfpred()
                        dfpredtr=dfpred[dfpred['profit'].isna()==False]
                        if len(dfpredtr)>=500000:
                            preddirL=os.listdir('KENO')
                            tmpdir=[]
                            for i in preddirL:
                                if i.startswith('dfpred'):
                                    tmpdir.append(i)
                            dirnum=str(int(len(tmpdir)))
                            print(' Refreshing prediction dataset...')
                            dfpredtr.to_pickle('KENO//dfpred'+dirnum+'.pkl')
                            dfpred=dfpred[dfpred['profit'].isna()]
                            dfpred.reset_index(drop=True,inplace=True)
                            dfpred.to_pickle('KENO//dfpred.pkl')
                        save_all_pickle()
                        os.system('cls' if os.name == 'nt' else 'clear')
                        now=datetime.datetime.now()
                        target=datetime.datetime(now.year,now.month,now.day,5,0,30)
                        tdelta=target-now                        
                        print('\n\n\n Keno is currently down.\n Automatic mode will continue\n at 5:00 AM EST.')
                        time.sleep(tdelta.total_seconds())
                        continue
                    else:
                        print('\n Games haven\'t been updated online\n since last predictions.\n Trying again in 30 seconds...')
                        time.sleep(30)
                        continue
                if num_loops%5==0:
                    print(' Updating previous predictions...')
                    check_dfpred()
                    dfpredtr=dfpred[dfpred['profit'].isna()==False]
                    if len(dfpredtr)>=500000:
                        preddirL=os.listdir('KENO')
                        tmpdir=[]
                        for i in preddirL:
                            if i.startswith('dfpred'):
                                tmpdir.append(i)
                        dirnum=str(int(len(tmpdir)))
                        print(' Refreshing prediction dataset...')
                        dfpredtr.to_pickle('KENO//dfpred'+dirnum+'.pkl')
                        dfpred=dfpred[dfpred['profit'].isna()]
                        dfpred.reset_index(drop=True,inplace=True)
                        dfpred.to_pickle('KENO//dfpred.pkl')
                print(' Generating new predictions...')
                pred_gen(def_prev_l,def_spot_l)
                save_all_pickle()
                lastdraw=dfpred['drawNumber'].iloc[-1]
                print('\n Finished loop', str(num_loops),'successfully.\n Press CTRL+C to exit.\n')
                num_loops+=1
                end=time.time()
                total_time=end-start
                try:
                    tt_sleep=240-total_time
                    time.sleep(tt_sleep)
                    continue
                except:
                    continue
        except KeyboardInterrupt:
            return welcome_screen('0',today_d)
        except ConnectionError or ConnectionAbortedError or ConnectionRefusedError or ConnectionResetError:
            os.system('cls' if os.name == 'nt' else 'clear') 
            print('\n\n Connection error occurred.\n Trying again in 5 minutes...\n\n')
            time.sleep(300)
            return welcome_screen('16',today_d)        
        except:
            os.system('cls' if os.name == 'nt' else 'clear') 
            print('\n\n Error Occured.\n Potentially connection error.\n Trying again in 5 minutes...\n\n')
            time.sleep(300)
            return welcome_screen('16',today_d)
    ### OPTION complete save
    if choice == 'save':
        save_all()
        input('\n Press enter to continue to welcome screen.')
        return welcome_screen('0',today_d)
    ### CLOSE
    if (choice == 'x') or (choice=='/'):
        return ''
    ### INCORRECT OPTION
    else:
        input('\n Value entered doesn\'t exist. Press enter to continue...\n')
        return welcome_screen('0',today_d)

def initialize_keno():
    try:
        print(' Initializing KENO updater...')
        start_update()    
        today_d=str(date.today())
        welcome_screen('0', today_d)
    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n\n Error occured. Restarting application...\n\n')
        initialize_keno()

initialize_keno()
