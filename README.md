# Foto Kita Blur TikTok ✌️

Aplikasi kamera real-time berbasis Python yang otomatis mem-blur tampilan layar saat pengguna menunjukkan gestur **peace sign (✌️)** di depan webcam — lengkap dengan musik latar yang diputar selama aplikasi berjalan. Terinspirasi dari tren "foto kita blur" yang viral di TikTok.

Dibangun menggunakan **OpenCV** untuk pemrosesan video, **MediaPipe Hands** untuk deteksi landmark tangan, dan **Pygame** untuk audio.

## ✨ Fitur

- Deteksi gestur tangan secara real-time menggunakan MediaPipe Hands
- Efek Gaussian Blur otomatis saat gestur peace sign terdeteksi
- Musik latar yang diputar otomatis dan berulang (loop) selama aplikasi berjalan
- Mode fullscreen yang bisa di-toggle kapan saja
- Struktur kode modular (config, detector, audio player, app) yang mudah dikembangkan

## 📂 Struktur Proyek

```
foto-kita-blur-tiktok/
├── main.py                      # Entry point aplikasi
├── requirements.txt             # Daftar dependency
├── assets/
│   └── background_music.wav     # Musik latar
└── src/
    └── foto_kita_blur/
        ├── __init__.py
        ├── config.py             # Konfigurasi terpusat
        ├── gesture_detector.py   # Deteksi gestur peace sign
        ├── audio_player.py       # Pemutar musik latar
        └── camera_app.py         # Logika aplikasi utama
```

## 🚀 Instalasi & Menjalankan

1. **Clone repository**
   ```bash
   git clone https://github.com/kristianNatalis/foto-kita-blur-tiktok-.git
   cd foto-kita-blur-tiktok
   ```

2. **Buat virtual environment (opsional, direkomendasikan)**
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux / macOS
   venv\Scripts\activate         # Windows
   ```

3. **Install dependency**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi**
   ```bash
   python main.py
   ```

## 🎮 Kontrol

| Tombol | Fungsi               |
|--------|-----------------------|
| `✌️`   | Aktifkan efek blur     |
| `f`    | Toggle fullscreen      |
| `q`    | Keluar aplikasi        |

## 🛠️ Teknologi

- [OpenCV](https://opencv.org/) — pemrosesan video & tampilan kamera
- [MediaPipe](https://developers.google.com/mediapipe) — deteksi landmark tangan
- [Pygame](https://www.pygame.org/) — pemutaran audio

## 📄 Lisensi

Proyek ini dirilis di bawah lisensi [MIT](LICENSE).
