#  Portfolio Optimization using Modern Portfolio Theory

This project implements a portfolio optimization tool using Modern Portfolio Theory (Markowitz framework). It uses historical stock data to compute optimal asset allocations based on expected returns and risk, helping investors build a risk-adjusted, diversified portfolio.

---

## Project Highlights

- Fetches real-time stock data using Yahoo Finance
- Calculates expected returns, volatility, and Sharpe ratio
- Solves for optimal asset weights using convex optimization (`cvxpy`)
- Visualizes allocations and the efficient frontier
- Compares performance against equal-weighted portfolio baseline

---

## Project Structure

| File | Purpose |
|------|---------|
| `main.py` | Main script to run the end-to-end pipeline — data fetch → optimization → visualization → metric output |
| `data_fetch.py` | Fetches adjusted close prices using `yfinance` and calculates daily/log returns |
| `optimizer.py` | Contains the convex optimization model using `cvxpy` to compute the optimal portfolio weights |
| `visualizer.py` | Generates pie chart of allocations and efficient frontier plot |
| `utils.py` | Computes key performance metrics (expected return, volatility, Sharpe ratio, comparison with equal-weighted portfolio) |
| `README.md` | Project documentation |


##  Objective Function: What Are We Optimizing?

This project uses the **Markowitz Modern Portfolio Theory** to balance return and risk through the following objective function:

\[
\text{Maximize: } $ \mu^T w - \lambda \cdot w^T \Sigma w $
\]

Where:

- \( $\mu \$) is the vector of expected returns for each asset
- \( $w$ \) is the vector of portfolio weights (how much to invest in each asset)
- \( $\Sigma $ \) is the covariance matrix of asset returns (i.e., risk relationships)
- \( $\lambda $ \) is the risk aversion parameter (higher = more conservative)

**Interpretation:**

- The goal is to **maximize return** ( \( \mu^T w \) ) while **minimizing portfolio risk** ( \( w^T \Sigma w \) ).
- This gives us an **optimal trade-off** between expected gain and variance (volatility).
- The risk aversion parameter \( \lambda \) controls the balance — you can tune this to favor higher returns or lower risk.

This is solved using the `cvxpy` convex optimization package under the constraints:
- Sum of weights = 1 (fully invested portfolio)
- Weights ≥ 0 (no short selling)
