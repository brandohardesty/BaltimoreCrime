import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mpc



def main():

    data = pd.read_csv('BPD_Part_1_Victim_Based_Crime_Data.csv')
    latitude = data["Latitude"].to_numpy()
    longitude = data["Longitude"].to_numpy()
    
    justShooting = data[((data.Description == "SHOOTING") | (data.Description == 'HOMICIDE'))]
    type = data["Description"]
    oneType = data["Description"][1:2]
    latitudeShooting = justShooting["Latitude"].to_numpy()
    longitudeShooting = justShooting["Longitude"].to_numpy()
    typeMap = {"ROBBERY - RESIDENCE":.1, "AUTO THEFT":.2,"SHOOTING":.3, "AGG. ASSAULT":.4, 'COMMON ASSAULT':.5, 'BURGLARY':.6, 'HOMICIDE':.7, 'ROBBERY - STREET':.8,
 'ROBBERY - COMMERCIAL':.9, 'LARCENY':.18, 'LARCENY FROM AUTO':.25, 'ARSON':.36,
 'ROBBERY - CARJACKING':.65, 'ASSAULT BY THREAT':.75, 'RAPE':1}
    
    colorMap = mpc.ListedColormap(["yellow","blue","orange","wheat","darkblue","tomato","darkred","olive","greenyellow","green","darkgreen","red","peru","slateblue","salmon"])
    plt.register_cmap('myMap', colorMap)

    figure, axis = plt.subplots()
    scatter = axis.scatter(longitude, latitude,c=type.map(typeMap), s=4, cmap=colorMap,marker='o')
    mat = np.random.random((0,1))

    print("Type")
    print(type[0:10])
    print("Type Mapped")
    print(type.map(typeMap)[0:10])
    print("Color Mapped")
    print(colorMap(type.map(typeMap))[0:10])
    plt.colorbar(scatter)
    plt.show()







main()