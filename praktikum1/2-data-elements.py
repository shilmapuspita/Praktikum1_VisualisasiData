import streamlit as st
import pandas as pd #mengelola data dlm bentuk tabel (dataframe)
import numpy as np #membuat data numerik acak
import altair as alt #membuat diagram char

st.title("Praktikum 1 - Visualisasi Data")
st.subheader("Bagian 2: Data Elements")
st.markdown("""
1. Shilma Puspita - 0110122038
2. Taufik Hidayat - 0110222093
3. Nurhafidudin - 0110222110
""")

#Data frame : struktur data berbentuk tabel (baris dan kolom) yg disediakan oleh library pandas

st.subheader("DataFrame")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10))
)

#menampilkan dataframe
st.dataframe(df)

#Highlight Nilai minimum
st.subheader("Highlight Minimum Value di DataFrame")

#Highlight nilai terkecil disetiap kolom dataframe
#axis=0 bekerja per kolom
st.dataframe(df.style.highlight_min(axis=0))

#Tabel statis
st.subheader("Tabel Statis")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10))
)

#menampilkan tabel statis
st.table(df)

#metrics: komponen tampilan angka penting
st.subheader("Metrics")

#menampilkan metrik tunggal (nilai utama+perubahan nilai)

#metrics tunggal
st.metric(label="Temperature", value="31 C", delta="1.2 C") #kenaikan 1.2 C

#metrics sesuai delta_color
#normal: naik -> hijau, turun -> merah
#inverse: kebalikannya (naik:merah)
#off: tidak menampilkan warna perubahan

#definisikan variabel metrics
col1, col2, col3 = st.columns(3)

#menampilkan indikator data
col1.metric("Curah Hujan", "100 cm", "10 cm") # naik dan baik
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar", delta_color="inverse") # naik tapi buruk
col3.metric(label="Pelanggan", value=100, delta=10,
delta_color="off") # netral (tidak baik, tidak buruk)

#Menampilkan metrik tambahan dengan nilai kosong atau nol
st.metric(label="Speed", value=None, delta=0) #kosong #naik baik karena di setting default
st.metric("Trees", "91456", "-1132649") #penurunan