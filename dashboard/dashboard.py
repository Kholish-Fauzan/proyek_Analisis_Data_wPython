import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px  # Menggunakan Plotly untuk grafik interaktif

# ------------------------- TAMPILAN UTAMA -------------------------
st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")  # Mengatur lebar dashboard

# **Judul Halaman Utama**
st.title("📊 E-Commerce Dashboard")
st.markdown("""
Selamat datang di **E-Commerce Dashboard**!  
Dashboard ini bertujuan untuk menganalisis berbagai aspek e-commerce, seperti:
- **Top 10 Kota dengan Pelanggan Terbanyak**
- **Top 10 Produk dengan Rating Tertinggi**
- **Distribusi Metode Pembayaran**
""")
st.markdown("""Dashboard ini bertujuan untuk menunjukkan hasil Analisis Data pada E-Commerce dari Olist, sebuah marketplace di Brasil yang menghubungkan penjual kecil dengan berbagai platform penjualan.
            Data ini mencakup informasi pelanggan, pesanan, pembayaran, dan ulasan.

**Pendefinisian Tujuan Analisis Data**
            
Berikut merupakan daftar pertanyaan akan tujuan Analisis Data yang dilakukan, antara lain:

1. Sebutkan 10 jumlah pelanggan E-Commerce terbanyak berdasarkan daerah asalnya?
2. Bagaimana tingkat kepuasan pelanggan E-Commerce berdasarkan 10 nilai rating tertinggi pada pembelian tiap jenis barang yang dilakukan?
3. Metode Pembayaran apa yang lebih banyak digunakan oleh para pelanggan E-Commerce pada saat memesan barang?


Pertanyaan-pertanyaan sederhana di atas tentu sangat berkaitan dengan proses maintenance kualitas layanan E-Commerce, antara lain: 
1. Mengetahui segi kepuasan pengalaman pengguna
2. Mendapatkan insight terkait persebaran pelanggan E-Commerce guna optimasi logistik dan strategi pemasaran
3. Mengetahui preferensi pembayaran pengguna yang berkaitan dengan konversi penjualan dalam aplikasi E-Commerce terkait.

Data diolah oleh: Ahmad Kholish Fauzan Shobiry """)

st.sidebar.title("📌 Navigasi Dashboard")
page = st.sidebar.radio("Pilih Analisis", ["🏠 Halaman Utama", "🏙️ Top 10 Kota", "🛒 Top 10 Produk Terbaik", "💳 Metode Pembayaran"])

# ---------------------- ANALISIS TOP 10 KOTA ----------------------
if page == "🏙️ Top 10 Kota":
    st.subheader("🏙️ Perbandingan Jumlah Pelanggan di antara 10 Kota Terpilih dengan Pelanggan Terbanyak")

    city_df = pd.read_csv("data/topTencities.csv")

    # Checkbox untuk memilih semua kota
    all_cities = st.checkbox("Bandingkan Semua Kota", value=False)

    # Multiselect untuk memilih kota tertentu jika "Bandingkan Semua Kota" tidak dicentang
    if not all_cities:
        selected_cities = st.multiselect(
            "Pilih Kota untuk Perbandingan:",
            options=city_df["customer_city"].unique(),
            default=city_df["customer_city"].unique()[:2]  # Default menampilkan 2 kota pertama
        )
    else:
        selected_cities = city_df["customer_city"].unique()  # Pilih semua kota jika checkbox aktif

    # Filter data sesuai pilihan user
    filtered_city_df = city_df[city_df["customer_city"].isin(selected_cities)]

    # Tampilkan Data
    st.dataframe(filtered_city_df)

    # **Visualisasi Perbandingan**
    fig = px.bar(
        filtered_city_df,
        x="customer_city",
        y="customer_count",
        color="customer_state",
        text="customer_count",
        title="Perbandingan Jumlah Pelanggan di antara 10 Kota Terpilih dengan Pelanggan Terbanyak",
        labels={"customer_count": "Jumlah Pelanggan", "customer_city": "Kota"},
        color_discrete_sequence=px.colors.sequential.Plasma
    )

    st.plotly_chart(fig, use_container_width=True)


     # **Menampilkan Jawaban Analisis**
    st.markdown(f"""
    **Kesimpulan:**\n
    São Paulo dan Rio de Janeiro memiliki jumlah pelanggan paling banyak dibandingkan kota-kota lain. Kota-kota besar lainnya seperti Belo Horizonte dan Brasília juga memiliki jumlah pelanggan yang cukup signifikan.\n
    **Insights:**\n
    São Paulo sebagai pusat pelanggan terbesar menunjukkan potensi besar untuk ekspansi bisnis dan pemasaran di kota ini. Rio de Janeiro sebagai pasar besar kedua menegaskan bahwa strategi bisnis harus tetap berfokus pada dua kota utama ini. Keberagaman geografis dari daftar ini menunjukkan bahwa bisnis memiliki jangkauan yang luas, mencakup berbagai negara bagian seperti SP, RJ, MG, DF, PR, RS, dan BA.\n
    **Strategi bisnis:**\n
    Perusahaan dapat mempertimbangkan lebih banyak kampanye iklan berbasis lokasi, promosi, dan pengoptimalan layanan pengiriman di kota-kota dengan pelanggan terbanyak         
    """)

# ---------------------- ANALISIS TOP 10 PRODUK ----------------------
elif page == "🛒 Top 10 Produk Terbaik":
    st.subheader("🛒 Top 10 Produk dengan Rating Tertinggi")

    # Load Dataset
    category_df = pd.read_csv("data/productreviewResult.csv")

    # **Menampilkan Pertanyaan Analisis**
    st.markdown("## Pertanyaan Analisis")
    st.write("**Bagaimana tingkat kepuasan pelanggan E-Commerce berdasarkan 10 nilai rating tertinggi pada pembelian tiap jenis barang yang dilakukan?**")
    
    # Ambil 10 kategori dengan rating tertinggi, URUTKAN agar skor tertinggi berada di atas
    top_10_satisfaction = category_df.nlargest(10, 'review_score').sort_values(by="review_score", ascending=False)

    # Tampilkan Data
    st.dataframe(top_10_satisfaction)

    # **Membuat Custom Palette dengan Saturasi Sesuai Review Score**
    custom_palette = list(reversed(sns.color_palette("Greens", len(top_10_satisfaction))))  # Reverse untuk warna gelap di atas

    # Visualisasi dengan Matplotlib & Seaborn
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(data=top_10_satisfaction, 
                x='review_score', 
                y='product_category_name_english', 
                palette=custom_palette, ax=ax)

    ax.set_xlabel("Average Review Score")
    ax.set_ylabel("Product Category (English)")
    ax.set_title("Top 10 Product Categories with Highest Customer Satisfaction")
    ax.set_xlim(0, 5)
    ax.grid(axis='x', linestyle='--', alpha=0.6)

    st.pyplot(fig)


    # **Menampilkan Jawaban Analisis**
    st.markdown(f"""
    **Kesimpulan:**\n
    Kategori furniture_bedroom, home_comfort_2, dan flowers memiliki rating kepuasan pelanggan tertinggi, dengan rata-rata mendekati 5. Produk dari kategori ini sangat memenuhi harapan pelanggan.\n
    **Insights:**\n
    Kategori dengan skor tinggi (furniture, home comfort, flowers) menunjukkan bahwa pelanggan puas dengan kualitas dan layanan produk-produk ini. Ini bisa disebabkan oleh kualitas produk yang baik, deskripsi produk yang akurat, atau layanan pengiriman yang andal. Buku dan media (books_general_interest, cds_dvds_musicals) juga mendapat rating tinggi, mungkin karena kualitas isi produk dan keakuratan informasi di toko online.\n
    **Strategi bisnis:**\n
    Perusahaan dapat mempertahankan standar tinggi dalam kategori produk dengan rating terbaik dan meningkatkan layanan pada kategori lain agar mendapat tingkat kepuasan yang sama.        
    """)


# ---------------------- ANALISIS METODE PEMBAYARAN ----------------------
elif page == "💳 Metode Pembayaran":
    st.subheader("💳 Analisis Metode Pembayaran")

    # Load Dataset
    payment_df = pd.read_csv("data/paymentCounts.csv")

    # Pilihan Visualisasi (Bar Chart atau Pie Chart)
    viz_option = st.radio("Pilih Tipe Visualisasi:", ["Bar Chart", "Pie Chart"], horizontal=True)

    # Visualisasi dengan Bar Chart atau Pie Chart
    if viz_option == "Bar Chart":
        fig = px.bar(
            payment_df,
            x="count",
            y="payment_type",
            text="count",
            title="Distribusi Metode Pembayaran",
            labels={"count": "Jumlah Transaksi", "payment_type": "Metode Pembayaran"},
            color="payment_type",
            color_discrete_sequence=px.colors.qualitative.Set2
        )
    else:
        fig = px.pie(
            payment_df,
            names="payment_type",
            values="count",
            title="Distribusi Metode Pembayaran",
            labels={"count": "Jumlah Transaksi", "payment_type": "Metode Pembayaran"},
            color="payment_type",
            color_discrete_sequence=px.colors.qualitative.Set2
        )

    # Tampilkan Grafik
    st.plotly_chart(fig, use_container_width=True)

    # Tampilkan Data
    st.dataframe(payment_df)

    # **Menampilkan Jawaban Analisis**
    st.markdown(f"""
    **Kesimpulan:**\n
    Mayoritas pelanggan menggunakan kartu kredit sebagai metode pembayaran utama, dengan jumlah yang jauh lebih tinggi dibandingkan metode lain seperti boleto, voucher, dan kartu debit. Sementara itu, kategori not_defined memiliki jumlah transaksi yang sangat sedikit.\n
    **Insights:**\n
    Kartu kredit adalah metode pembayaran paling populer, kemungkinan karena kenyamanan dan fitur cicilan yang disediakan. Boleto sebagai metode pembayaran kedua mungkin lebih sering digunakan oleh pelanggan yang tidak memiliki kartu kredit. Voucher dan kartu debit kurang populer, menunjukkan bahwa banyak pelanggan lebih memilih kredit dibanding debit untuk berbelanja online.\n
    **Strategi bisnis:**\n
    Merchant dapat mempertimbangkan untuk menawarkan lebih banyak promo atau cashback bagi pengguna metode pembayaran yang kurang populer guna meningkatkan diversifikasi transaksi.         
    """)
