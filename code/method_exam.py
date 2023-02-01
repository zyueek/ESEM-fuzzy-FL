import os 
import sys
import pandas as pd
import argparse
from pandas.core.frame import DataFrame
from tqdm import *
if __name__ == "__main__":
  parser=argparse.ArgumentParser()
  parser.add_argument('--project',required=True)
  parser.add_argument('--num',required=True)
  parser.add_argument('--formula',required=True)
  parser.add_argument('--window',required=True)
  args=parser.parse_args()
  pro=args.project
  num=args.num
  formula=args.formula
  win=args.window
  buggyfile="buggyline/"+pro+"_bug.csv"
  df_bug=pd.read_csv(buggyfile)
  buglist=df_bug.iloc[:,0].to_list()
  outname="/root/fld/analysis/method/"+formula+win+".csv"
  df_result=pd.read_csv(outname)
  for i in tqdm(range(int(num))):
#    rankfile=pro+num+"/"+formula+"/totaldefn-elements/"+formula+"_win"+str(win)+".csv"
#    print(rankfile)
#    df=pd.read_csv(rankfile)
#    df["Rank_M"]=df["Suspiciousness"].rank(method="min",ascending=False)
#    df=df.sort_values(by=['Rank_M'],ascending=True)
    bugrank=[]
    totalmethod=[]
    perlist=[]
    outputname=pro+str(i+1)+"/"+formula+"/totaldefn-elements/"+formula+"_win"+str(win)+"_method"+".csv"
#    df.to_csv(outputname,index=False)
#    outputname=pro+str(i+1)+"/fusion/fusion_"+str(formula)+"_win"+str(win)+"method.csv"
    df=pd.read_csv(outputname)
    df_bugnum=df_bug[df_bug["bugid"]==i+1]
    methodnum=len(list(set(df.iloc[:,2].to_list())))
    for j in range(len(df_bugnum)):
      start=df_bugnum.iloc[j,3]
      end=df_bugnum.iloc[j,4]
      
      for k in range(len(df)):
        buggy=df.iloc[k,0]
        sus=df.iloc[k,1]
        methodid=df.iloc[k,2]
        methodname=df.iloc[k,0].split('#',1)[0]
        methodline=int(df.iloc[k,0].split('#',1)[1])
        if(methodname==df_bugnum.iloc[j,1] and start<=methodline<=end):
          df_rank=df[df["Suspiciousness"]>sus]
          stat=df_rank.iloc[:,2].to_list()
          methodrank=len(list(set(stat)))+1
          methodper=methodrank/methodnum
#          bugrank.append(len(methodrank)+1)
#          perlist.append(methodper)
          pronum=pro+str(i+1)
          df_result.loc[len(df_result.index)]=[pronum,methodrank,methodnum,methodper,formula,win,methodid]
          df_result.to_csv(outname,index=False)
          break
#    print(bugrank)
      
       
        
    
  
  
