"""
camera_app.py
-------------
Aplikasi utama: membaca feed webcam, mendeteksi gestur peace sign,
lalu mem-blur frame secara real-time saat gestur terdeteksi.
"""

import cv2

from . import config
from .audio_player import BackgroundMusicPlayer
from .gesture_detector import PeaceSignDetector


class PeaceBlurCameraApp:
    """Aplikasi kamera real-time dengan efek blur berbasis gestur tangan."""

    def __init__(self) -> None:
        self._detector = PeaceSignDetector(
            max_num_hands=config.MAX_NUM_HANDS,
            min_detection_confidence=config.MIN_DETECTION_CONFIDENCE,
            min_tracking_confidence=config.MIN_TRACKING_CONFIDENCE,
        )
        self._music = BackgroundMusicPlayer(config.BACKGROUND_MUSIC_PATH)
        self._capture = None
        self._is_fullscreen = False

    def run(self) -> None:
        """Jalankan loop utama aplikasi sampai user menutup window atau menekan 'q'."""
        self._capture = cv2.VideoCapture(config.CAMERA_INDEX)

        if not self._capture.isOpened():
            print("Kamera tidak bisa dibuka. Pastikan webcam terpasang dan tidak dipakai aplikasi lain.")
            return

        self._setup_window()
        self._music.play()

        print("Kamera aktif. Tunjukkan peace sign (✌️) untuk mengaktifkan blur.")
        print(f"Tekan '{config.KEY_TOGGLE_FULLSCREEN}' untuk fullscreen, '{config.KEY_QUIT}' untuk keluar.")

        try:
            self._loop()
        except KeyboardInterrupt:
            print("Dihentikan manual lewat Ctrl+C.")
        finally:
            self._cleanup()

    def _setup_window(self) -> None:
        cv2.namedWindow(config.WINDOW_NAME, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(config.WINDOW_NAME, config.WINDOW_WIDTH, config.WINDOW_HEIGHT)

    def _loop(self) -> None:
        while True:
            ok, frame = self._capture.read()
            if not ok:
                print("Gagal mengambil frame dari kamera, menghentikan aplikasi...")
                break

            frame = cv2.flip(frame, 1)  # efek cermin, lebih intuitif buat user

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            detection_result = self._detector.process(frame_rgb)

            if self._detector.any_hand_is_peace_sign(detection_result):
                frame = cv2.GaussianBlur(frame, config.BLUR_KERNEL_SIZE, 0)

            cv2.imshow(config.WINDOW_NAME, frame)

            if not self._handle_keyboard_and_window_state():
                break

    def _handle_keyboard_and_window_state(self) -> bool:
        """Tangani input keyboard & status window. Return False kalau aplikasi harus berhenti."""
        key = cv2.waitKey(1) & 0xFF

        if key == ord(config.KEY_QUIT):
            return False

        if key == ord(config.KEY_TOGGLE_FULLSCREEN):
            self._toggle_fullscreen()

        # Window ditutup manual lewat tombol X
        if cv2.getWindowProperty(config.WINDOW_NAME, cv2.WND_PROP_VISIBLE) < 1:
            return False

        return True

    def _toggle_fullscreen(self) -> None:
        self._is_fullscreen = not self._is_fullscreen
        if self._is_fullscreen:
            cv2.setWindowProperty(config.WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        else:
            cv2.setWindowProperty(config.WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
            cv2.resizeWindow(config.WINDOW_NAME, config.WINDOW_WIDTH, config.WINDOW_HEIGHT)

    def _cleanup(self) -> None:
        self._music.stop()
        self._detector.close()
        if self._capture is not None:
            self._capture.release()
        cv2.destroyAllWindows()
        print("Kamera & audio sudah dimatikan. Selesai.")
