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

> ⚠️ **Penting:** gunakan **Python 3.11 atau 3.12**. MediaPipe belum stabil di Python versi terbaru (3.13/3.14) dan bisa menyebabkan error `module 'mediapipe' has no attribute 'solutions'`.

1. **Clone repository**
   ```bash
   git clone https://github.com/kristianNatalis/foto-kita-blur-tiktok-.git
   cd foto-kita-blur-tiktok-
   ```

2. **Buat virtual environment** (wajib pakai Python 3.11/3.12)
   ```bash
   py -3.12 -m venv venv
   venv\Scripts\activate         # Windows
   source venv/bin/activate      # Linux / macOS
   ```

3. **Install dependency**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi**
   ```bash
   python main.py
   ```

### 🛠️ Troubleshooting

**Error `module 'mediapipe' has no attribute 'solutions'`**
Ini terjadi kalau versi MediaPipe atau Python yang dipakai tidak kompatibel. Pastikan:
- Pakai Python 3.11 atau 3.12 (bukan 3.13/3.14)
- Versi dependency sesuai `requirements.txt` (sudah di-pin ke versi yang stabil)

Kalau masih error meski sudah pakai Python yang benar, reset environment-nya:
```bash
pip uninstall mediapipe numpy opencv-python opencv-contrib-python -y
pip install -r requirements.txt
```

## 🎮 Kontrol

| Tombol | Fungsi               |
|--------|-----------------------|
| `✌️`   | Aktifkan efek blur     |
| `f`    | Toggle fullscreen      |
| `q`    | Keluar aplikasi        |

## 🛠️ Teknologi

- [OpenCV](https://opencv.org/) `4.10.0` — pemrosesan video & tampilan kamera
- [MediaPipe](https://developers.google.com/mediapipe) `0.10.14` — deteksi landmark tangan
- [Pygame](https://www.pygame.org/) — pemutaran audio



## 📄 Lisensi

Proyek ini dirilis di bawah lisensi [MIT](LICENSE).
