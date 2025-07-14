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

This project uses **Modern Portfolio Theory** to construct a portfolio that balances expected return and risk. The core objective function is:

$$
\text{Maximize: } \mu^T w - \lambda \cdot w^T \Sigma w
$$

Where:

- $\mu$ = vector of expected annual returns for each asset  
- $w$ = vector of portfolio weights (how much capital is allocated to each asset)  
- $\sigma$ = covariance matrix of asset returns (i.e., risk relationship between assets)  
- $\lambda$ = risk aversion parameter (higher values penalize risk more heavily)

###  Interpretation:

- The first term $\mu^Tw$ represents **expected return** of the portfolio.
- The second term $w^T\sigma w$ represents **portfolio variance** (i.e., risk).
- By adjusting $\lambda$, the model finds the best trade-off between maximizing return and minimizing risk.

The optimization is solved using `cvxpy` with these constraints:

- $$\sum w_i=1$$ (100% of capital is allocated)
- $$w_i\geq 0$$ (no short selling allowed)
