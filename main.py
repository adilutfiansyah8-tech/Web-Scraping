import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_quotes():
    semua_data = []

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
            print(f"Quote : {teks}")
            print(f"Penulis : {penulis}")
            print("-" * 60)
        # ... scrape halaman ini (end)
        
        print(f"✓ Halaman {halaman} selesai — {len(quotes)} quotes diambil")


        # ... tambahkan ke semua_data
    df = pd.DataFrame(semua_data)
    df.to_excel("hasil_scraping.xlsx", index=False, engine="openpyxl")
    print(f"\n✓ {len(semua_data)} quotes berhasil di simpan ke hasil_scraping.xlsx")

scrape_quotes()