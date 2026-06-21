"""
audio_player.py
----------------
Modul kecil untuk memutar musik latar (background music) selama aplikasi berjalan.
"""

import pygame


class BackgroundMusicPlayer:
    """Wrapper sederhana di atas pygame.mixer untuk memutar musik latar secara loop."""

    def __init__(self, file_path: str) -> None:
        self._file_path = file_path
        self._initialized = False

    def play(self) -> None:
        """Inisialisasi mixer lalu putar musik secara berulang (loop tanpa henti)."""
        pygame.mixer.init()
        pygame.mixer.music.load(self._file_path)
        pygame.mixer.music.play(loops=-1)
        self._initialized = True

    def stop(self) -> None:
        """Hentikan musik jika sedang berjalan."""
        if self._initialized:
            pygame.mixer.music.stop()
