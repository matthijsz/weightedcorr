# WeightedCorr
Weighted correlation in Python. Pandas based implementation of weighted Pearson and Spearman correlations.

I thought it was strange that I couldn't easily find a way to get both these weighted correlations with a single class/function in Python. So I made it myself.

## Weighted Pearson correlation

The weighted Pearson r is calculated as

<img src="https://render.githubusercontent.com/render/math?math=r_{pearson} = \frac{\sum_{i=1}^{n} (w_i(x_i - \overline{x})(y_i - \overline{y}))}  {\sqrt{\sum_{i=1}^{n}(w_i(x_i-\overline{x})^2) \sum_{i=1}^{n}(w_i(y_i-\overline{y})^2) }}" height="60">

Where

<img src="https://render.githubusercontent.com/render/math?math=\overline{x} = \frac{\sum_{i=1}^{n} (w_i*x_i)} {\sum_{i=1}^{n} w_i}" height="60">

and

<img src="https://render.githubusercontent.com/render/math?math=\overline{y} = \frac{\sum_{i=1}^{n} (w_i*y_i)} {\sum_{i=1}^{n} y_i}" height="60">



<img src="https://render.githubusercontent.com/render/math?math=">

