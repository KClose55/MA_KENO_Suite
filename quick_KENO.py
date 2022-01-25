#!/usr/bin/env python3
import pandas as pd
import requests
from datetime import date
import os

def keno_update(start_d,end_d):
    global dfat, dfnat, dfnvc, today_d, latest_d,dfatX1, dfatX2, dfatX3, dfatX4, dfatX5, dfatX6, dfatX7, dfatX8, dfatX9, dfatX10, dfatX11, dfatX12, dfatX13, dfatX14, dfatX15, dfatX16, dfatX17, dfatX18, dfatX19, dfatX20, dfatXCL
    
    for i in pd.date_range(start=start_d,end=end_d):
        r=requests.get('https://www.masslottery.com/rest/keno/getDrawsByDateRange?startDate='+str(i)+'&endDate='+str(i))
        i_daystr=str(i).split(' ')[0]
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
        dfat=pd.concat([dfat,rjn1])

    dfat.reset_index(drop=True,inplace=True)
    latest_d=dfat['drawDate'].iloc[-1]
    
    dftd=dfat[dfat['drawDate']==today_d]
    dftd.reset_index(drop=True,inplace=True)

    print(' ...')
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

    print(' ...')
    dfnat=sum(dfatXCL)
    dfnvc=pd.DataFrame(columns=['Occurances'],data=dfnat)
    dfnvc.sort_values('Occurances', ascending=False, inplace=True)
    dfnvc['Normalized']=(dfnvc['Occurances']-dfnvc['Occurances'].mean())/dfnvc['Occurances'].std()
    dfnvc['Normalized/N.max()']=dfnvc['Normalized']/dfnvc['Normalized'].max()
    dfnvc['Normalized/N.min()']=dfnvc['Normalized']/dfnvc['Normalized'].min()

def man_upd():
    global dfat, today_d
    if 0<len(dfat[dfat['drawDate']==today_d])<300:
        dfat=dfat[dfat['drawDate']!=today_d]
        return keno_update(today_d,today_d)
    else:
        dfat=dfat[dfat['drawDate']!=latest_d]
        keno_update(latest_d,latest_d)
        return print('')

def draw_pred(c_ch, num_p):
    global dfpred, pred_cols, initpred_cols, dfat, dftd, dfntvc, dfntd, dftdXCL, dftdX1, dftdX2, dftdX3, dftdX4, dftdX5, dftdX6, dftdX7, dftdX8, dftdX9, dftdX10, dftdX11, dftdX12, dftdX13, dftdX14, dftdX15, dftdX16, dftdX17, dftdX18, dftdX19, dftdX20
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

    print(' ...')
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

    dfntvc['Normalized']=(dfntvc['Occurances']-dfntvc['Occurances'].mean())/dfntvc['Occurances'].std()
    dfntvc['Normalized/N.max()']=dfntvc['Normalized']/dfntvc['Normalized'].max()
    dfntvc['Normalized/N.min()']=dfntvc['Normalized']/dfntvc['Normalized'].min()

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
    tdat_p['top3td-N/3']=dfntvc1['Normalized']-(dfnvc['Normalized']/3)

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
    dfpred=pd.DataFrame([pred1row,pred2row,pred3row,pred4row,pred5row, pred6row, pred7row, pred8row, pred9row, pred10row, pred11row], columns=initpred_cols)

def draw_pred_2(c_ch2,num_p2,pred_tp):
    draw_pred(c_ch2,num_p2)
    cur_pred=dfpred[dfpred['predictionType']==pred_tp]
    cur_pred.reset_index(drop=True,inplace=True)
    pred_num=cur_pred['prediction'].iloc[0]
    pred_pr=str(pred_num).strip('][').replace(', ','-')
    print('\n\nSpots:',str(num_p2))
    print('Prediction:',pred_pr)

while True:
    print('\n Generating...')
    dfat=pd.read_pickle('KENO//KENO_alltime.pkl')
    initpred_cols=['drawNumber', 'prediction', 'previousGameN', 'predictionType', 'totalSpots']
    today_d=str(date.today()) 
    latest_d=dfat['drawDate'].iloc[-1]

    if today_d == latest_d:
        man_upd()
    if today_d > latest_d:
        try:
            dfat=dfat[dfat['drawDate']!=latest_d]
            keno_update(latest_d,today_d)
        except:
            dfat=dfat[dfat['drawDate']!=latest_d]
            keno_update(latest_d,latest_d)

    print('\n\nLast Draw Number:', str(dfat['drawNumber'].iloc[-1]))

    
    draw_pred_2(300,6,'N-N/2')
    draw_pred_2(300,7,'N-N/4')
    draw_pred_2(16,12,'N-N/4')

    input('\n\nPress enter to restart...')
    os.system('cls' if os.name == 'nt' else 'clear')
