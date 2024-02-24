import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
fiyat=[100,200,250,150]
marka=["A","B","C","D"]
liste=list(zip(fiyat,marka))#data frame oluşturmak için değerleri eşleştridik
print(liste)
veri=pd.DataFrame(data=liste,columns=["Fiyat","Marka"])
print(veri)
#fig,ax=plt.subplots(2,2)
#print(ax)
#ax[1,0].plot(marka,fiyat)
#ax[1,1].set_title("örnek başlık",color="red")
renkler={"A":"tab:pink",
         "B":"tab:purple",
         "C":"tab:green",
         "D":"tab:grey"}
#
#sns.barplot(x=marka,y=fiyat,palette=renkler,alpha=0.5).set_facecolor("midnightblue")
#plt.title("örnek başlık",color="darkblue",fontsize=50,fontweight="bold",fontname="Times New Roman",loc="left",pad=20)
#plt.xlabel("Markalar",color="red",fontsize=15)
#plt.ylabel("Fiyatlar",color="red",fontsize=15)
#plt.ylim(0,300)
#nereden başlasın nereye kadar ve kaçar aralıklarla
#sns.barplot(y=marka,x=fiyat,orient="h")#x ve y nin yerini değiştirdik
sns.barplot(x="Fiyat",y="Marka",data=veri,orient="h",order=veri.sort_values("Fiyat",ascending=False).Marka)
plt.show()
