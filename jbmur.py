import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

jbmur = gpd.read_file('C:/Users/Bang Ray/Documents/neighbors/JBMUR/editjbmur.shp')

# add new column
jbmur["NEIGHBORS"] = None  
jbmur["M"]= 0
jbmur["sWij"] = 0.00

jbmur["sWijV63j"] = 0.00
jbmur["sWijV9_1j"] = 0.00
jbmur["sWijV21_1j"] = 0.00
jbmur["sWijV22_1j"] = 0.00
jbmur["sWijV23_1j"] = 0.00
jbmur["sWijV24_1j"] = 0.00
jbmur["sWijV25_1j"] = 0.00
jbmur["sWijX20j"] = 0.00
jbmur["sWijX21j"] = 0.00

jbmur["V63i_sWijV63j"] = 0.00
jbmur["V9_1i_sWijV9_1j"] = 0.00
jbmur["V21_1i_sWijV21_1j"] = 0.00
jbmur["V22_1i_sWijV22_1j"] = 0.00
jbmur["V23_1i_sWijV23_1j"] = 0.00
jbmur["V24_1i_sWijV24_1j"] = 0.00
jbmur["V25_1i_sWijV25_1j"] = 0.00
jbmur["X20i_sWijX20j"] = 0.00
jbmur["X21i_sWijX21j"] = 0.00

jbmur["V63_Adj2"] = 0
jbmur["V9_1_Adj2"] = 0
jbmur["V21_1_Adj2"] = 0
jbmur["V22_1_Adj2"] = 0
jbmur["V23_1_Adj2"] = 0
jbmur["V24_1_Adj2"] = 0
jbmur["V25_1_Adj2"] = 0
jbmur["X20_Adj2"] = 0
jbmur["X21_Adj2"] = 0
    
for index, row in jbmur.iterrows():   
    # neighbors
    neighbors = jbmur[~jbmur.geometry.disjoint(row.geometry)].KECAMATAN.tolist()
    neighbors = [KECAMATAN for KECAMATAN in neighbors if row.KECAMATAN != KECAMATAN]
    
    #V63
    V63_sum = jbmur[~jbmur.geometry.disjoint(row.geometry)].V63.tolist()
    V63_sum = [V63 for V63 in V63_sum if row.V63 != V63]
    
    #V9_1
    V9_1_sum = jbmur[~jbmur.geometry.disjoint(row.geometry)].V9_1.tolist()
    V9_1_sum = [V9_1 for V9_1 in V9_1_sum if row.V9_1 != V9_1]
    
    #V21_1
    V21_1_sum = jbmur[~jbmur.geometry.disjoint(row.geometry)].V21_1.tolist()
    V21_1_sum = [V21_1 for V21_1 in V21_1_sum if row.V21_1 != V21_1]
    
    #V22_1
    V22_1_sum = jbmur[~jbmur.geometry.disjoint(row.geometry)].V22_1.tolist()
    V22_1_sum = [V22_1 for V22_1 in V22_1_sum if row.V22_1 != V22_1]
    
    #V23_1
    V23_1_sum = jbmur[~jbmur.geometry.disjoint(row.geometry)].V23_1.tolist()
    V23_1_sum = [V23_1 for V23_1 in V23_1_sum if row.V23_1 != V23_1]
    
    #V24_1
    V24_1_sum = jbmur[~jbmur.geometry.disjoint(row.geometry)].V24_1.tolist()
    V24_1_sum = [V24_1 for V24_1 in V24_1_sum if row.V24_1 != V24_1]
    
    #V25_1
    V25_1_sum = jbmur[~jbmur.geometry.disjoint(row.geometry)].V25_1.tolist()
    V25_1_sum = [V25_1 for V25_1 in V25_1_sum if row.V25_1 != V25_1]
    
    #X20
    X20_JRK_JK_sum = jbmur[~jbmur.geometry.disjoint(row.geometry)].X20_JRK_JK.tolist()
    X20_JRK_JK_sum = [X20_JRK_JK for X20_JRK_JK in X20_JRK_JK_sum if row.X20_JRK_JK != X20_JRK_JK]
    
    #X21
    X21_JRK_JA_sum = jbmur[~jbmur.geometry.disjoint(row.geometry)].X21_JRK_JA.tolist()
    X21_JRK_JA_sum = [X21_JRK_JA for X21_JRK_JA in X21_JRK_JA_sum if row.X21_JRK_JA != X21_JRK_JA]  
    
    # add names of neighbors as NEIGHBORS value
    jbmur.at[index, "NEIGHBORS"] = ", ".join(neighbors)
    jbmur.at[index, "M"]=len(neighbors)
    
     #Add Values Sigma WIJ    
    swij =1/jbmur.M
    jbmur.sWij = swij
    
    #Add value
    jbmur.at[index, "sWijV63j"]=float(sum(V63_sum))
    jbmur.at[index, "sWijV9_1j"]=float(sum(V9_1_sum))
    jbmur.at[index, "sWijV21_1j"]=float(sum(V21_1_sum))
    jbmur.at[index, "sWijV22_1j"]=float(sum(V22_1_sum))
    jbmur.at[index, "sWijV23_1j"]=float(sum(V23_1_sum))
    jbmur.at[index, "sWijV24_1j"]=float(sum(V24_1_sum))
    jbmur.at[index, "sWijV25_1j"]=float(sum(V25_1_sum))
    jbmur.at[index, "sWijX20j"]=float(sum(X20_JRK_JK_sum))
    jbmur.at[index, "sWijX21j"]=float(sum(X21_JRK_JA_sum))
    
    #Add Values of COLUMN
    sumxV63 = jbmur.sWijV63j*jbmur.V63
    sumxV9_1 = jbmur.sWijV9_1j*jbmur.V63
    sumxV21_1 = jbmur.sWijV21_1j*jbmur.V21_1
    sumxV22_1 = jbmur.sWijV22_1j*jbmur.V22_1
    sumxV23_1 = jbmur.sWijV23_1j*jbmur.V23_1
    sumxV24_1 = jbmur.sWijV24_1j*jbmur.V24_1
    sumxV25_1 = jbmur.sWijV25_1j*jbmur.V25_1
    sumxX20 = jbmur.sWijX20j*jbmur.X20_JRK_JK
    sumxX21 = jbmur.sWijX21j*jbmur.X21_JRK_JA
    
    jbmur.V63i_sWijV63j = sumxV63
    jbmur.V9_1i_sWijV9_1j = sumxV9_1
    jbmur.V21_1i_sWijV21_1j = sumxV21_1
    jbmur.V22_1i_sWijV22_1j = sumxV22_1
    jbmur.V23_1i_sWijV23_1j = sumxV23_1
    jbmur.V24_1i_sWijV24_1j = sumxV24_1
    jbmur.V25_1i_sWijV25_1j = sumxV25_1
    jbmur.X20i_sWijX20j = sumxX20
    jbmur.X21i_sWijX21j = sumxX21
    
    jbmur.V63_Adj2 = np.sqrt(sumxV63*swij)
    jbmur.V9_1_Adj2 = np.sqrt(sumxV9_1*swij)
    jbmur.V21_1_Adj2 = np.sqrt(sumxV21_1*swij)
    jbmur.V22_1_Adj2 = np.sqrt(sumxV22_1*swij)
    jbmur.V23_1_Adj2 = np.sqrt(sumxV23_1*swij)
    jbmur.V24_1_Adj2 = np.sqrt(sumxV24_1*swij)
    jbmur.V25_1_Adj2 = np.sqrt(sumxV25_1*swij)
    jbmur.X20_Adj2 = np.sqrt(sumxX20*swij)
    jbmur.X21_Adj2 = np.sqrt(sumxX21*swij)
    
    #Prosess
#    print("Processing: %s" % jbmur.KECAMATAN)
    print ('Processing complete.')
    
#    jbmur.to_file("C:/Users/Bang Ray/Documents/neighbors/JBMUR/editjbmur2.shp")
    



