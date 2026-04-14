import time
import datetime

def get_monthly_kpis() -> dict:
    """Veritabanından çekilmiş gibi davranan sahte aylık veri tablosu (dictionary)."""
    return {
        "ay": datetime.datetime.now().strftime('%Y-%m'),
        "aylik_gelir": "425.000 ₺",
        "yeni_musteri_sayisi": 215,
        "iptal_eden_musteri": 18,
        "iptal_orani": "%2.5",
        "musteri_memnuniyeti_puani": "9.4/10"
    }

def mock_ai_analyst(data: dict) -> str:
    """Sayısal KPI verilerini alır ve yöneticiler için kısa, motive edici ve doğal bir metne (AI raporu) dönüştürür."""
    summary = (
        f"📊 *{data['ay']} Dönemi - Yönetim Durum Özeti* 📊\n\n"
        f"Ekip merhaba! Bu ayı harika metriklerle geride bıraktık. Toplam gelirimiz *{data['aylik_gelir']}* seviyelerine ulaştı "
        f"ve ailemize *{data['yeni_musteri_sayisi']}* yeni müşteri daha katıldı! 🥳\n\n"
        f"Ayrılan ({data['iptal_eden_musteri']}) müşterilerimiz olsa da, müşteri koruma eforlarımız sayesinde iptal oranını *{data['iptal_orani']}* "
        f"gibi oldukça iyi bir seviyede tutmayı başardık. Üstelik anketlere yansıyan *{data['musteri_memnuniyeti_puani']}*'lük müşteri memnuniyet skoru, "
        f"işimizi ne kadar iyi yaptığımızın en büyük kanıtı.\n\n"
        f"Önümüzdeki ay ivmemizi daha da artırmak dileğiyle. Herkesin eline sağlık! 🚀"
    )
    return summary

def main():
    print("[*] Zamanlanmış Görev (Cron Trigger) Başlatıldı...")
    time.sleep(1) # Gerçekçi bir gecikme (delay) simülasyonu
    
    print("[*] Veritabanından Aylık KPI Değerleri Çekiliyor...")
    kpis = get_monthly_kpis()
    time.sleep(1)
    
    print("[*] Veriler Yorumlanmak Üzere Yapay Zeka Analistine İletiliyor...")
    ai_report_text = mock_ai_analyst(kpis)
    time.sleep(1.5)
    
    print("\n=======================================================")
    print("              [SLACK MESAJI GÖNDERİLDİ]                ")
    print("=======================================================")
    print("Hedef Kanal: #yonetim-raporlari\n")
    print(ai_report_text)
    print("\n=======================================================")
    print("[*] Görev başarıyla tamamlandı ve işlem sonlandırıldı.")

if __name__ == "__main__":
    main()
