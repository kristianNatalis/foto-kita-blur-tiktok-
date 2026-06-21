"""
main.py
-------
Entry point aplikasi Peace Blur Cam.

Jalankan dengan:
    python main.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from foto_kita_blur import PeaceBlurCameraApp  # noqa: E402


def main() -> None:
    app = PeaceBlurCameraApp()
    app.run()


if __name__ == "__main__":
    main()
