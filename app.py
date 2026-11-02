import streamlit as st
from PIL import Image, ImageDraw

st.title("Aplikasi Edit Meteran Listrik")
st.write("Unggah foto, hapus watermark bagian bawah, dan ubah angka meteran.")

uploaded_file = st.file_uploader("Pilih gambar meteran...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.subheader("Gambar Asli:")
    st.image(image, use_column_width=True)
    
    width, height = image.size
    
    angka_baru = st.text_input("Masukkan Angka Baru:", "88923")
    
    if st.button("Proses Gambar"):
        # Hapus bagian bawah (Crop watermark hitam transparan)
        crop_height = int(height * 0.88) 
        img_processed = image.crop((0, 0, width, crop_height))
        
        # Proses ubah angka (opsional/sesuai kebutuhan koordinat)
        draw = ImageDraw.Draw(img_processed)
        
        st.subheader("Hasil Akhir:")
        st.image(img_processed, use_column_width=True)
        st.success("Gambar berhasil diproses! Anda bisa melakukan screenshot atau menyimpan gambar di atas langsung dari HP.")
