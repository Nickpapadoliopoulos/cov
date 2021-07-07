import csv
import pandas as pd
import numpy as np
from itertools import combinations

filename = 'data.csv'
history_days = 252*2

df = pd.read_csv(r"C:\Users\User\Downloads\data.csv", sep=",") #headers
df = df.iloc[:, 1:] ## not needed

ty = df[df['index'] >= '2019-05-31']
# prices // pandas tail last history_days

for col in ty.columns[1:]:
    ty[[col+"_log"]] = np.log(ty[col]/ty[col].shift(1))
# pct_change() in another varialbe roc

# roc.cov()

#combinations
print(ty.columns)
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

ty_cov = ty[ty.columns[12:]].cov()
triplets = list(combinations(ty_cov.columns,3) )
print(triplets)

triplet_array=[]
for trip in triplets:
    # trip_array = np.asarray(trip) <- kanei th lista array
    # elements = ty[trip_array]     <- dialegei ta elements (tripleta) mesa sto ty
    # elements.cov()                <- vriskei to cov mesa sthn tripleta
    trip_cov = ty[np.asarray(trip)].cov()
    #print(trip_cov)
    #print(np.diag(trip_cov))
    var_sum = sum(np.diag(trip_cov))
    #print(var_sum)
    covar_sum = sum(sum(trip_cov.to_numpy()))-var_sum  #<- to .to_numpy() metatrepei to dataframe se array
    #print(covar_sum)
    triplet_array.append({"triplet": trip, "var": var_sum, "covar": covar_sum})

print(triplet_array[2])
exit()
mean1 = ty.mean('FCX.Close_log')
k_1 =ty['FCX.Close_log']-mean1

mean2 = ty['EBAY.Close_log'].mean()
k_2 =ty['EBAY.Close_log']-mean2

mean3 = ty['LEN.Close_log'].mean()
k_3 =ty['LEN.Close_log']-mean3

mean4 = ty['TSN.Close_log'].mean()
k_4 =ty['TSN.Close_log']-mean4

mean5 = ty['KR.Close_log'].mean()
k_5 =ty['KR.Close_log']-mean5

mean6 = ty['IP.Close_log'].mean()
k_6 =ty['IP.Close_log']-mean6

mean7 = ty['AN.Close_log'].mean()
k_7 =ty['AN.Close_log']-mean7

mean8 = ty['LPX.Close_log'].mean()
k_8 =ty['LPX.Close_log']-mean8

mean9 = ty['CROX.Close_log'].mean()
k_9 =ty['CROX.Close_log']-mean9

mean10 = ty['MTH.Close_log'].mean()
k_10 =ty['MTH.Close_log']-mean10

mean11 = ty['ATKR.Close_log'].mean()
k_11 =ty['ATKR.Close_log']-mean11
#Total Sum of Squares
TSS_1 = k_1.dot(k_1)
TSS_2 = k_2.dot(k_2)
TSS_3 = k_3.dot(k_3)
TSS_4 = k_4.dot(k_4)
TSS_5 = k_5.dot(k_5)
TSS_6 = k_6.dot(k_6)
TSS_7 = k_7.dot(k_7)
TSS_8 = k_8.dot(k_8)

print(ty)




