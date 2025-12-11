# 📐 Law of Cosines Triangle Solver

A simplified, interactive web application built with [Gradio](https://www.gradio.app/) that solves triangle geometry problems. This tool calculates missing sides and angles, provides detailed step-by-step mathematical solutions using LaTeX, and generates a to-scale visualization of the resulting triangle.

## ✨ Features

- **Multi-Case Support:** Solves triangles based on available information:
- **SSS (Side-Side-Side):** Calculates all angles given three sides.
- **SAS (Side-Angle-Side):** Calculates the third side and remaining angles.
- **ASA / AAS (Angle-Side-Angle):** Calculates remaining sides and angle.
- **Step-by-Step Derivations:** Displays the full mathematical process with rendered LaTeX equations.
- **Visual Plotting:** Generates a matplotlib graph of the triangle drawn to scale.
- **Data Validation:** Checks for valid triangle inequality and valid inputs.

## 🛠️ Prerequisites

You need Python 3.7+ installed along with the following libraries:

- ```gradio```
- ```numpy```
- ```matplotlib```

## 📦 Installation

1. Clone this repository or download the source code.

2. Install the required dependencies using pip:
```pip install gradio numpy matplotlib``` or ```pip install -r requirements.txt```


## 🚀 Usage

### Local Dependencies & Run

1. After installing the dependencies, run the script: ```python app.py```

2. Open the local URL provided in the terminal (usually ```http://127.0.0.1:7860```) in your web browser.

### Docker Image (Pre-Built, Instant Run)

1. Pull the Docker image. Our image is available on the **Github Container Registry**, **Docker Hub**, and **HuggingFace Container Registry** (if you are using the HuggingFace Cotainer Registry, the image might be bigger because they use a different base image and install more dependencies than we do).

- To pull from **GHCR (Github Container Registry) run ```docker pull ghcr.io/alexscottcodes/cosine-solver:latest```.
- To pull from our official Docker Hub image, run ```docker pull browservm/law-of-cosines-solver:latest```.
- To pull from the HuggingFace Container Registry run

```
docker run -it -p 7860:7860 --platform=linux/amd64 \
	registry.hf.space/namelessai-cosine-solver:latest python app.py
```

If you pulled from the HuggingFace Container Registry, the app will start automatically. If you pulled from the other two, run the following:

- **GHCR:** ```docker run ghcr.io/alexscottcodes/cosine-solver```
- **Docker Hub** ```docker run browservm/law-of-cosines-solver```

## 🧮 How to Use

1. Input Data: Enter the values you know in the Sides and Angles fields.
2. Leave Blanks: Leave unknown values empty.
3. Click Solve: Press the 🔍 Solve Triangle button.
4. View Results:

The results panel shows the final calculated values.
The triangle visualization panel shows the shape of the triangle.
Scroll down to step-by-step Solution to see the math used (Law of Cosines/Sines).

## 📚 Mathematical Concepts Used

### Law of Cosines

Used primarily for SSS and SAS cases:
$$c^2 = a^2 + b^2 - 2ab \cos(C)$$

### Law of Sines

Used for calculating subsequent sides/angles after the initial Law of Cosines calculation:
$$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$$

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements, such as adding ambiguous case handling (SSA) or area calculations.

## 📄 License

This project is open-source and available for educational purposes.
