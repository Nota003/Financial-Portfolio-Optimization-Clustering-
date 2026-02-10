import numpy as np
import pandas as pd
import yfinance as yf
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans 

#seleziono azioni 
stock = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA',   # Tech
           'XOM', 'CVX', 'SHEL', 'TTE',             # Energy
           'JPM', 'BAC', 'C', 'GS',                 # Finance
           'JNJ', 'PFE', 'MRK', 'ABBV',             # Pharma
           'KO', 'PEP', 'MCD', 'SBUX']              # Consumer

raw_data = yf.download(stock, start="2020-01-01", end="2023-12-31", auto_adjust=True) 
data = raw_data['Close']

returns_annual = data.pct_change().mean() * 250
volatility_annual = data.pct_change().std() * np.sqrt(250)
df_kmeans = pd.DataFrame({'Returns': returns_annual, 
                          'Volatility': volatility_annual
                          })
X = df_kmeans.values




#Categorizzo i dati
kmeans = KMeans(n_clusters=4, random_state=0)
kmeans.fit(X)
df_kmeans['Cluster'] = kmeans.labels_


print(df_kmeans.sort_values(by='Cluster'))

# grafico 
plt.style.use('seaborn-v0_8-dark')
plt.scatter(x=df_kmeans['Volatility'], 
            y=df_kmeans['Returns'], 
            c=df_kmeans['Cluster'], 
            cmap='viridis',    
            edgecolors='black', 
            alpha=0.8)
          

for i, txt in enumerate(df_kmeans.index):
    plt.annotate(txt, 
                 (df_kmeans['Volatility'].iloc[i], df_kmeans['Returns'].iloc[i]),
                 xytext=(8, 8),           # Sposta la scritta un po' a destra e in alto
                 textcoords='offset points',
                 fontsize=11, 
                 fontweight='bold')
    
plt.title('K-Means Clustering: Mappa Rischio/Rendimento', fontsize=18)
plt.xlabel('Volatilità Annuale (Rischio)', fontsize=14)
plt.ylabel('Rendimento Atteso Annuale', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()