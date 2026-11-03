#!/usr/bin/env python3
# Sonsuz Çay Demleme Dengesi Simülatörü
# Bu kod aslında çay demlemez, sadece demliyor gibi yapar.
# Bilimsel dayanağı yoktur. Garantisi de yoktur.

import time
import random
import sys

def sonsuz_cay_demle():
    print("🍵 Sonsuz Çay Demleme Dengesi başlatılıyor...")
    print("Uyarı: Bu süreç asla bitmeyecek. Çayınız soğuyabilir. Hayatınız da.")
    print("-" * 50)
    
    sicaklik = 80.0
    demleme_suresi = 0
    denge_bozuldu = False
    
    while True:
        demleme_suresi += 1
        sicaklik += random.uniform(-0.5, 1.2)
        
        if sicaklik > 100:
            print(f"🔥 {demleme_suresi}. saniye: Çay kaynadı! Denge tamamen bozuldu.")
            denge_bozuldu = True
        elif sicaklik < 60:
            print(f"❄️ {demleme_suresi}. saniye: Çay soğudu. Hayatın anlamı sorgulanıyor...")
        else:
            durumlar = [
                "Demleniyor... belki",
                "Denge korunuyor (yalan)",
                "Çay taneleri dans ediyor",
                "Evren genişliyor, çay daralıyor",
                "Bu süreç sonsuz, sen de sonsuzsun"
            ]
            print(f"☕ {demleme_suresi}. saniye: {random.choice(durumlar)} | Sıcaklık: {sicaklik:.1f}°C")
        
        if denge_bozuldu and random.random() < 0.1:
            print("\n🎯 Denge bozulduğu için çay kendini yok etti. Yeniden başlatılıyor...")
            sicaklik = 80.0
            denge_bozuldu = False
        
        time.sleep(0.8)
        if demleme_suresi > 10000:  # pratikte sonsuz
            print("Hata: Sonsuzluk bile sıkıldı.")
            break

if __name__ == "__main__":
    try:
        sonsuz_cay_demle()
    except KeyboardInterrupt:
        print("\n\n🚫 Çay demleme işlemi insan tarafından durduruldu.")
        print("Sonuç: Çay demlenmedi. Denge bozuldu. Her şey boşuna.")
        sys.exit(0)

# Gizli not: bazen denge bozulması gerekir ki yeni şeyler doğsun. (sadece bir gözlem)
