#%%
import streamlit as st
import pandas as pd
import numpy as np
import pickle

file1 = open('laptoppricepredictor4.pkl', 'rb')
pipe2 = pickle.load(file1)
file1.close()

# Apple,Ultrabook,8,Mac,1.37,0,1,226.98300468106115,Intel Core i5,0,128,Intel

df = pd.read_csv("data/for_app.csv")


#%%

# Başlık
st.title("Bilgisayarının Fiyatı ne kadar ?  ")
st.image("images/laptop.png")

#Marka
#marka = st.selectbox('Marka', df['marka'].unique())

# ekran_boyutu
ekran_boyutu = st.number_input('Screen Size')

# işlemciçekirdek sayısı
islemci_cekirdek_sayisi = st.selectbox('İşlemci Çekirdek Sayısı', [2, 4, 6, 8, 10, 12, 14])

# islemci_hizi 
islemci_hizi = st.number_input('İşlemci Hızı GHz')

# disk_tipi
disk_tipi = st.selectbox('Disk Tipi', df['disk_tipi'].unique())

# ram_tipi
ram_tipi = st.selectbox('Ram Tipi', df['ram_tipi'].unique())

# gpu_model
gpu_model = st.selectbox('Gpu Model Tipi', df['gpu_model'].unique())

# parmak_izi_okuyucu
parmak_izi_okuyucu = st.selectbox('parmak_izi_okuyucu', ['Yok', 'Var'])

# isletim_sistemi 
isletim_sistemi = st.selectbox('isletim_sistemi', df['isletim_sistemi'].unique())

# ekran_cozunurluk 
ekran_cozunurluk = st.selectbox('ekran_cozunurluk', df['ekran_cozunurluk'].unique())

# Ram 
ram_miktari = st.selectbox('Ram(in GB)', [32,16,8,64,12,4,40,20,36,24,48,128])

# gpumiktari 
gpu_miktari = st.selectbox('Gpu(in GB)', [6,4,2,8,16,3])

# disk_kapasitesi 
disk_kapasitesi = st.number_input('Disk Kapasitesi GB')

# hdmi
hdmi = st.selectbox('Hdmi', ['Yok', 'Var'])



if st.button('Predict Price'):

     #parmak_izi_okuyucu +
    if parmak_izi_okuyucu == 'Var':
        parmak_izi_okuyucu = 1
    else:
        parmak_izi_okuyucu = 0

    #gpu_model +
    if gpu_model == 'Paylasimli':
        gpu_model = 1
    else:
        gpu_model = 0     
    
    #hdmi +
    if hdmi == 'Var':
        hdmi = 1
    else:
        hdmi = 0 

    #disk_tipi +
    if disk_tipi == 'SSD':
        disk_tipi = 2

    elif disk_tipi == 'HDD-SSD' : 
         disk_tipi = 1
    else:
        disk_tipi = 0 

    #ram_tipi +
    if ram_tipi == 'DDR5':
        ram_tipi = 2
    elif ram_tipi == 'DDR4' : 
         ram_tipi = 1
    else:
        ram_tipi = 0 

    #isletim_sistemi +
    if isletim_sistemi == 'Windows':
        isletim_sistemi = 2
    elif isletim_sistemi == 'Linux' : 
         isletim_sistemi = 1
    else:
        isletim_sistemi = 0     

    #ekran_cozunurluk
    if ekran_cozunurluk == '2560 x 1440':
        ekran_cozunurluk = 3
    elif ekran_cozunurluk == '1920 x 1200' : 
         ekran_cozunurluk = 2
    elif ekran_cozunurluk == '1920 x 1080' : 
         ekran_cozunurluk = 1
    else:
        ekran_cozunurluk = 0 

    

    query = np.array([ekran_boyutu, islemci_cekirdek_sayisi, islemci_hizi, disk_tipi, ram_tipi , 
                     gpu_model, parmak_izi_okuyucu, isletim_sistemi, ekran_cozunurluk, ram_miktari,
                     gpu_miktari,disk_kapasitesi,hdmi])

    query = query.reshape(1, 13)

    prediction = int(np.exp(pipe2.predict(query)[0]))

    st.title("Tahmin edilen fiyat aralığı : " +
             str(prediction-1000)+" TL" + " - " + str(prediction+1000)+" TL")
    
    st.image("images/amantanrımALLAHIM.png")



