import numpy as np
import cvxpy as cp

class PortfolioOptimizer:
    
    def optimize_portfolio(expected_return, covariance_returns, risk_aversion):
        
        n = len(expected_return)
        portfolio_weights = cp.Variable(n)
        
        MPT_Utility_objective = cp.Maximize(expected_return@portfolio_weights - risk_aversion * cp.quad_form(portfolio_weights, covariance_returns))
        constraints = [cp.sum(portfolio_weights) == 1, portfolio_weights >= 0]
        
        problem = cp.Problem(objective= MPT_Utility_objective, constraints= constraints)
        problem.solve()
        
        return portfolio_weights.value
        