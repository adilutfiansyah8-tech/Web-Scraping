# 🕷️ Web Scraping Quotes

Script Python untuk mengambil data quotes dari website secara otomatis menggunakan `requests` dan `BeautifulSoup`, lalu menyimpan hasilnya ke file Excel.

---

## 📋 Deskripsi Project

Web Scraping adalah teknik mengambil data dari website secara otomatis tanpa perlu copy-paste manual. Project ini mensimulasikan pekerjaan freelance nyata — klien minta data dari website tertentu, lo ambil otomatis pakai Python.

```
Website (HTML)  →  requests ambil  →  BeautifulSoup parsing  →  Excel
```

**Target:** [quotes.toscrape.com](http://quotes.toscrape.com) — website khusus latihan scraping

---

## ✨ Fitur

- ✅ Scrape **100 quotes** dari 10 halaman sekaligus
- ✅ Ambil teks quote dan nama penulis
- ✅ Progress per halaman ditampilkan di terminal
- ✅ Simpan semua hasil ke file Excel (`.xlsx`)

---

## 🗂️ Struktur File

```
Web Scraping Project/
│
├── main.py                 → Script utama (jalankan ini)
├── hasil_scraping.xlsx     → Output hasil scraping (auto-generated)
└── README.md
```

---

## 🧠 Konsep yang Digunakan

### HTTP Request dengan `requests`
```python
response = requests.get(url)
# response.status_code → 200 = OK, 404 = Not Found, 403 = Blocked
```
Python "membuka" website seperti browser, tapi hasilnya raw HTML tanpa tampilan visual.

### Parsing HTML dengan `BeautifulSoup`
```python
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.select("div.quote")  # CSS selector
```
Mengubah raw HTML string menjadi objek yang bisa dicari dan difilter — seperti inspeksi elemen di browser.

### Pagination (Multi-halaman)
```python
for halaman in range(1, 11):
    url = f"http://quotes.toscrape.com/page/{halaman}/"
    # scrape tiap halaman
```
Loop otomatis berpindah halaman — tanpa ini, hanya halaman pertama yang ter-scrape.

### List of Dictionary → DataFrame
```python
semua_data.append({"quote": teks, "penulis": penulis})
df = pd.DataFrame(semua_data)
```
Data ditampung sebagai list of dictionary, lalu dikonversi ke DataFrame pandas untuk di-export ke Excel.

---

## 🔍 Penjelasan Fungsi

### `scrape_quotes()`
Fungsi utama yang menjalankan seluruh proses scraping:

1. Loop dari halaman 1 sampai 10
2. Kirim HTTP request ke tiap halaman
3. Parse HTML dengan BeautifulSoup
4. Ambil teks quote dan nama penulis dari tiap elemen
5. Tampilkan progress di terminal
6. Simpan semua data ke Excel

---

## 🚀 Cara Menjalankan

### Prasyarat
```bash
pip install requests beautifulsoup4 pandas openpyxl
```

### Jalankan
```bash
python main.py
```

### Output
File `hasil_scraping.xlsx` berisi 100 quotes dari 10 halaman.

---

## 💡 Contoh Output Terminal

```
✓ Halaman 1 selesai — 10 quotes diambil
Quote  : "The world as we have created it is a process of our thinking..."
Penulis: Albert Einstein
------------------------------------------------------------
...
✓ Halaman 10 selesai — 10 quotes diambil

✓ 100 quotes berhasil disimpan ke hasil_scraping.xlsx
```

---

## ⚠️ Catatan & Keterbatasan

- **Koneksi internet dibutuhkan** — script tidak bisa jalan offline
- **Website statis only** — `requests` + `BeautifulSoup` hanya bisa scrape website statis. Website yang datanya dimuat JavaScript (dinamis) butuh `selenium`
- **Tidak ada delay antar request** — di project nyata sebaiknya tambahkan `time.sleep()` agar tidak membebani server klien
- **Single data point** — hanya mengambil quote dan penulis, belum mengambil tags

---

## 🔧 Kemungkinan Pengembangan

- [ ] Tambahkan `time.sleep()` antar request untuk menghindari rate limiting
- [ ] Ambil juga data tags tiap quote
- [ ] Tambahkan filter scraping berdasarkan penulis tertentu
- [ ] Simpan ke CSV sebagai alternatif Excel
- [ ] Tambahkan handling error jika koneksi gagal di tengah proses
- [ ] Support scraping website dinamis dengan `selenium`

---

## 🛠️ Library yang Digunakan

| Library | Versi | Fungsi |
|---|---|---|
| `requests` | 2.32.5 | Kirim HTTP request ke website |
| `beautifulsoup4` | latest | Parse dan ekstrak data dari HTML |
| `pandas` | 3.0.0 | Konversi data ke DataFrame |
| `openpyxl` | 3.1.5 | Export ke file Excel (.xlsx) |

---

## 👤 Author

Dibuat sebagai project portfolio Python — implementasi Web Scraping dengan `requests` dan `BeautifulSoup`.
