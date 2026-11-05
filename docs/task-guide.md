# Task Guide and Individual Write-Up Notes

The PDF requires each task discussion to identify inputs and operations, change at least one input or parameter, interpret the output (including graphs), and document a related real-world case with its assumptions, data, output, and interpretation. The notes below record the implemented examples and provide a starting point for the individual write-up. Use your own words and add any lecturer-required evidence.

## Task 02: NumPy Arrays

- **Inputs and operation:** 24 hourly Celsius readings; NumPy computes mean, minimum, maximum, and the element-wise conversion $F=1.8C+32$.
- **Change and interpretation:** Adding 2 C to every reading raises all three summary statistics by 2 C. The baseline daily mean is 23.12 C, with a 17.50-29.40 C range.
- **Related case:** Use hourly temperatures from a greenhouse. Assume the sensors are calibrated and report Celsius; convert the daily series to Fahrenheit for an overseas operator. The converted series preserves the same ordering and its mean is converted by the same formula.

## Task 03: Vectorization

- **Inputs and operation:** One million seeded latency samples in milliseconds; convert to seconds and square each value, comparing a Python loop with NumPy vectorization.
- **Change and interpretation:** Reducing the sample to 500,000 processes half as many readings. Runtime varies by machine; in the example run, vectorization was about 33 times faster.
- **Related case:** Process a day's sensor latency logs instead of simulated network readings. Assume each record is in milliseconds; convert and square the records to compute a mean squared latency, with vectorization reducing processing time on large logs.

## Task 04: Floating-Point Error

- **Inputs and operation:** Decimal values 0.1, 0.2, and 0.3 plus an approximation to sqrt(2); compare exact equality, tolerance-based equality, absolute/relative error, and stable versus cancellation-prone formulas.
- **Change and interpretation:** At x=1e-12, direct subtraction loses visible precision while the algebraically equivalent stable expression remains close to 0.5. Changing x to 1e-6 provides a less extreme comparison.
- **Related case:** Validate a sensor calibration result against a reference measurement. Assume the instrument tolerance is specified; report absolute and relative error and use a tolerance-aware comparison rather than exact floating-point equality.

## Task 05: Matrix Algebra

- **Inputs and operation:** Four square-corner coordinates, scale factors 2 and 1.5, and a 45-degree rotation; compose transformation matrices and multiply each point.
- **Change and interpretation:** Reducing rotation to 30 degrees changes the transformed coordinates while the scale remains fixed. The determinant 3 is the area scale factor.
- **Related case:** Transform a small set of robot-map coordinates. Assume coordinates are in metres and the same planar scale and rotation apply to every point; the resulting coordinates are in the rotated/scaled frame.

## Task 06: Linear Systems

- **Inputs and operation:** CPU and memory totals with per-server resource coefficients; solve $Ax=b$ and inspect the residual.
- **Change and interpretation:** Raising total CPU from 20 to 24 while holding memory at 72 changes the solution from 3 Type A and 4 Type B servers to 4 Type A and 3 Type B. A zero residual confirms the equations are satisfied.
- **Related case:** Estimate quantities of two machine types from power and floor-space totals. Assume each machine type has fixed resource use and the totals are exact; the solution gives the quantities consistent with both measurements.

## Task 07: Gaussian Elimination and LU

- **Inputs and operation:** One 3-by-3 coefficient matrix reused for three measurement vectors; LU-factor once, solve each right-hand side, and check residual norms.
- **Change and interpretation:** Changing the first measurement from 15 to 18 changes the solution, while reusing the factorization agrees with a direct solve.
- **Related case:** Repeatedly estimate the state of a small electrical network as sensor measurements change. Assume the network coefficients stay fixed; factorization is reusable and near-zero residuals indicate consistent solutions.

## Task 08: Iterative Linear Methods

- **Inputs and operation:** A diagonally dominant five-node temperature system; Jacobi and Gauss-Seidel iteratively update estimates and compare with a direct solve.
- **Change and interpretation:** Relaxing tolerance from 1e-8 to 1e-4 reduces Jacobi iterations from 150 to 86 but permits a less precise answer. The plot shows error decreasing; Gauss-Seidel reaches the stated tolerance in fewer iterations for this system.
- **Related case:** Estimate steady temperatures at five points along an insulated pipe. Assume boundary temperatures are fixed and conduction is represented by the given linear equations; the converged vector approximates the interior temperatures.

## Task 09: Eigenvalues and Eigenvectors

- **Inputs and operation:** An undirected four-node adjacency matrix; find its largest eigenvalue and normalize the corresponding eigenvector as node-importance scores.
- **Change and interpretation:** Adding a connection between A and D makes this example's scores equal at 0.25, showing that network structure affects relative centrality.
- **Related case:** Rank intersections in a small road network. Assume links are undirected and a node's importance increases when connected to important nodes; the normalized dominant eigenvector gives a relative score, not a causal measure.

## Task 10: Bisection and Fixed Point

- **Inputs and operation:** A heat-balance residual and bracket [20, 40] C; find its zero by bisection and solve its equivalent fixed-point equation.
- **Change and interpretation:** Raising heat gain from 10 to 12 moves the equilibrium from about 27.525 C to 27.964 C. Both baseline methods agree, and the residual at the root is nearly zero. The graph's crossing of zero marks the equilibrium.
- **Related case:** Find an equipment set point where modeled heat input equals heat loss. Assume the model is valid across the bracket and has a sign change there; the root is the balance temperature.

## Task 11: Newton-Raphson and Secant

- **Inputs and operation:** Initial investment and annual cash flows; solve net present value equals zero using a derivative-based Newton method and a secant method.
- **Change and interpretation:** Both methods give an internal rate of return of about 11.542%; NPV at the root is approximately zero. Increasing the final inflow from 2500 to 3000 raises IRR to about 13.038%.
- **Related case:** Evaluate a different equipment purchase with a known upfront cost and projected annual savings. Assume cash flows occur at year-end and the model has a meaningful single root; the computed rate is the discount rate that makes NPV zero.

## Task 12: Nonlinear Equations

- **Inputs and operation:** Two residual equations describing a circle and parabola; SciPy's root solver searches for intersections from initial guesses.
- **Change and interpretation:** Different starting guesses find the positive and negative x intersections. Residual norms near zero verify that both equations hold at the returned points.
- **Related case:** Find where a circular component boundary meets a curved conveyor path. Assume both shapes share a coordinate system; each root is a geometric intersection, and the initial guess can determine which one is found.

## Task 13: Interpolation

- **Inputs and operation:** Seven hourly temperatures from 08:00 to 14:00; evaluate linear and cubic-spline interpolants at 10-minute intervals.
- **Change and interpretation:** Moving the query from 10:30 to 11:30 changes the estimated temperature from about 23.25/23.36 C to 24.50/24.54 C (linear/cubic). The graph passes through measured points; estimates between them are not new observations.
- **Related case:** Estimate water temperature between hourly river samples. Assume the measured interval is representative and avoid extrapolating beyond the first and last samples; the interpolated values fill reporting timestamps.

## Task 14: Curve Fitting

- **Inputs and operation:** User loads and measured response times; fit a quadratic with least squares, calculate RMSE, and predict response for new loads.
- **Change and interpretation:** Prediction increases from about 377.86 ms at 400 users to 463.21 ms at 450. The 1.55 ms training RMSE summarizes in-sample fit error; extrapolated predictions are less certain.
- **Related case:** Fit a quadratic model to measured pump throughput versus operating load. Assume measurements cover the intended operating region and residuals are acceptable; use fitted predictions for planning, not as guaranteed performance.

## Task 15: Numerical Differentiation

- **Inputs and operation:** GPS time and position samples; estimate speed with finite differences using `numpy.gradient`.
- **Change and interpretation:** Applying a +5% position calibration factor raises the estimated speed by 5%; at 3 seconds, speed changes from 6.25 to 6.56 m/s. Endpoint estimates rely on one-sided information and may be less reliable.
- **Related case:** Estimate conveyor-belt speed from recorded positions. Assume timestamps are accurate and samples are close enough for finite differences; the derivative estimates instantaneous speed in metres per second.

## Task 16: Numerical Integration

- **Inputs and operation:** Power readings every two hours; integrate power over time with trapezoidal and Simpson rules to estimate kWh.
- **Change and interpretation:** A 10% increase in every reading raises trapezoidal energy from 15.700 to 17.270 kWh and Simpson energy from 15.800 to 17.380 kWh. The small baseline difference reflects numerical approximation.
- **Related case:** Estimate daily water volume from flow-meter samples. Assume flow is in volume per hour and readings represent the intervals; integrating flow over time gives total volume.

## Task 17: Euler ODE

- **Inputs and operation:** Ambient and initial temperatures, cooling constant, and time step; Euler updates Newton's law of cooling and is compared with the exact solution.
- **Change and interpretation:** Reducing step size from 1 to 0.5 minute reduces final absolute error from 0.372 C to 0.189 C. The graph shows the numerical trajectory approaching the exact cooling curve.
- **Related case:** Predict cooling of a food container. Assume a constant ambient temperature and cooling coefficient; smaller time steps improve approximation but require more updates.

## Task 18: SciPy ODE

- **Inputs and operation:** RC supply voltage, resistance, capacitance, and initial voltage; `solve_ivp` integrates the charging equation and is checked against its exact solution.
- **Change and interpretation:** Increasing supply voltage from 5 to 6 V raises the 5-second voltage from about 4.966 to 5.960 V. The baseline maximum error is below 1e-9 V for these tolerances; the graph approaches the supply voltage.
- **Related case:** Model a different capacitor in a sensor circuit. Assume a constant supply and ideal resistor/capacitor; changing R or C changes the time constant and therefore the charging speed.

## Task 19: Optimization

- **Inputs and operation:** Per-unit cost and capacity for two server types plus a minimum capacity; minimize linear cost subject to capacity and nonnegative bounds.
- **Change and interpretation:** Raising required capacity from 1000 to 1200 increases the continuous minimum cost from about 105.88 to 127.06. The continuous solution can be fractional; the integer check gives 6 Type B units at cost 108 for the baseline requirement.
- **Related case:** Choose machine capacity to meet a minimum production target at least cost. Assume costs and capacities add linearly; enumerate integer machines when fractional units are physically impossible.

## Task 20: Monte Carlo

- **Inputs and operation:** 100,000 seeded normal-demand samples with mean 850 and standard deviation 120; estimate overload probability as the fraction exceeding capacity.
- **Change and interpretation:** Estimated overload rises from 10.616% at capacity 1000 to 20.221% at capacity 950. The histogram visualizes simulated demand and capacity thresholds; the estimate is random-sampling based and has finite-sample uncertainty.
- **Related case:** Estimate the chance a clinic exceeds daily staffing capacity from uncertain patient demand. Assume historical demand is reasonably modeled by the selected distribution; the simulation fraction estimates risk under that assumption.
