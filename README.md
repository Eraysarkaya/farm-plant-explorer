# Farm Plant Explorer

Bitki adı yazarak yetiştirme bilgilerini aramaya yarayan küçük bir masaüstü uygulaması. Verileri OpenFarm API'den alır ve Kivy arayüzünde gösterir; Python ile API ve masaüstü arayüzü pratiği için geliştirilmiştir.

## Çalıştırma

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python chatbot.py
```

Windows'ta sanal ortamı `.venv\Scripts\activate` ile açın. Giriş dosyasının adı `chatbot.py` olsa da uygulama sohbet botu değil, bitki arama arayüzüdür. Boş arama, ağ kesintisi ve geçersiz API yanıtları için temel hata yönetimi içerir. Bitki bilgilerini almak için internet bağlantısı gerekir.

## Lisans

[MIT](LICENSE).
