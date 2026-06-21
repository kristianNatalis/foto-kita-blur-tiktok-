"""
gesture_detector.py
--------------------
Modul untuk mendeteksi gestur tangan "peace sign" (✌️) menggunakan MediaPipe Hands.

Index landmark tangan mengikuti urutan baku dari MediaPipe:
https://developers.google.com/mediapipe/solutions/vision/hand_landmarker
"""

from dataclasses import dataclass

import mediapipe as mp


@dataclass(frozen=True)
class HandLandmarkIndex:
    """Index titik (landmark) ujung & sendi setiap jari, sesuai standar MediaPipe."""

    THUMB_TIP: int = 4
    THUMB_IP: int = 3
    INDEX_TIP: int = 8
    INDEX_PIP: int = 6
    MIDDLE_TIP: int = 12
    MIDDLE_PIP: int = 10
    RING_TIP: int = 16
    RING_PIP: int = 14
    PINKY_TIP: int = 20
    PINKY_PIP: int = 18


class PeaceSignDetector:
    """
    Mendeteksi formasi tangan "peace sign":
    - Telunjuk berdiri
    - Jari tengah berdiri
    - Jari manis & kelingking menekuk
    - Jempol menekuk ke dalam (bukan mengacung ke samping)
    """

    LM = HandLandmarkIndex()

    def __init__(self, max_num_hands: int = 1,
                 min_detection_confidence: float = 0.7,
                 min_tracking_confidence: float = 0.7) -> None:
        self._mp_hands = mp.solutions.hands
        self._hands = self._mp_hands.Hands(
            max_num_hands=max_num_hands,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence,
        )

    def process(self, frame_rgb):
        """Jalankan deteksi tangan pada satu frame RGB, kembalikan hasil mentah MediaPipe."""
        return self._hands.process(frame_rgb)

    def is_peace_sign(self, landmarks, handedness_label: str) -> bool:
        """Cek apakah landmark tangan yang diberikan membentuk peace sign."""
        lm = landmarks

        index_up = lm[self.LM.INDEX_TIP].y < lm[self.LM.INDEX_PIP].y
        middle_up = lm[self.LM.MIDDLE_TIP].y < lm[self.LM.MIDDLE_PIP].y
        ring_down = lm[self.LM.RING_TIP].y > lm[self.LM.RING_PIP].y
        pinky_down = lm[self.LM.PINKY_TIP].y > lm[self.LM.PINKY_PIP].y

        # Gerakan jempol dicek secara horizontal karena arah tekuknya beda dari jari lain
        if handedness_label == "Right":
            thumb_folded = lm[self.LM.THUMB_TIP].x > lm[self.LM.THUMB_IP].x
        else:
            thumb_folded = lm[self.LM.THUMB_TIP].x < lm[self.LM.THUMB_IP].x

        return index_up and middle_up and ring_down and pinky_down and thumb_folded

    def any_hand_is_peace_sign(self, detection_result) -> bool:
        """Cek apakah ada minimal satu tangan yang membentuk peace sign pada hasil deteksi."""
        if not (detection_result.multi_hand_landmarks and detection_result.multi_handedness):
            return False

        for hand_landmarks, handedness in zip(
            detection_result.multi_hand_landmarks,
            detection_result.multi_handedness,
        ):
            label = handedness.classification[0].label
            if self.is_peace_sign(hand_landmarks.landmark, label):
                return True

        return False

    def close(self) -> None:
        self._hands.close()
