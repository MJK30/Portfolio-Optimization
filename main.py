from GetPriceData import GetPriceData
from PortfolioOptimizer import PortfolioOptimizer
from Visualizations import Visualizations
import numpy as np


def main():
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]
    start_date = "2020-01-01"
    end_date = "2025-01-01"
    return_calc_method ="simple"  # simple / log 
    risk_aversion = 1
    
    # Get the data and the returns per day
    prices = GetPriceData.get_PriceData(tickers, start_date, end_date)
    returns = GetPriceData.get_returns(prices, return_calc_method)
    
    # Calculate the annual expected returns and the covariance of the Adjusted Returns
    expected_returns = returns.mean() * 252  # 252 Trading days per year. Annual Return per asset calculated
    covariance_returns = returns.cov() * 252  # # 252 Trading days per year. Annual Return per asset calculated
    
    # Compute the Optimal Portfolio weights according to the Modern Portfolio Theory
    opt_portfolio_weights = PortfolioOptimizer.optimize_portfolio(expected_returns.values, covariance_returns.values, risk_aversion)
    
    weights = np.clip(opt_portfolio_weights, 0, 1)
    
    # Output
    print("Optimal Portfolio Weights:")
    for t, w in zip(tickers, weights):
        if abs(w) > 1e-4:  # only print weights > 0.01%
            print(f"{t}: {w:.4%}")
            
    # Expected Returns from the portfolio
    expected_portfolio_return = np.dot(opt_portfolio_weights, expected_returns)
    print(f"Expected Annual Return: {expected_portfolio_return:.2%}")
    
    # Portfolio Volatility/Risk
    portfolio_volatility = np.sqrt(opt_portfolio_weights @ covariance_returns @ opt_portfolio_weights)
    print(f"Portfolio Volatility: {portfolio_volatility:.2%}")
    
    # Sharpe Ratio
    sharpe_ratio = expected_portfolio_return / portfolio_volatility
    print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
    
    
    # Effectiveness of the Optimized Portfolio
    n = len(expected_returns)
    equal_weights = np.array([1/n] * n) # if equally invested in each of the portfolio
    
    # expected returns, volatility, sharpe ratio for equal ratio investment
    equal_return = np.dot(equal_weights, expected_returns)
    equal_volatility = np.sqrt(equal_weights @ covariance_returns @ equal_weights)
    equal_sharpe = equal_return / equal_volatility
    
    # Comparison
    print(f"Improvement in Expected Return: {(expected_portfolio_return - equal_return):.2%}")
    print(f"Reduction in Volatility: {(equal_volatility - portfolio_volatility):.2%}")
    print(f"Sharpe Ratio Improvement: {(sharpe_ratio - equal_sharpe):.2f}")
    
    # Visualizations
    Visualizations.plot_allocations(opt_portfolio_weights, tickers)
    Visualizations.plot_efficient_frontier(returns)
    
    print("STOP")



if __name__ == "__main__":
    main()