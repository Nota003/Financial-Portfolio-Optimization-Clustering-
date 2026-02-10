# Financial-Portfolio-Optimization-Clustering-
Ottimizzazione di portafogli finanziari tramite Asset Clustering (K-Means) e Teoria di Markowitz. Simulazione Monte Carlo per il calcolo della Frontiera Efficiente in Python.

# Financial Portfolio Management: AI & Quantitative Analysis

[cite_start]Questo progetto esplora l'integrazione dell'**Intelligenza Artificiale** e delle **tecniche quantitative** nel settore finanziario[cite: 1]. [cite_start]L'obiettivo è migliorare l'efficienza dei servizi e ridurre i costi operativi tramite l'automazione e l'analisi avanzata[cite: 9, 10, 11, 12].

---

## 🎯 Obiettivi del Progetto

* [cite_start]**Asset Clustering**: Identificazione di gruppi omogenei di titoli basati sul profilo di rischio/rendimento[cite: 30, 38].
* [cite_start]**Asset Allocation**: Ottimizzazione del bilanciamento di portafoglio tra rischio e rendimento potenziale[cite: 134, 135].
* [cite_start]**Implementazione Pratica**: Utilizzo di algoritmi di apprendimento non supervisionato e simulazioni Monte Carlo[cite: 36, 246].

---

## 🛠 Tecnologie e Data Source

[cite_start]Il progetto utilizza lo stack tecnologico standard per la finanza quantitativa[cite: 52, 53, 54, 55]:
* **Python**: Linguaggio principale per l'analisi dei dati.
* [cite_start]**yfinance**: Per il recupero dei dati storici di mercato (2020-2023)[cite: 74].
* **Pandas & NumPy**: Per la manipolazione di Dataframe e calcoli matriciali.
* [cite_start]**Scikit-Learn**: Per l'implementazione del clustering K-Means[cite: 82].
* [cite_start]**Matplotlib**: Per la visualizzazione della Frontiera Efficiente e dei cluster[cite: 127].

---

## 📊 Analisi 1: Asset Clustering tramite K-Means

[cite_start]L'algoritmo **K-Means** divide le osservazioni in gruppi basandosi sulla distanza dal centroide (media)[cite: 36].
* [cite_start]**Dataset**: 21 azioni di diversi settori (Tech, Energy, Finance, Pharma, Consumer)[cite: 72].
* [cite_start]**Parametri**: `n_clusters = 4` con inizializzazione $k\text{-means++}$[cite: 79].
* [cite_start]**Metodologia**: Addestramento del modello tramite `fit(X)` per assegnare ogni titolo al cluster più vicino[cite: 84, 85].



---

## 📈 Analisi 2: Ottimizzazione e Frontiera Efficiente

[cite_start]Basandosi sulla **Teoria Moderna del Portafoglio** di Harry Markowitz, il rischio di un portafoglio dipende dalla correlazione tra i titoli e non solo dalla media dei rischi singoli[cite: 136, 138].

### Simulazione Monte Carlo
[cite_start]Sono stati generati **70.000 portafogli casuali** per tracciare la **Frontiera Efficiente**[cite: 247].
* [cite_start]**Sharpe Ratio**: Calcolato come rendimento atteso diviso la volatilità per misurare l'efficienza[cite: 219].
  $$Sharpe = \frac{Returns}{Volatility}$$
* [cite_start]**Risultati**: Identificazione del portafoglio a varianza minima e di quello con il massimo Sharpe Ratio[cite: 248, 251, 252].



---

## 📚 Fonti Principali
* [cite_start]**Trerotola M.**, *L'intelligenza artificiale applicata ai portafogli finanziari*[cite: 4].
* [cite_start]**Zheng et al.**, *FinBrain: when finance meets AI 2.0*[cite: 5].

---

## ⚙️ Come eseguire il progetto

1. Clona il repository:
   ```bash
   git clone [https://github.com/tuo-username/nome-repo.git](https://github.com/tuo-username/nome-repo.git)
