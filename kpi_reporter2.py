def read_kpi_from_sheet():
    # Kod içine gömülmüş sahte tablo verisi
    data = {
        "Revenue": "$45,000",
        "New Customers": 120,
        "Churn": "3.5%"
    }
    return data

def format_as_table(data):
    # Ham verileri basit bir metin tablosu haline getiren fonksiyon
    table = "-----------------------------\n"
    table += "| Metrik         | Değer    |\n"
    table += "-----------------------------\n"
    for key, value in data.items():
        table += f"| {key:<14} | {str(value):<8} |\n"
    table += "-----------------------------"
    return table

def send_automated_email(table_text):
    # Terminale e-posta atıyormuş gibi çıktı veren fonksiyon
    print("[OTOMATİK E-POSTA GÖNDERİLDİ]")
    print("Kime: yonetim@sirket.com")
    print("Konu: Aylık KPI Ham Veri Raporu")
    print("\n-----------------------------")
    print(table_text)

if __name__ == "__main__":
    # Script terminalden doğrudan çalıştırıldığında sırasıyla adımları uygular
    kpi_data = read_kpi_from_sheet()
    table_output = format_as_table(kpi_data)
    send_automated_email(table_output)
