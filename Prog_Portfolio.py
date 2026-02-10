import yfinance as yf
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#seleziono le azioni
selected = ['AAPL', 'GM', 'GE', 'TSLA', 'ALGN', 'XOM', 'SPG', 'AIG']

#scarico i dati 
raw_data = yf.download(selected, start="2020-01-01", end="2023-12-31", auto_adjust=True)

data = raw_data['Close']

returns_daily = data.pct_change()
returns_annual = returns_daily.mean() * 250
cov_daily = returns_daily.cov()
cov_annual = cov_daily * 250
port_returns = []
port_volatility = []
sharpe_ratio = []
stock_weights = []
num_assets = len(selected)
num_portfolios = 70000
np.random.seed(101)

for x in range(num_portfolios):
    weights = np.random.random(num_assets)
    #normalizzazione 
    weights /= np.sum(weights)
    #rendimento atteso
    returns = np.sum(weights * returns_annual)
    #volatilità
    volatility = np.sqrt(np.dot(weights.T, np.dot(cov_annual, weights)))
    #rendimento tenuto conto del rischio
    sharpe = returns / volatility
    sharpe_ratio.append(sharpe)
    port_returns.append(returns)
    port_volatility.append(volatility)
    stock_weights.append(weights)

portfolio = {'Returns': port_returns,
             'Volatility': port_volatility,
             'Sharpe Ratio': sharpe_ratio}

#aggiungo i pesi di ogni azione
for counter, symbol in enumerate(selected):
    portfolio[symbol+'Weight'] = [Weight[counter] for Weight in stock_weights]
#creo il DataFrame
df = pd.DataFrame(portfolio)
#column_order = ['Returns', 'Volatility', 'Sharpe Ratio'] + [stock+'Weight' for stock in selected]

#ricerca dei valori
min_volatility = df['Volatility'].min()
max_sharpe = df['Sharpe Ratio'].max()
#ricerca dei portafogli dei corrispettevi valori min e max
sharpe_portfolio = df.loc[df['Sharpe Ratio'] == max_sharpe]
min_variance_port = df.loc[df['Volatility'] == min_volatility]

print(min_variance_port.T)
print(sharpe_portfolio.T)

plt.style.use('seaborn-v0_8-dark')
df.plot.scatter(x='Volatility', y='Returns', c='Sharpe Ratio', cmap='RdYlGn', edgecolors='black', figsize=(10, 8), grid=True)
plt.scatter(x=sharpe_portfolio['Volatility'], y=sharpe_portfolio['Returns'], c='red', marker='D', s=200)
plt.scatter(x=min_variance_port['Volatility'], y=min_variance_port['Returns'], c='red', marker='D', s=200)
plt.xlabel('Volatility')
plt.ylabel('Expected Returns')
plt.title('Efficient Frontier')
plt.show()