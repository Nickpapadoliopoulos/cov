import csv
import pandas as pd
import numpy as np
from itertools import combinations

#path = "C:\\Users\\User\\Downloads\\"
path = "/home/workstation/papadio/"
filename = "data-1.csv"

history_days = 252*2

#df = pd.read_csv(r"C:\Users\User\Downloads\data.csv", sep=",") #headers
df = pd.read_csv(str(path + filename), sep=",") #headers
df = df.iloc[:, 1:] ## not needed
df = df.set_index('index')

#ty = df[df['index'] >= '2019-05-31']
ty = df.tail(history_days)
# prices // pandas tail last history_days
roc = ty.pct_change()

# pct_change() in another varialbe roc

#combinations
print(ty.head)
print(roc.head)

# ty['EBAY.Close_log'] = np.log(ty['EBAY.Close']/ty['EBAY.Close'].shift(1))
# ty['LEN.Close_log'] = np.log(ty['LEN.Close']/ty['LEN.Close'].shift(1))
# ty['TSN.Close_log'] = np.log(ty['TSN.Close']/ty['TSN.Close'].shift(1))
# ty['KR.Close_log'] = np.log(ty['KR.Close']/ty['KR.Close'].shift(1))
# ty['IP.Close_log'] = np.log(ty['IP.Close']/ty['IP.Close'].shift(1))
# ty['AN.Close_log'] = np.log(ty['AN.Close']/ty['AN.Close'].shift(1))
# ty['LPX.Close_log'] = np.log(ty['LPX.Close']/ty['LPX.Close'].shift(1))
# ty['CROX.Close_log'] = np.log(ty['CROX.Close']/ty['CROX.Close'].shift(1))
# ty['MTH.Close_log'] = np.log(ty['MTH.Close']/ty['MTH.Close'].shift(1))
# ty['ATKR.Close_log'] = np.log(ty['ATKR.Close']/ty['ATKR.Close'].shift(1))

roc_cov = roc.cov()
print(roc_cov)

triplets = list(combinations(roc_cov.columns,3) )
print(triplets)

triplet_array=[]
for trip in triplets:
    # trip_array = np.asarray(trip) <- kanei th lista array
    # elements = ty[trip_array]     <- dialegei ta elements (tripleta) mesa sto ty
    # elements.cov()                <- vriskei to cov mesa sthn tripleta
    trip_cov = roc[np.asarray(trip)].cov()
    #print(trip_cov)
    #print(np.diag(trip_cov))
    var_sum = sum(np.diag(trip_cov))
    #print(var_sum)
    covar_sum = sum(sum(trip_cov.to_numpy()))-var_sum  #<- to .to_numpy() metatrepei to dataframe se array
    #print(covar_sum)
    triplet_array.append({"triplet": trip, "var": var_sum, "covar": covar_sum})

print(triplet_array[2])
exit()
mean1 = roc.mean('FCX.Close')
k_1 =roc['FCX.Close']-mean1

mean2 = roc['EBAY.Close'].mean()
k_2 =roc['EBAY.Close']-mean2

mean3 = roc['LEN.Close'].mean()
k_3 =roc['LEN.Close']-mean3

mean4 = roc['TSN.Close'].mean()
k_4 =roc['TSN.Close']-mean4

mean5 = roc['KR.Close'].mean()
k_5 =roc['KR.Close']-mean5

mean6 = roc['IP.Close'].mean()
k_6 =roc['IP.Close']-mean6

mean7 = roc['AN.Close'].mean()
k_7 =roc['AN.Close']-mean7

mean8 = roc['LPX.Close'].mean()
k_8 =roc['LPX.Close']-mean8

mean9 = roc['CROX.Close'].mean()
k_9 =roc['CROX.Close']-mean9

mean10 = roc['MTH.Close'].mean()
k_10 =roc['MTH.Close']-mean10

mean11 = roc['ATKR.Close'].mean()
k_11 =roc['ATKR.Close']-mean11
#Total Sum of Squares
TSS_1 = k_1.dot(k_1)
TSS_2 = k_2.dot(k_2)
TSS_3 = k_3.dot(k_3)
TSS_4 = k_4.dot(k_4)
TSS_5 = k_5.dot(k_5)
TSS_6 = k_6.dot(k_6)
TSS_7 = k_7.dot(k_7)
TSS_8 = k_8.dot(k_8)

print(roc)




