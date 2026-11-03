# BIT 2118 Scientific Computing Group Work

This project implements every coded activity in the supplied assignment PDF. It contains Tasks 02-20; the PDF lists **Data Science Essentials with Python** as a self-paced prerequisite rather than a program task.

## Before starting

- [ ] Complete the Data Science Essentials with Python prerequisite.
- [ ] Install Python 3.10 or later.
- [ ] Install the project dependencies.
- [ ] Run each task and review its explanation in [`docs/task-guide.md`](docs/task-guide.md).
- [ ] Record your own discussion, screenshots, and individual GitHub repository link for VLMS submission.

The assignment specifies that discussion is group work, but each student must maintain and submit an individual GitHub repository. Do not submit a shared group repository as your individual submission.

## Setup

From this project folder, run:

```powershell
python -m pip install -r requirements.txt
```

Run an individual task, for example:

```powershell
python code/Task_02_numpy_arrays.py
```

Run the complete assignment check:

```powershell
python -m unittest discover -s tests -v
```

Scripts are independent and contain their sample inputs. Plot-based tasks save figures in `outputs/` and do not open interactive windows, so they also run in automated environments.

## Project layout

```text
code/       One runnable Python program for each PDF task, Tasks 02-20
docs/       Task explanations, parameter changes, interpretations, and extensions
outputs/    Generated figures from the plotting tasks
tests/      Automated smoke test for every program
```

## Tasks

| PDF task | Topic                                          | Program                                     |
| -------- | ---------------------------------------------- | ------------------------------------------- |
| 02       | NumPy arrays and numerical computation         | `code/Task_02_numpy_arrays.py`              |
| 03       | Mathematical functions and vectorization       | `code/Task_03_vectorization.py`             |
| 04       | Floating-point arithmetic and numerical errors | `code/Task_04_numerical_errors.py`          |
| 05       | Matrix algebra and matrix operations           | `code/Task_05_matrix_algebra.py`            |
| 06       | Systems of linear equations                    | `code/Task_06_linear_systems.py`            |
| 07       | Gaussian elimination and LU decomposition      | `code/Task_07_gaussian_lu.py`               |
| 08       | Iterative methods for linear systems           | `code/Task_08_iterative_linear.py`          |
| 09       | Eigenvalues and eigenvectors                   | `code/Task_09_eigenvalues.py`               |
| 10       | Bisection and fixed-point root finding         | `code/Task_10_bisection_fixed_point.py`     |
| 11       | Newton-Raphson and secant methods              | `code/Task_11_newton_secant.py`             |
| 12       | Polynomial and nonlinear equations             | `code/Task_12_nonlinear_equations.py`       |
| 13       | Interpolation                                  | `code/Task_13_interpolation.py`             |
| 14       | Curve fitting and approximation                | `code/Task_14_curve_fitting.py`             |
| 15       | Numerical differentiation                      | `code/Task_15_numerical_differentiation.py` |
| 16       | Numerical integration                          | `code/Task_16_numerical_integration.py`     |
| 17       | Euler method for ODEs                          | `code/Task_17_euler_ode.py`                 |
| 18       | SciPy ODE solution                             | `code/Task_18_scipy_ode.py`                 |
| 19       | Numerical optimization                         | `code/Task_19_optimization.py`              |
| 20       | Random numbers and Monte Carlo                 | `code/Task_20_monte_carlo.py`               |
