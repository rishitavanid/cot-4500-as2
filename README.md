# **Polynomial Interpolation - COT 4500 Assignment 2** 

Welcome to **Programming Assignment 2**! This project explores **polynomial interpolation**, a key numerical method for approximating values using known data points. 🚀  

## **📌 Overview**  

Polynomial interpolation allows us to approximate points on complicated curves by constructing **the lowest-degree polynomial** that passes through a given set of points.  

In this assignment, we implement **five powerful interpolation techniques**:  

✔ **Neville’s Method** - Finds a 2nd-degree interpolating value.  
✔ **Newton’s Forward Interpolation** - Computes polynomials of degree 1, 2, and 3.  
✔ **Newton’s Forward Interpolation Evaluation** - Approximates a given function value.  
✔ **Hermite Interpolation** - Constructs a divided difference table for derivatives.  
✔ **Cubic Spline Interpolation** - Computes piecewise polynomial coefficients.  

This project involves **matrix operations**, **difference tables**, and **multiple numerical methods**, making it a great exercise in numerical computing! 💡  

---

## **🛠️ Project Structure**  

Your project should be structured as follows:  

```
cot-4500-as2/
│-- src/
│   │-- main/
│   │   │-- __init__.py
│   │   │-- assignment_2.py  # All interpolation methods implemented here
│   │-- test/
│   │   │-- __init__.py
│   │   │-- test_assignment_2.py  # Unit tests for verification
│-- requirements.txt  # Required dependencies
│-- README.md  # This file!
```

---

## **📋 Installation Instructions**  

Before running the code, ensure you have **Python 3.10+** installed. Then, follow these steps:  

### **1️⃣ Set Up a Virtual Environment (Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

> 📌 **Note:** If you already have `numpy` and `scipy` installed, you may skip this step.

---

## **🚀 How to Run the Program**  

### **Run the Main Script**
To execute the interpolation methods, run:
```bash
python src/main/assignment_2.py
```
This will print the **Neville’s interpolation, Newton’s method, Hermite table, and cubic spline results.**  

---

## **🔎 How to Run Tests**  

This project includes **unit tests** to ensure numerical accuracy. Run:
```bash
python -m unittest discover -s src/test
```
If all tests pass, you’ll see:
```
Ran 4 tests in 0.002s
OK
```
If there are any issues, verify the expected values and precision.

---

## **📌 Methods Implemented & Expected Outputs**  

### **1️⃣ Neville’s Method - Find `f(3.7)`**
**Data:**
```
x       f(x)
3.6     1.675
3.8     1.436
3.9     1.318
```
✔ Expected Output:
```
Neville's Interpolation f(3.7): 1.555000
```

---

### **2️⃣ Newton’s Forward Method - Print Polynomial Approximations**
**Data:**
```
x       f(x)
7.2     23.5492
7.4     25.3913
7.5     26.8224
7.6     27.4589
```
✔ Expected Output:
```
Polynomial Degree 1: P(x) = ...
Polynomial Degree 2: P(x) = ...
Polynomial Degree 3: P(x) = ...
```

---

### **3️⃣ Approximate `f(7.3)` using Newton’s Forward Interpolation**
✔ Expected Output:
```
Newton's Forward Interpolation f(7.3): 24.016575
```

---

### **4️⃣ Hermite Interpolation - Print Divided Difference Matrix**
**Data:**
```
x       f(x)     f’(x)
3.6     1.675    -1.195
3.8     1.436    -1.188
3.9     1.318    -1.182
```
✔ Expected Output:
```
Hermite Interpolation Table:
[[  1.675   -1.195  ... ]
 [  1.675   -1.195  ... ]
 ...
```

---

### **5️⃣ Cubic Spline Interpolation**
**Data:**
```
x       f(x)
2       3
5       5
8       7
10      9
```
✔ Expected Output:
```
Cubic Spline Interpolation: f(6) ≈ 5.600601
```

✔ **Find Matrix `A`**  
✔ **Find Vector `b`**  
✔ **Find Vector `x`**  

---

## **📌 Final Submission Checklist** ✅  
✔ **Code is structured correctly (`src/main/`, `src/test/`)**  
✔ **README includes clear instructions**  
✔ **All methods work as expected**  
✔ **Unit tests pass (`OK` message when running tests)**  
✔ **Screenshots of output are attached (if required)**  
✔ **Uploaded to GitHub as `cot-4500-as2` repository**  

---

### **🔗 References**
- [NumPy Documentation](https://numpy.org/doc/)
- [SciPy Interpolation](https://docs.scipy.org/doc/scipy/reference/interpolate.html)
- [Python Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/)

---

