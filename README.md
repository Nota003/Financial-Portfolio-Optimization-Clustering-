# Financial-Portfolio-Optimization-Clustering-
Ottimizzazione di portafogli finanziari tramite Asset Clustering (K-Means) e Teoria di Markowitz. Simulazione Monte Carlo per il calcolo della Frontiera Efficiente in Python.

# Financial Portfolio Management: AI & Quantitative Analysis

Questo progetto esplora l'integrazione dell'**Intelligenza Artificiale** e delle **tecniche quantitative** nel settore finanziario. 

---

## Obiettivi del Progetto

**Asset Clustering**: Identificazione di gruppi omogenei di titoli basati sul profilo di rischio/rendimento.
**Asset Allocation**: Ottimizzazione del bilanciamento di portafoglio tra rischio e rendimento potenziale.
**Implementazione Pratica**: Utilizzo di algoritmi di apprendimento non supervisionato e simulazioni Monte Carlo.

---

## Tecnologie e Data Source

Il progetto utilizza lo stack tecnologico standard per la finanza quantitativa:
* **Python**: Linguaggio principale per l'analisi dei dati.
* **yfinance**: Per il recupero dei dati storici di mercato (2020-2023).
* **Pandas & NumPy**: Per la manipolazione di Dataframe e calcoli matriciali.
* **Scikit-Learn**: Per l'implementazione del clustering K-Means.
* **Matplotlib**: Per la visualizzazione della Frontiera Efficiente e dei cluster.

---

## Analisi 1: Asset Clustering tramite K-Means

L'algoritmo **K-Means** divide le osservazioni in gruppi basandosi sulla distanza dal centroide (media).
* **Dataset**: 21 azioni di diversi settori (Tech, Energy, Finance, Pharma, Consumer).
* **Parametri**: `n_clusters = 4` con inizializzazione $k\text{-means++}$.
* **Metodologia**: Addestramento del modello tramite `fit(X)` per assegnare ogni titolo al cluster più vicino.



---

## Analisi 2: Ottimizzazione e Frontiera Efficiente

Basandosi sulla **Teoria Moderna del Portafoglio** di Harry Markowitz, il rischio di un portafoglio dipende dalla correlazione tra i titoli e non solo dalla media dei rischi singoli.

### Simulazione Monte Carlo
Sono stati generati **70.000 portafogli casuali** per tracciare la **Frontiera Efficiente**.
* **Sharpe Ratio**: Calcolato come rendimento atteso diviso la volatilità per misurare l'efficienza.
  $$Sharpe = \frac{Returns}{Volatility}$$
* **Risultati**: Identificazione del portafoglio a varianza minima e di quello con il massimo Sharpe Ratio.



---

## 📚 Fonti Principali
* **Trerotola M.**, *L'intelligenza artificiale applicata ai portafogli finanziari*.
* **Zheng et al.**, *FinBrain: when finance meets AI 2.0*.

---

