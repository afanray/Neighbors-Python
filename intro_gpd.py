import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



cities = gpd.read_file('C:/Users/Bang Ray/Documents/neighbors/newfile.shp')

# add new column
#cities["IPD"] = 0 

cities["NEIGHBORS"] = None  
cities["M"]= 0
cities["sWij"] = 0

cities["sWijPopj"] = 0
cities["Popi_sWijPopj"] = 0
cities["Pop_Adj2"] = 0

#cities["sumIpdNb"] = 0
#cities["ipdSumipdNb"] = 0
#cities["sTiIpd"] = 0

#ipd =[12,13,14,15,16,17,12,14]
#cities.IPD = ipd
    
for index, row in cities.iterrows():   
    # get 'not disjoint' countries
    neighbors = cities[~cities.geometry.disjoint(row.geometry)].DESA.tolist()
    # remove own name from the list
    neighbors = [DESA for DESA in neighbors if row.DESA != DESA]
    
    #POP
    pop_sum = cities[~cities.geometry.disjoint(row.geometry)].POP.tolist()
    pop_sum = [POP for POP in pop_sum if row.POP != POP]
    
    #IPD
#    ipd_sum = cities[~cities.geometry.disjoint(row.geometry)].IPD.tolist()
#    ipd_sum = [IPD for IPD in ipd_sum if row.IPD != IPD]
     
    # add names of neighbors as NEIGHBORS value
    cities.at[index, "NEIGHBORS"] = ", ".join(neighbors)
    cities.at[index, "M"]=len(neighbors)
    
    #Add value
    cities.at[index, "sWijPopj"]=sum(pop_sum)
#    cities.at[index, "sumIpdNb"]=sum(ipd_sum)
    
    #Add Values Sigma WIJ    
    swij =1/cities.M
    cities.sWij = swij
    
    #Add Values of POP
    sumxpop = cities.sWijPopj*cities.POP
    cities.Popi_sWijPopj = sumxpop
    cities.Pop_Adj2 = np.sqrt(sumxpop*swij)
    
    #Add Values of iPD
#    sumxipd = cities.sumIpdNb*cities.IPD
#    cities.ipdSumipdNb = sumxipd
#    cities.sTiIpd = np.sqrt(sumxipd*swij)
    
#    cities.Pop_Adj2.plot(figsize=(10,10))
#    cities.plot(cmap='rainbow', column='DESA', figsize=(10,10))
    
       
    #create new file
#    cities.to_file("C:/Users/Bang Ray/Documents/neighbors/newfile3.shp")
    
    #Prosess
#    print("Processing: %s" % cities.DESA)
    print ('Processing complete.')
    



