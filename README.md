# 🃏 Real-Time Poker Hand Evaluator using YOLOv8

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![YOLO](https://img.shields.io/badge/YOLO-v8-yellow.svg)

> A high-performance Computer Vision system that detects playing cards via webcam or video input and evaluates standard Poker hands (e.g., Royal Flush, Full House) in real-time.

---

## 🎬 Demo

![Poker Demo](./detection/Poker_Detection.gif)

---

## 🚀 Key Features

* **Real-Time Object Detection**
  Uses a fine-tuned YOLOv8 model to accurately detect and classify all 52 playing cards with high confidence.

* **Optimized Evaluation Logic**
  Built a fast and efficient poker hand evaluation engine using Python’s `collections.Counter`, eliminating unnecessary loops and significantly improving performance.

* **False-Positive Mitigation**
  Handles overlapping and duplicate detections using dynamic set-based filtering, preventing errors caused by redundant bounding boxes.

* **Dynamic & Responsive UI**
  Implements OpenCV’s `getTextSize()` to automatically adjust text boundaries, ensuring labels remain visible and properly aligned across different resolutions.

---

## 🛠️ Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/jefanno1/realtime-poker-hand-evaluator.git
cd realtime-poker-hand-evaluator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Detector

Make sure `playingCards.pt` and your test video (if not using a webcam) are in the correct directory. (following the project structure)

```bash
python PokerDetection.py
```

---

## 🧠 Under the Hood (Technical Highlights)

### Algorithmic Refactoring

Traditional poker evaluation often relies on nested loops and complex conditional logic. This project replaces that approach with Python’s `collections.Counter` to analyze frequency distributions directly.

For example:

* `[3, 2]` → Full House
* `[2, 2, 1]` → Two Pair

This refactor reduces code complexity by over 60% while making the evaluation faster and cleaner.

---

### Mitigating YOLO False Positives (Overlapping Boxes)

In real-world scenarios, YOLO may occasionally produce duplicate detections for a single card. Feeding more than five cards into the evaluator can break the logic.

To solve this:

* A deduplication pipeline using Python’s `set()` is applied
* Duplicate detections are filtered before entering the evaluation stage

This ensures system stability even under noisy detection conditions.

---


## 📌 Notes

* Ensure your YOLO model (`playingCards.pt`) is properly trained for best accuracy
* Works with both webcam streams and pre-recorded video inputs
* Designed for real-time performance, so GPU acceleration is recommended

---

## 📄 License

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgments

* YOLOv8 for object detection framework
* OpenCV for real-time image processing
* Python ecosystem for rapid development and optimization
