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
    st.subheader("🏙️ Top 10 Kota dengan Pelanggan Terbanyak")

    # Load Dataset
    city_df = pd.read_csv("data/topTencities.csv")

    # **Menampilkan Pertanyaan Analisis**
    st.markdown("## Pertanyaan Analisis")
    st.write("**Sebutkan 10 jumlah pelanggan E-Commerce terbanyak berdasarkan daerah asalnya?**")

    # Urutkan dari jumlah pelanggan terbanyak
    city_df = city_df.sort_values(by="customer_count", ascending=False)

    # Tampilkan Data
    st.dataframe(city_df)

    # Visualisasi dengan Plotly
    fig = px.bar(
        city_df, 
        x="customer_count", 
        y="customer_city", 
        color="customer_state", 
        text="customer_count", 
        orientation="h",
        title="Top 10 Kota dengan Pelanggan Terbanyak",
        labels={"customer_count": "Jumlah Pelanggan", "customer_city": "Kota"},
        color_continuous_scale="Blues"
    )

    # Menyesuaikan tampilan agar lebih bersih dan mudah dibaca
    fig.update_traces(texttemplate='%{text:,}', textposition='inside')
    fig.update_layout(
        xaxis_title="Jumlah Pelanggan",
        yaxis_title="Kota",
        yaxis={'categoryorder':'total ascending'},
        template="plotly_white"
)

    st.plotly_chart(fig, use_container_width=True)

     # **Menampilkan Jawaban Analisis**
    st.markdown(f"""
    **Insights**
    - São Paulo memiliki jumlah pelanggan tertinggi, maka kota ini bisa menjadi target utama kampanye pemasaran atau pengoptimalan logistik.
    - Dapat dilihat bahwa kota selain Sao Paulo memliki persebaran jumlah pelanggan yang sangat jauh, maka, daerah dengan pelanggan yang jauh lebih sedikit ini dapat menjadi potensi untuk kampanye pemasaran digital atau diskon khusus untuk menarik lebih banyak pelanggan di kota tersebut.         
    """)

# ---------------------- ANALISIS TOP 10 PRODUK ----------------------
elif page == "🛒 Top 10 Produk Terbaik":
    st.subheader("🛒 Top 10 Produk dengan Rating Tertinggi")

    # Load Dataset
    category_df = pd.read_csv("data/productreviewResult.csv")

    # **Menampilkan Pertanyaan Analisis**
    st.markdown("## Pertanyaan Analisis")
    st.write("**Bagaimana tingkat kepuasan pelanggan E-Commerce berdasarkan 10 nilai rating tertinggi pada pembelian tiap jenis barang yang dilakukan?**")
    
    # Ambil 10 kategori dengan rating tertinggi
    top_10_satisfaction = category_df.nlargest(10, 'review_score')

    # Tampilkan Data
    st.dataframe(top_10_satisfaction)

    # Visualisasi dengan Matplotlib & Seaborn
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(data=top_10_satisfaction, 
                x='review_score', 
                y='product_category_name_english', 
                palette='viridis', ax=ax)

    ax.set_xlabel("Average Review Score")
    ax.set_ylabel("Product Category (English)")
    ax.set_title("Top 10 Product Categories with Highest Customer Satisfaction")
    ax.set_xlim(0, 5)
    ax.grid(axis='x', linestyle='--', alpha=0.6)

    st.pyplot(fig)

    # **Menampilkan Jawaban Analisis**
    st.markdown(f"""
    **Insights**
    1.  Kategori "Furniture Bedroom" Mendapatkan Rating Tertinggi (4.94)
    2. Produk Home & Living Mendominasi "Home Comfort 2" (4.63) dan "Home Appliances 2" (4.33) juga masuk dalam daftar tertinggi.
    3. Buku dan Hiburan Juga Banyak Disukai Kategori "Books General Interest" (4.42) dan "Books Technical" (4.35) menunjukkan bahwa buku memiliki ulasan yang baik.
    4. "CDs, DVDs, Musicals" (4.42) juga memiliki rating tinggi, menunjukkan bahwa produk hiburan piringan fisik masih memiliki pasar.
    5. Kategori Alat & Aksesori Juga Populer "Construction Tools" (4.39) dan "Luggage Accessories" (4.36) mendapatkan skor tinggi.
    6. Produk Makanan & Minuman Masuk 10 Besar (4.31)

    **Kesimpulan & Rekomendasi**
    - Fokus pada produk Home & Living karena kategori ini mendominasi rating tinggi.
    - Eksplorasi peluang di kategori buku dan hiburan, karena pelanggan memberikan rating baik.
    - Pastikan kualitas produk tetap terjaga, terutama di kategori dengan rating tinggi, untuk mempertahankan kepuasan pelanggan.
    - Tingkatkan strategi pemasaran pada kategori dengan skor tinggi untuk meningkatkan penjualan.         
    """)


# ---------------------- ANALISIS METODE PEMBAYARAN ----------------------
elif page == "💳 Metode Pembayaran":
    st.subheader("💳 Distribusi Metode Pembayaran")

    # Load Dataset
    payment_df = pd.read_csv("data/paymentCounts.csv")

    st.markdown("## Pertanyaan Analisis")
    st.write("**Metode Pembayaran apa yang lebih banyak digunakan oleh para pelanggan E-Commerce pada saat memesan barang?**")

    # Tampilkan Data
    st.dataframe(payment_df)

    # Visualisasi dengan Plotly
    fig = px.pie(
        payment_df,
        names="payment_type",
        values="count",
        title="Distribusi Penggunaan Metode Pembayaran",
        color_discrete_sequence=px.colors.sequential.Viridis
        )
    
    st.plotly_chart(fig)

    # **Menampilkan Jawaban Analisis**
    st.markdown(f"""
    **Insights**
    1. Kartu Kredit adalah Metode Pembayaran Paling Populer (76.795 transaksi)
    2. Boleto Menjadi Alternatif Populer (19.784 transaksi) Boleto (sistem pembayaran berbasis kode di Brasil) menjadi metode kedua yang paling banyak digunakan. Ini menunjukkan bahwa beberapa pelanggan masih memilih pembayaran tunai atau transfer bank.
    3. Debit Card Kurang Diminati (1.529 transaksi)
    4. Voucher Digunakan dalam 5.775 Transaksi Cukup banyak pelanggan yang menggunakan voucher, menunjukkan bahwa program diskon atau promo cukup diminati.
    5. Kategori "Not Defined" (3 transaksi) Perlu Diperiksa. Bisa jadi ada data yang salah input atau transaksi yang tidak valid.

    **Kesimpulan & Rekomendasi**
    1. Fokus pada kartu kredit dan boleto sebagai metode utama pembayaran dengan meningkatkan keamanan dan kemudahan transaksi.
    2. Tingkatkan promosi dan program diskon berbasis voucher, karena sudah cukup banyak pelanggan yang menggunakannya.
    3. Lakukan analisis lebih lanjut terhadap transaksi debit card untuk memahami mengapa penggunaannya rendah.            
    """)
