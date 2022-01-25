#!/usr/bin/env python3
import pandas as pd
import numpy as np
import os
pd.set_option('display.max_rows',None,'display.max_columns',None)

print('\n Creating variables...')
def_spot_l=[6,7,12]
def_prev_l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,25,50,100,200,300,600,900,1200,1500,1800,2100]
drop_cols=['correct1', 'numbersHit1', 'correct2', 'numbersHit2',
       'correct3', 'numbersHit3', 'correct4', 'numbersHit4', 'correct5',
       'numbersHit5', 'correct6', 'numbersHit6', 'correct7', 'numbersHit7',
       'correct8', 'numbersHit8', 'correct9', 'numbersHit9', 'correct10',
       'numbersHit10', 'winningGamesN']
predCols=['N-N','N-N/2','N-N/3','N-N/4','N/maxt+N/mina','top1td','top1td-N/3','top2td','top2td-N/3','top3td','top3td-N/3',
'xN-N', 'xN-N/2', 'xN-N/3', 'xN-N/4', 'xN/maxt+N/mina', 'xtop1td', 'xtop1td-N/3', 'xtop2td', 'xtop2td-N/3', 'xtop3td', 'xtop3td-N/3', 'meanPrev','zA4','zlNN-at','zlN-2at','zN-2at']
ptype=['N-N', 'N-N/2', 'N-N/3', 'N-N/4', 'N/maxt+N/mina', 'top1td', 'top1td-N/3', 'top2td', 'top2td-N/3', 'top3td', 'top3td-N/3']
pXtype=['xN-N', 'xN-N/2', 'xN-N/3', 'xN-N/4', 'xN/maxt+N/mina', 'xtop1td', 'xtop1td-N/3', 'xtop2td', 'xtop2td-N/3', 'xtop3td', 'xtop3td-N/3']
pZtype=['zA4','zlNN-at','zlN-2at','zN-2at']

print(' Importinging datasets...')
print(' df1...')
df1=pd.read_pickle('KENO//dfpred1.pkl')
df1.drop(columns=drop_cols, inplace=True)
print(' df2...')
df2=pd.read_pickle('KENO//dfpred2.pkl')
df2.drop(columns=drop_cols, inplace=True)
print(' df3...')
df3=pd.read_pickle('KENO//dfpred3.pkl')
df3.drop(columns=drop_cols, inplace=True)
print(' df4...')
df4=pd.read_pickle('KENO//dfpred4.pkl')
df4.drop(columns=drop_cols, inplace=True)
print(' df5...')
df5=pd.read_pickle('KENO//dfpred5.pkl')
df5.drop(columns=drop_cols, inplace=True)
print(' df6...')
df6=pd.read_pickle('KENO//dfpred6.pkl')
df6.drop(columns=drop_cols, inplace=True)
print(' df7...')
df7=pd.read_pickle('KENO//dfpred7.pkl')
df7.drop(columns=drop_cols, inplace=True)
print(' df8...')
df8=pd.read_pickle('KENO//dfpred8.pkl')
df8.drop(columns=drop_cols, inplace=True)
print(' df9...')
df9=pd.read_pickle('KENO//dfpred9.pkl')
df9.drop(columns=drop_cols, inplace=True)
print(' df10...')
df10=pd.read_pickle('KENO//dfpred10.pkl')
df10.drop(columns=drop_cols, inplace=True)
print(' df11...')
df11=pd.read_pickle('KENO//dfpred11.pkl')
df11.drop(columns=drop_cols, inplace=True)
print(' df12...')
df12=pd.read_pickle('KENO//dfpred12.pkl')
df12.drop(columns=drop_cols, inplace=True)
print(' df13...')
df13=pd.read_pickle('KENO//dfpred13.pkl')
df13.drop(columns=drop_cols, inplace=True)
print(' df14...')
df14=pd.read_pickle('KENO//dfpred14.pkl')
df14.drop(columns=drop_cols, inplace=True)
print(' df15...')
df15=pd.read_pickle('KENO//dfpred15.pkl')
df15.drop(columns=drop_cols, inplace=True)
print(' df16...')
df16=pd.read_pickle('KENO//dfpred16.pkl')
df16.drop(columns=drop_cols, inplace=True)
print(' df17...')
df17=pd.read_pickle('KENO//dfpred17.pkl')
df17.drop(columns=drop_cols, inplace=True)
print(' df18...')
df18=pd.read_pickle('KENO//dfpred18.pkl')
df18.drop(columns=drop_cols, inplace=True)
print(' df19...')
df19=pd.read_pickle('KENO//dfpred19.pkl')
df19.drop(columns=drop_cols, inplace=True)
print(' df20...')
df20=pd.read_pickle('KENO//dfpred20.pkl')
df20.drop(columns=drop_cols, inplace=True)
print(' df21...')
df21=pd.read_pickle('KENO//dfpred21.pkl')
df21.drop(columns=drop_cols, inplace=True)
print(' df22...')
df22=pd.read_pickle('KENO//dfpred22.pkl')
df22.drop(columns=drop_cols, inplace=True)
print(' df23...')
df23=pd.read_pickle('KENO//dfpred23.pkl')
df23.drop(columns=drop_cols, inplace=True)
print(' df24...')
df24=pd.read_pickle('KENO//dfpred24.pkl')
df24.drop(columns=drop_cols, inplace=True)
print(' df25...')
df25=pd.read_pickle('KENO//dfpred25.pkl')
df25.drop(columns=drop_cols, inplace=True)
print(' df26...')
df26=pd.read_pickle('KENO//dfpred26.pkl')
df26.drop(columns=drop_cols, inplace=True)
print(' df27...')
df27=pd.read_pickle('KENO//dfpred27.pkl')
df27.drop(columns=drop_cols, inplace=True)
print(' df28...')
df28=pd.read_pickle('KENO//dfpred28.pkl')
df28.drop(columns=drop_cols, inplace=True)
print(' df29...')
df29=pd.read_pickle('KENO//dfpred29.pkl')
df29.drop(columns=drop_cols, inplace=True)
print(' df30...')
df30=pd.read_pickle('KENO//dfpred30.pkl')
df30.drop(columns=drop_cols, inplace=True)
print(' df31...')
df31=pd.read_pickle('KENO//dfpred31.pkl')
df31.drop(columns=drop_cols, inplace=True)
print(' df32...')
df32=pd.read_pickle('KENO//dfpred32.pkl')
df32.drop(columns=drop_cols, inplace=True)
print(' df33...')
df33=pd.read_pickle('KENO//dfpred33.pkl')
df33.drop(columns=drop_cols, inplace=True)
print(' df34...')
df34=pd.read_pickle('KENO//dfpred34.pkl')
df34.drop(columns=drop_cols, inplace=True)
print(' df35...')
df35=pd.read_pickle('KENO//dfpred35.pkl')
df35.drop(columns=drop_cols, inplace=True)
print(' df36...')
df36=pd.read_pickle('KENO//dfpred36.pkl')
df36.drop(columns=drop_cols, inplace=True)
print(' df37...')
df37=pd.read_pickle('KENO//dfpred37.pkl')
df37.drop(columns=drop_cols, inplace=True)
print(' df38...')
df38=pd.read_pickle('KENO//dfpred38.pkl')
df38.drop(columns=drop_cols, inplace=True)
print(' df39...')
df39=pd.read_pickle('KENO//dfpred39.pkl')
df39.drop(columns=drop_cols, inplace=True)
print(' df40...')
df40=pd.read_pickle('KENO//dfpred40.pkl')
df40.drop(columns=drop_cols, inplace=True)
print(' df41...')
df41=pd.read_pickle('KENO//dfpred41.pkl')
df41.drop(columns=drop_cols, inplace=True)
print(' df42...')
df42=pd.read_pickle('KENO//dfpred42.pkl')
df42.drop(columns=drop_cols, inplace=True)
print(' df43...')
df43=pd.read_pickle('KENO//dfpred43.pkl')
df43.drop(columns=drop_cols, inplace=True)
print(' df44...')
df44=pd.read_pickle('KENO//dfpred44.pkl')
df44.drop(columns=drop_cols, inplace=True)
print(' df45...')
df45=pd.read_pickle('KENO//dfpred45.pkl')
df45.drop(columns=drop_cols, inplace=True)
print(' df46...')
df46=pd.read_pickle('KENO//dfpred46.pkl')
df46.drop(columns=drop_cols, inplace=True)
print(' df47...')
df47=pd.read_pickle('KENO//dfpred47.pkl')
df47.drop(columns=drop_cols, inplace=True)
print(' df48...')
df48=pd.read_pickle('KENO//dfpred48.pkl')
df48.drop(columns=drop_cols, inplace=True)
print(' df49...')
df49=pd.read_pickle('KENO//dfpred49.pkl')
df49.drop(columns=drop_cols, inplace=True)
print(' df50...')
df50=pd.read_pickle('KENO//dfpred50.pkl')
df50.drop(columns=drop_cols, inplace=True)
print(' df51...')
df51=pd.read_pickle('KENO//dfpred51.pkl')
df51.drop(columns=drop_cols, inplace=True)
print(' df52...')
df52=pd.read_pickle('KENO//dfpred52.pkl')
df52.drop(columns=drop_cols, inplace=True)
print(' df53...')
df53=pd.read_pickle('KENO//dfpred53.pkl')
df53.drop(columns=drop_cols, inplace=True)
print(' df54...')
df54=pd.read_pickle('KENO//dfpred54.pkl')
df54.drop(columns=drop_cols, inplace=True)
print(' df55...')
df55=pd.read_pickle('KENO//dfpred55.pkl')
df55.drop(columns=drop_cols, inplace=True)
print(' df56...')
df56=pd.read_pickle('KENO//dfpred56.pkl')
df56.drop(columns=drop_cols, inplace=True)
print(' df57...')
df57=pd.read_pickle('KENO//dfpred57.pkl')
df57.drop(columns=drop_cols, inplace=True)
print(' df58...')
df58=pd.read_pickle('KENO//dfpred58.pkl')
df58.drop(columns=drop_cols, inplace=True)
print(' df59...')
df59=pd.read_pickle('KENO//dfpred59.pkl')
df59.drop(columns=drop_cols, inplace=True)
print(' df60...')
df60=pd.read_pickle('KENO//dfpred60.pkl')
df60.drop(columns=drop_cols, inplace=True)
print(' df61...')
df61=pd.read_pickle('KENO//dfpred61.pkl')
df61.drop(columns=drop_cols, inplace=True)
print(' df62...')
df62=pd.read_pickle('KENO//dfpred62.pkl')
df62.drop(columns=drop_cols, inplace=True)
print(' dfpred...')
dfpredC=pd.read_pickle('KENO//dfpred.pkl')
dfpredC.drop(columns=drop_cols, inplace=True)
print(' Removing incomplete predictions...')
dfpredC=dfpredC[dfpredC['profit'].isna()==False]

print(' Combining datasets...')
dflist=[df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,\
    df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24,df25,\
    df26,df27,df28,df29,df30,df31,df32,df33,df34,df35,df36,df37,\
    df38,df39,df40,df41,df42,df43,df44,df45,df46,df47,df48,df49,\
    df50,df51,df52,df53,df54,df55,df56,df57,df58,df59,df60,df61,\
    df62,dfpredC]
dfpredA=pd.concat(dflist)
dfpredA.reset_index(drop=True,inplace=True)

print(' Removing old datasets...')
del df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,\
    df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24,df25,\
    df26,df27,df28,df29,df30,df31,df32,df33,df34,df35,df36,df37,\
    df38,df39,df40,df41,df42,df43,df44,df45,df46,df47,df48,df49,\
    df50,df51,df52,df53,df54,df55,df56,df57,df58,df59,df60,df61,\
    df62,dfpredC

print(' Creating new datasets...')
print(' dfpred6...')
dfpred6=dfpredA.to_dict('series')
dfpred6_ind=dfpred6['totalSpots'][dfpred6['totalSpots']==6].index
for col6 in dfpred6:
    dfpred6[col6]=dfpred6[col6].iloc[dfpred6_ind]
    dfpred6[col6].reset_index(drop=True,inplace=True)
dfpred6=pd.DataFrame(data=dfpred6)
print(' dfpred7...')
dfpred7=dfpredA.to_dict('series')
dfpred7_ind=dfpred7['totalSpots'][dfpred7['totalSpots']==7].index
for col7 in dfpred7:
    dfpred7[col7]=dfpred7[col7].iloc[dfpred7_ind]
    dfpred7[col7].reset_index(drop=True,inplace=True)
dfpred7=pd.DataFrame(data=dfpred7)
print(' dfpred12...')
dfpred12=dfpredA.to_dict('series')
dfpred12_ind=dfpred12['totalSpots'][dfpred12['totalSpots']==12].index
for col12 in dfpred12:
    dfpred12[col12]=dfpred12[col12].iloc[dfpred12_ind]
    dfpred12[col12].reset_index(drop=True,inplace=True)
dfpred12=pd.DataFrame(data=dfpred12)

print(' dfpredO6...')
dfpredO6d=dfpred6.to_dict('series')
dfpredO6_ind=dfpredO6d['predictionType'][dfpredO6d['predictionType'].isin(ptype)].index
for colO6 in dfpredO6d:
    dfpredO6d[colO6]=dfpredO6d[colO6].iloc[dfpredO6_ind]
    dfpredO6d[colO6].reset_index(drop=True,inplace=True)
print(' dfpredO7...')
dfpredO7d=dfpred7.to_dict('series')
dfpredO7_ind=dfpredO7d['predictionType'][dfpredO7d['predictionType'].isin(ptype)].index
for colO7 in dfpredO7d:
    dfpredO7d[colO7]=dfpredO7d[colO7].iloc[dfpredO7_ind]
    dfpredO7d[colO7].reset_index(drop=True,inplace=True)
print(' dfpredO12...')
dfpredO12d=dfpred12.to_dict('series')
dfpredO12_ind=dfpredO12d['predictionType'][dfpredO12d['predictionType'].isin(ptype)].index
for colO12 in dfpredO12d:
    dfpredO12d[colO12]=dfpredO12d[colO12].iloc[dfpredO12_ind]
    dfpredO12d[colO12].reset_index(drop=True,inplace=True)

print(' dfpredX6...')
dfpredX6d=dfpred6.to_dict('series')
dfpredX6_ind=dfpredX6d['predictionType'][dfpredX6d['predictionType'].isin(pXtype)].index
for colX6 in dfpredX6d:
    dfpredX6d[colX6]=dfpredX6d[colX6].iloc[dfpredX6_ind]
    dfpredX6d[colX6].reset_index(drop=True,inplace=True)
print(' dfpredX7...')
dfpredX7d=dfpred7.to_dict('series')
dfpredX7_ind=dfpredX7d['predictionType'][dfpredX7d['predictionType'].isin(pXtype)].index
for colX7 in dfpredX7d:
    dfpredX7d[colX7]=dfpredX7d[colX7].iloc[dfpredX7_ind]
    dfpredX7d[colX7].reset_index(drop=True,inplace=True)
print(' dfpredX12...')
dfpredX12d=dfpred12.to_dict('series')
dfpredX12_ind=dfpredX12d['predictionType'][dfpredX12d['predictionType'].isin(pXtype)].index
for colX12 in dfpredX12d:
    dfpredX12d[colX12]=dfpredX12d[colX12].iloc[dfpredX12_ind]
    dfpredX12d[colX12].reset_index(drop=True,inplace=True)

print(' dfpredZ6...')
dfpredZ6d=dfpred6.to_dict('series')
dfpredZ6_ind=dfpredZ6d['predictionType'][dfpredZ6d['predictionType'].isin(pZtype)].index
for colZ6 in dfpredZ6d:
    dfpredZ6d[colZ6]=dfpredZ6d[colZ6].iloc[dfpredZ6_ind]
    dfpredZ6d[colZ6].reset_index(drop=True,inplace=True)
print(' dfpredZ7...')
dfpredZ7d=dfpred7.to_dict('series')
dfpredZ7_ind=dfpredZ7d['predictionType'][dfpredZ7d['predictionType'].isin(pZtype)].index
for colZ7 in dfpredZ7d:
    dfpredZ7d[colZ7]=dfpredZ7d[colZ7].iloc[dfpredZ7_ind]
    dfpredZ7d[colZ7].reset_index(drop=True,inplace=True)
print(' dfpredZ12...')
dfpredZ12d=dfpred12.to_dict('series')
dfpredZ12_ind=dfpredZ12d['predictionType'][dfpredZ12d['predictionType'].isin(pZtype)].index
for colZ12 in dfpredZ12d:
    dfpredZ12d[colZ12]=dfpredZ12d[colZ12].iloc[dfpredZ12_ind]
    dfpredZ12d[colZ12].reset_index(drop=True,inplace=True)

print(' Creating dataset variables and definitions...')
dfpred6.name='dfpred6'
dfpred7.name='dfpred7'
dfpred12.name='dfpred12'
dataframesNames=['dfpred6','dfpred7','dfpred12']
dataframes=[dfpred6,dfpred7,dfpred12]
predIndex=pd.MultiIndex.from_product([dataframesNames,def_prev_l],names=['dataframe','prevGameN'])
dfprmean=pd.DataFrame(columns=predCols, index=predIndex)

def chpM(spots,prevN,predT):
    for spot in spots:
        dfLoc='dfpred'+str(spot)
        for num in prevN:
            for ptype in predT:
                print(dfprmean.loc[(dfLoc,num),ptype])
    return None

def prTvc(spots,prevN,predT):
    dfimportant=dfpredA.loc[(dfpredA['predictionType']==predT)&(dfpredA['previousGameN']==prevN)&(dfpredA['totalSpots']==spots)]
    print(dfimportant['profit'].value_counts())
    print('\n  Number of predictions:',len(dfimportant),'   Profit:',dfimportant['profit'].sum(),'\n')
    return None

def save_all():
    print('\n Saving...')
    dfprmean.to_csv('KENO//dfprmean.csv',mode='a')
    print(' ...')
    dfgpO.to_csv('KENO//dfgpO.csv',mode='a')
    print(' ...')
    dfgpX.to_csv('KENO//dfgpX.csv',mode='a')
    print(' ...')
    dfgpZ.to_csv('KENO//dfgpZ.csv',mode='a')
    return None

print(' Creating means dataframe...')
for dframe in dataframes:
    for prevN in def_prev_l:
        for predT in predCols:
            tempdf=dframe.to_dict('series')
            tempdf_ind=tempdf['previousGameN'][tempdf['previousGameN']==prevN].index
            for coltemp in tempdf:
                tempdf[coltemp]=tempdf[coltemp].iloc[tempdf_ind]
                tempdf[coltemp].reset_index(drop=True,inplace=True)
            tempdfT_ind=tempdf['predictionType'][tempdf['predictionType']==predT].index
            for coltempT in tempdf:
                tempdf[coltempT]=tempdf[coltempT].iloc[tempdfT_ind]
                tempdf[coltempT].reset_index(drop=True,inplace=True)
            #tempdf=dframe.loc[(dframe['previousGameN']==prevN)&(dframe['predictionType']==predT)]
            dfprmean.loc[(dframe.name,prevN),predT]=tempdf['profit'].mean()
dfprmean['meanPrev']=dfprmean.mean(axis=1)
prS=pd.Series(np.nan, index=predCols, name=('meanType', ''))
dfprmean=dfprmean.append(prS)
dfprmean.loc[('meanType','')]=dfprmean.mean(axis=0)

print(' Creating normal prediction green combinations dataset...')
greenpredsO=[]
for pind in dfprmean.index:    
    for pcol in ptype:
        if dfprmean.loc[pind,pcol]>=0:
            mval=dfprmean.loc[pind,pcol]
            greenpredsO.append([pind,pcol,mval])
dfgpO=pd.DataFrame(data=greenpredsO, columns=['(dFrame,prevN)','pType','mean'])

print(' Creating positional prediction green combinations dataset...')
greenpredsX=[]
for pindX in dfprmean.index:    
    for pcolX in pXtype:
        if dfprmean.loc[pindX,pcolX]>=0:
            mvalX=dfprmean.loc[pindX,pcolX]
            greenpredsX.append([pindX,pcolX,mvalX])
dfgpX=pd.DataFrame(data=greenpredsX, columns=['(dFrame,prevN)','pXType','mean'])

print(' Creating mixed prediction green combinations dataset...')
greenpredsZ=[]
for pindZ in dfprmean.index:    
    for pcolZ in pZtype:
        if dfprmean.loc[pindZ,pcolZ]>=0:
            mvalZ=dfprmean.loc[pindZ,pcolZ]
            greenpredsZ.append([pindZ,pcolZ,mvalZ])
dfgpZ=pd.DataFrame(data=greenpredsZ, columns=['(dFrame,prevN)','pZType','mean'])

def pred_intro(predinput):
    os.system('cls' if os.name == 'nt' else 'clear')
    if predinput == '0':
        os.system('cls' if os.name == 'nt' else 'clear')
        predintro='''
        1. See complete mean dataset.
        2. See positive mean regular-type predictions.
        3. See positive mean positional-type predictions.
        4. See positive mean mixed-type predictions.
        5. Check mean profit of a prediction combination.
        6. Check value counts of a prediction combination.
        7. Save analysis datasets.'''
        print('\n\n Prediction Analysis.')
        print('\n Number of 7 spot predictions: ',len(dfpred7.loc[(dfpred7['previousGameN']==7)&(dfpred7['predictionType']=='N-N')]))
        print(' Number of 6/12 spot predictions: ',len(dfpred12.loc[(dfpred12['previousGameN']==17)&(dfpred12['predictionType']=='N-N')]))
        print(' Number of positional-type predictions: ',len(dfpred12.loc[(dfpred12['previousGameN']==17)&(dfpred12['predictionType']=='xN-N')]))
        print(' Number of mixed-type predictions: ',len(dfpred12.loc[(dfpred12['previousGameN']==17)&(dfpred12['predictionType']=='zA4')]))
        print(predintro)
        predinput=input('\n Which option would you like? ')
        os.system('cls' if os.name == 'nt' else 'clear')
    if predinput == '1':
        print('\n\n Complete Means dataset:\n\n',dfprmean)
        input('\n Press Enter to return to home screen. ')
        return pred_intro('0')
    if predinput == '2':
        print('\n\n Green Regular Predictions:\n\n',dfgpO)
        input('\n Press Enter to return to home screen. ')
        return pred_intro('0')
    if predinput == '3':
        print('\n\n Green Placement Predictions:\n\n',dfgpX)
        input('\n Press Enter to return to home screen. ')
        return pred_intro('0')
    if predinput == '4':
        print('\n\n Green Mixed Predictions:\n\n',dfgpZ)
        input('\n Press Enter to return to home screen. ')
        return pred_intro('0')
    if predinput == '5':
        print('\n\n Number of spots options: ',def_spot_l,'\n')
        tspots=input(' Number of spots: ')
        try:
            tspots=int(tspots)
            print('\n Previous game options: ',def_prev_l,'\n')
            tprevN=input(' Number of previous games: ')
            try:
                tprevN=int(tprevN)
                print('\n Prediction types: ',predCols,'\n')
                tpredT=input(' Type of prediction: ')
                try:
                    chpM(tspots,tprevN,tpredT)
                    tryag=input('\n Enter 1 to try another prediction combination.\n Otherwise, press Enter to return to home screen.')
                    if tryag=='1':
                        return pred_intro('5')
                    else:
                        return pred_intro('0')
                except:
                    tryag=input('\n You did not enter a correct prediction type.\n Enter 1 to try again.\n Otherwise press Enter to return to home screen.: ')
                    if tryag=='1':
                        return pred_intro('5')
                    else:
                        return pred_intro('0')
            except:
                tryag=input('\n You did not enter a correct previous game number.\n Enter 1 to try again.\n Otherwise press Enter to return to home screen.: ')
                if tryag=='1':
                    return pred_intro('5')
                else:
                    return pred_intro('0')
        except:
            tryag=input('\n You did not enter a correct number of spots. Enter 1 to try again.\n Otherwise press Enter to return to home screen.: ')
            if tryag=='1':
                return pred_intro('5')
            else:
                return pred_intro('0')
    if predinput == '6':
        print('\n\n Number of spots options: ',def_spot_l,'\n')
        tspots=input(' Number of spots: ')
        try:
            tspots=int(tspots)
            print('\n Previous game options: ',def_prev_l,'\n')
            tprevN=input(' Number of previous games: ')
            try:
                tprevN=int(tprevN)
                print('\n Prediction types: ',predCols,'\n')
                tpredT=input(' Type of prediction: ')
                try:
                    prTvc(tspots,tprevN,tpredT)
                    tryag=input('\n Enter 1 to try another prediction combination.\n Otherwise, press Enter to return to home screen.')
                    if tryag=='1':
                        return pred_intro('6')
                    else:
                        return pred_intro('0')
                except:
                    tryag=input('\n You did not enter a correct prediction type.\n Enter 1 to try again.\n Otherwise press Enter to return to home screen.: ')
                    if tryag=='1':
                        return pred_intro('6')
                    else:
                        return pred_intro('0')
            except:
                tryag=input('\n You did not enter a correct previous game number.\n Enter 1 to try again.\n Otherwise press Enter to return to home screen.: ')
                if tryag=='1':
                    return pred_intro('6')
                else:
                    return pred_intro('0')
        except:
            tryag=input('\n You did not enter a correct number of spots. Enter 1 to try again.\n Otherwise press Enter to return to home screen.: ')
            if tryag=='1':
                return pred_intro('6')
            else:
                return pred_intro('0')
    if predinput == '7':
        save_all()
        print(' Done.')
        input('\n Press Enter to return to home screen. ')
        return pred_intro('0')

def boot_up():
    try:
        pred_intro('0')
    except:
        input('Something went wrong. Press Enter to reload home screen. ')
        return boot_up()

boot_up()
