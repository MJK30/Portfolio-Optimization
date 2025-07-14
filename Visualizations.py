import matplotlib.pyplot as plt

class Visualizations:
    
    def plot_allocations(weights, tickers):
        plt.figure(figsize=(6,6))
        plt.pie(weights, labels=tickers, autopct='%1.1f%%')
        plt.title('Optimal Portfolio Allocation')
        plt.show()
        
    def plot_efficient_frontier(returns_df, num_portfolios=5000):
        import numpy as np

        mean_returns = returns_df.mean()
        cov_matrix = returns_df.cov()
        results = {'returns': [], 'volatility': [], 'sharpe': [], 'weights': []}

        for _ in range(num_portfolios):
            weights = np.random.random(len(mean_returns))
            weights /= np.sum(weights)
            port_return = np.sum(weights * mean_returns) * 252
            port_vol = np.sqrt(weights.T @ cov_matrix.values @ weights) * np.sqrt(252)
            sharpe = port_return / port_vol
            results['returns'].append(port_return)
            results['volatility'].append(port_vol)
            results['sharpe'].append(sharpe)
            results['weights'].append(weights)

        plt.figure(figsize=(10,6))
        plt.scatter(results['volatility'], results['returns'], c=results['sharpe'], cmap='viridis')
        plt.xlabel('Volatility (Risk)')
        plt.ylabel('Expected Return')
        plt.colorbar(label='Sharpe Ratio')
        plt.title('Efficient Frontier')
        plt.show()
        
    