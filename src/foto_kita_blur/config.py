"""
config.py
---------
Konfigurasi terpusat untuk aplikasi Peace Blur Cam.
Ubah nilai di sini untuk menyesuaikan perilaku aplikasi tanpa menyentuh logika utama.
"""

from pathlib import Path

# Path dasar proyek
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ASSETS_DIR = BASE_DIR / "assets"

# Audio
BACKGROUND_MUSIC_PATH = str(ASSETS_DIR / "background_music.wav")

# Kamera & jendela tampilan
CAMERA_INDEX = 0
WINDOW_NAME = "Foto Kita Blur TikTok"
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 720

# Deteksi tangan (MediaPipe)
MAX_NUM_HANDS = 1
MIN_DETECTION_CONFIDENCE = 0.7
MIN_TRACKING_CONFIDENCE = 0.7

# Efek blur (harus angka ganjil untuk Gaussian kernel)
BLUR_KERNEL_SIZE = (35, 35)

# Keyboard shortcut
KEY_QUIT = "q"
KEY_TOGGLE_FULLSCREEN = "f"
