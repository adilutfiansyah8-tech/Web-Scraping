import requests
from bs4 import BeautifulSoup
import pandas as pd

#Target website khusus latihan web scraping
URL = "http://quotes.toscrape.com"

print("=== Web Scraping Quotes ===\n")

# proses scrap (start)
#untuk kirim requests ke website
response = requests.get(URL)

#cek apakah berhasil (200=ok)
print(f"Status code: {response.status_code}")

#Parse html
soup = BeautifulSoup(response.text, "html.parser")
# print(response.text[:2000])  # Print 2000 karakter pertama HTML nya

#ambil semua quotes
# quotes = soup.find_all("div", class_="quotes") #ini baris lama
quotes = soup.select("div.quote")

#hitung jumlah quotes 
print(f"Jumlah Quotes ditemukan: {len(quotes)}\n")

#loop tiap quotes
for quote in quotes:
    teks = quote.find("span", class_="text").text
    penulis = quote.find("small", class_="author").text
    print(f"Quote : {teks}")
    print(f"Penulis : {penulis}")
    print("-" * 60)
#proses scrap (end)



#     Yang perlu lo pahami:
# requests.get(URL) — Python "membuka" website tersebut, sama seperti browser tapi tanpa tampilan visual. Hasilnya adalah raw HTML.
# response.status_code — kode respon dari server. 200 artinya berhasil, 404 artinya tidak ditemukan, 403 artinya diblokir.
# BeautifulSoup(response.text, "html.parser") — mengubah raw HTML string menjadi objek yang bisa dicari dan difilter dengan mudah.
# soup.find_all("div", class_="quote") — cari semua elemen <div> yang punya class quote di dalam HTML. Ini seperti CSS selector.

#Tampung data semua ke list
data_quotes = []

# proses scrap (start)
for quote in quotes:
    teks = quote.find("span", class_="text").text
    penulis = quote.find("small", class_="author").text
    data_quotes.append({
        "Quotes": teks,
        "Penulis": penulis
    })
# proses scrap (end)


# #simpan data ke excel
df = pd.DataFrame(data_quotes)
df.to_excel("hasil_scraping.xlsx", index=False, engine="openpyxl")

print(f"\n✓ {len(data_quotes)} quotes berhasil di simpan ke hasil_scraping.xlsx")

# Yang perlu lo pahami:
# data_quotes = [] — list kosong sebagai wadah tampung data sebelum dijadiin DataFrame
# data_quotes.append({...}) — tiap quote ditambahkan sebagai dictionary ke dalam list. Strukturnya:
# python[
#   {"quote": "...", "penulis": "Albert Einstein"},
#   {"quote": "...", "penulis": "J.K. Rowling"},
#   ...
# ]
# pd.DataFrame(data_quotes) — pandas otomatis konversi list of dictionary jadi tabel, key dictionary jadi nama kolom

semua_data = []
halaman = 1

# while halaman <= 10:
for halaman in range(1,11):
    url = f"http://quotes.toscrape.com/page/{halaman}/"
    # ... scrape halaman ini (start)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.select("div.quote")

    for quote in quotes:
        teks = quote.find("span", class_="text").text
        penulis = quote.find("small", class_="author").text
        semua_data.append({"quote": teks, "penulis": penulis})
    # ... scrape halaman ini (end)
    

    # ... tambahkan ke semua_data
df = pd.DataFrame(semua_data)
df.to_excel("hasil_scraping.xlsx", index=False, engine="openpyxl")

print(f"\n✓ {len(semua_data)} quotes berhasil di simpan ke hasil_scraping.xlsx")

