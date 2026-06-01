# Virtual Background Replacement using OpenCV and Selfie Segmentation

## Overview

This project is a **real-time virtual background replacement system** built using **Python**, **OpenCV**, and **CvZone’s Selfie Segmentation module**.

The application captures live webcam video, removes the original background using AI-powered segmentation, and replaces it with custom background images. Users can dynamically switch between different backgrounds using keyboard controls.

This project demonstrates practical implementation of:

* Computer Vision
* Real-time Video Processing
* Background Segmentation
* Human Foreground Extraction
* OpenCV-based Interactive Applications

---

## Features

* Real-time webcam video capture
* AI-based background removal
* Replace background with custom images
* Switch between multiple backgrounds
* Live FPS (Frames Per Second) display
* Side-by-side comparison view
* Keyboard-controlled navigation

---

## Technologies Used

* **Python**
* **OpenCV**
* **CvZone**
* **Selfie Segmentation**
* **NumPy**

---

## Project Structure

```bash
Virtual-Background-Replacement/
│
├── Images/                 # Custom background images
│   ├── bg1.jpg
│   ├── bg2.jpg
│   └── ...
│
├── main.py                 # Main project file
└── README.md
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/virtual-background-replacement.git
cd virtual-background-replacement
```

### 2. Install Dependencies

Install required Python packages:

```bash
pip install opencv-python cvzone
```

---

## How to Run

Run the main Python file:

```bash
python main.py
```

---

## Controls

| Key   | Function            |
| ----- | ------------------- |
| **N** | Next background     |
| **B** | Previous background |
| **Q** | Quit application    |

---

## How It Works

### 1. Webcam Initialization

The system captures live video from the default webcam.

### 2. Background Segmentation

Using CvZone’s **SelfieSegmentation**, the human subject is separated from the background.

### 3. Background Replacement

The removed background is replaced with a selected custom image.

### 4. Real-Time Rendering

The original and processed outputs are displayed side-by-side.

### 5. Interactive Background Switching

Users can navigate through available backgrounds using keyboard inputs.

---

## Code Workflow

```text
Start
   ↓
Capture Webcam Frame
   ↓
Apply Selfie Segmentation
   ↓
Remove Background
   ↓
Insert Selected Background Image
   ↓
Display Output
   ↓
Listen for Keyboard Input
   ↓
Change Background / Exit
```

---

## Example Use Cases

* Virtual meetings
* Online classes
* Live streaming
* Video conferencing
* Computer vision learning projects

---

## Learning Outcomes

This project helps in understanding:

* Real-time computer vision systems
* Image segmentation concepts
* OpenCV video processing
* Human-computer interaction
* AI-assisted visual processing

---

## Future Improvements

Possible enhancements include:

* Blur background option
* Custom image upload during runtime
* Save processed video
* Gesture-based background switching
* Green screen simulation
* GUI integration using Tkinter or PyQt

---

## Screenshots

Add project screenshots here:

```bash
screenshots/output1.png
screenshots/output2.png
```

---

## Author

**Musfique Anam**
CSE Student | Computer Vision Enthusiast | Machine Learning Learner

---

## License

This project is open-source and available under the **MIT License**.
