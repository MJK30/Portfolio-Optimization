# 📈 Portfolio Optimization using Modern Portfolio Theory

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
