# 📊 E-Commerce Dashboard Streamlit

## 📌 Deskripsi Proyek
Dashboard ini dibuat untuk **menganalisis data e-commerce**, termasuk:
- **🏙️ Top 10 Kota dengan Pelanggan Terbanyak**
- **🛒 Top 10 Produk dengan Rating Tertinggi**
- **💳 Distribusi Metode Pembayaran**

Dashboard dikembangkan menggunakan **Streamlit**, dengan data hasil analisis dari Python.

---

## **🚀 Panduan Menjalankan Dashboard di VS Code**

### **1️⃣ Instalasi Awal**
Sebelum menjalankan dashboard, pastikan:
- **Python** sudah terinstal (**Cek dengan:** `python --version`)
- **VS Code** sudah terinstal di komputer
- **Git** sudah terinstal (**Cek dengan:** `git --version`)

---

### **2️⃣ Clone atau Download Repository**
#### **🔹 a) Clone dari GitHub (Jika ada Repository)**
Jika proyek sudah ada di **GitHub**, jalankan perintah ini di terminal VS Code:
```bash
  git clone https://github.com/Kholish-Fauzan/analysis_data_with_Python.git
  cd analysis_data_with_Python
```
#### **🔹 b) Jika Menggunakan File ZIP**
1. **Download ZIP** proyek.
2. **Ekstrak ZIP** di komputer.
3. **Buka folder proyek di VS Code**.

---

### **3️⃣ Buat & Aktifkan Virtual Environment**
**Virtual Environment** digunakan agar dependensi proyek tidak mengganggu sistem utama.

#### **🔹 Windows**
```bash
  python -m venv env
  env\Scripts\activate

```
📌 Jika berhasil, kamu akan melihat **`(env)`** di terminal.

---

### **4️⃣ Instal Semua Dependencies**
Setelah virtual environment aktif, instal semua **library** yang diperlukan:
```bash
  pip install -r requirements.txt
```
📌 Ini akan menginstal **Streamlit, Pandas, Matplotlib, Seaborn, Plotly**, dan library lainnya.

---

### **5️⃣ Jalankan Dashboard di VS Code**
Pastikan kamu berada di folder proyek, lalu jalankan perintah ini:
```bash
  streamlit run dashboard/dashboard.py
```
📌 Setelah itu, **buka browser** dan akses:
```
  http://localhost:8501
```

---

## **📊 Dataset yang Digunakan**
Data yang digunakan dalam proyek ini:
- 📂 **`categorysatisfaction.csv`** → Berisi rating produk e-commerce.
- 📂 **`payment_type_counts.csv`** → Berisi distribusi metode pembayaran.
- 📂 **`top10cities.csv`** → Berisi data pelanggan berdasarkan kota.

Semua dataset sudah **dibersihkan dan dianalisis** di **Google Colab (`.ipynb`)** sebelum digunakan di dashboard.

---

## **🌎 Streamlit Dashboard **
Dashboard sudah deploy ke **Streamlit Cloud**, akses dashboard melalui URL berikut:
```
  https://kholish-fauzan-analysis-da-dashboardsubmission-dashboard-iivgyr.streamlit.app/
```
---

## **📝 Author**
- **Nama:** Ahmad Kholish Fauzan Shobiry 
- **Email:** fauzanshobi@gmail.com  
- **GitHub:** [https://github.com/Kholish-Fauzan](https://github.com/Kholish-Fauzan)  

---

### **🔥 Sekarang, Kamu Bisa Menjalankan Dashboard dengan Mudah di VS Code!** 🚀  
Jika ada pertanyaan atau kendala, **silakan hubungi saya!** 😊

