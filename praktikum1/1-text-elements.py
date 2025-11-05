#import library yang dibutuhkan
import streamlit as st

#Bagian 1 : Text element
# st.header("Ini header") #header - untuk buat tulisan header
# st.subheader("Ini sub header") #untuk membuat sub judul
# st.text("Ini teks biasa tanpa format") #untuk buat teks polos
# st.markdown("**ini teks bold** dan *ini teks italic*") #untuk membuat teks tebal/miring
# st.caption("caption") #untuk buat teks kecil dibawah elemen
# st.title("ini judul")
# st.markdown("""
# - baris 1
# 1. baris 2 
# * baris 3 
# """)

st.title("Praktikum 1 - Visualisasi Data")
st.subheader("Bagian 1: Text Elements")
st.markdown("""
1. Shilma Puspita - 0110122038
2. Taufik Hidayat - 0110222093
3. Nurhafidudin - 0110222110
""")

#Bagian 2 : Menampilkan Rumus (LaTex)

# st.latex(r''' \cos^2\theta = 1-2\sin^2\theta ''') #rumus trigonometri
# st.latex(r'''' (a+b)^2 = a^2 + b^2 + 2ab ''') #rumus kuadrat biominal

#Bagian 3 : Menampilkan Kode Program
st.header("Displaying Code")
st.subheader("Python Code")

#simpan ke variable
code = '''
def hello():
    print("Hello, Streamlit!")
'''

#st.code() untuk menampilkan potongan kode dgn format rapi dan syntax highlighting
st.code(code, language='python')

st.subheader("Java Code")
st.code("""
public class GFG {
    public static void main(String arg[]){
        System.out.printIn("Hello World");
    }
}        
""", language='java')

#fungsi st.code() bisa digunakan untuk bahasa pemrograman lain seperti Jva, JavaScript, C++, HTML, dll

st.subheader("JavaScript Code")
st.code("""
<p id="demo"></p>
<script>
try {
    addalert("Welcome guest!"); // kesalahan ketik (addaleart)
    sengaja dibuat untuk menimbulkan error
}
catch(err){
    document.getElementById("demo").innerHTML = err.massage; // menampilkan pesan error di elemen HTML dgn id 'demo'
}
</script>
""", language='javascript')

#Kode ini menunjukkan contoh bagaimana menangani error (exception) dio javascript
#Hasilnya tidak dijalankan di Streamlit, tapi ditampilkan sebagai contoh kode