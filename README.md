# 📐 Law of Cosines Triangle Solver

A simplified, interactive web application built with [Gradio](https://www.gradio.app/) that solves triangle geometry problems. This tool calculates missing sides and angles, provides detailed step-by-step mathematical solutions using LaTeX, and generates a to-scale visualization of the resulting triangle.

### ✨ Features

- **Multi-Case Support:** Solves triangles based on available information:
- **SSS (Side-Side-Side):** Calculates all angles given three sides.
- **SAS (Side-Angle-Side):** Calculates the third side and remaining angles.
- **ASA / AAS (Angle-Side-Angle):** Calculates remaining sides and angle.
- **Step-by-Step Derivations:** Displays the full mathematical process with rendered LaTeX equations.
- **Visual Plotting:** Generates a matplotlib graph of the triangle drawn to scale.
- **Data Validation:** Checks for valid triangle inequality and valid inputs.

🛠️ Prerequisites

You need Python 3.7+ installed along with the following libraries:
```
gradio

numpy

matplotlib
```

📦 Installation

Clone this repository or download the source code.

Install the required dependencies using pip:

pip install gradio numpy matplotlib


🚀 Usage

Save the code into a file named app.py.

Run the script:

python app.py


Open the local URL provided in the terminal (usually http://127.0.0.1:7860) in your web browser.

🧮 How to Use

Input Data: Enter the values you know in the Sides and Angles fields.

Note: Side $a$ is opposite Angle $A$, Side $b$ is opposite Angle $B$, etc.

Leave Blanks: Leave unknown values empty.

Click Solve: Press the 🔍 Solve Triangle button.

View Results:

The Results panel shows the final calculated values.

The Triangle Visualization panel shows the shape of the triangle.

Scroll down to Step-by-Step Solution to see the math used (Law of Cosines/Sines).

📚 Mathematical Concepts Used

Law of Cosines

Used primarily for SSS and SAS cases:
$$ c^2 = a^2 + b^2 - 2ab \cos(C) $$

Law of Sines

Used for calculating subsequent sides/angles after the initial Law of Cosines calculation:
$$ \frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} $$

🤝 Contributing

Feel free to fork this project and submit pull requests for improvements, such as adding ambiguous case handling (SSA) or area calculations.

📄 License

This project is open-source and available for educational purposes.
