# WeightedCorr
Weighted correlation in Python. Pandas based implementation of weighted Pearson and Spearman correlations.

I thought it was strange that I couldn't easily find a way to get both these weighted correlations with a single class/function in Python. So I made it myself.

# V2 Update 21-07-2020

Switched from a `pandas` backend to a `numpy`/`scipy` backend. Usage remains the same, but performance for Spearman correlations is significantly improved. See table below.

| N samples     |    Pearson_v1 |   Pearson_v2 |  Spearman_v1 |  Spearman_v2 | 
| ------------- | ------------- |------------- |------------- |------------- |
| 10 | 3.55 ms ± 64.1 µs  | **1.59 ms** ± 9.32 µs | 14 ms ± 131 µs | **1.78 ms** ± 7.55 µs |
| 100  | 6.69 ms ± 89 µs  | **4.94 ms** ± 79.9 µs | 21.4 ms ± 979 µs | **5.08 ms** ± 144 µs |
| 1000  | 39.1 ms ± 426 µs  | **36.7 ms** ± 529 µs | 93.7 ms ± 1.03 ms | **37.2 ms** ± 433 µs |
| 10000  | 350 ms ± 4.56 ms  | **343 ms** ± 5.41 ms | 746 ms ± 5.29 ms | **350 ms** ± 7.42 ms |
| 100000  | 3.48 s ± 11.9 ms  | **3.48 s** ± 6.44 ms | 7.44 s ± 20.1 ms | **3.52 s** ± 9.27 ms |

## Usage

This class can be used in a few different ways depending on your needs. The data should be passed to the initialization of the class. Then calling the class will produce the result with desired method (pearson is the default). Note that the method should be passed to the call, not the initialization. The examples below will result in pearson, pearson, and spearman correlations.

1. You can supply a pandas DataFrame with x, y, and w columns (columns should be in that order). The output will be a single floating point value.
```
WeightedCorr(xyw=my_data[['x', 'y', 'w']])(method='pearson')
```
2. You can supply x, y, and w pandas Series separately. The output will be a single floating point value.
```
WeightedCorr(x=my_data['x'], y=my_data['y'], w=my_data['w'])()
```
3. You can supply a pandas DataFrame, and the name of the weight column in that DataFrame. In this case the output will be an MxM pandas DataFrame (the correlation matrix) for M columns, not including the weights columns.
```
WeightedCorr(df=my_data, wcol='w')(method='pearson')
```

## Weighted Pearson correlation

The weighted Pearson r, given _n_ pairs is calculated as

<img src="https://render.githubusercontent.com/render/math?math=r_{pearson} = \frac{\sum_{i=1}^{n} (w_i(x_i - \overline{x})(y_i - \overline{y}))}  {\sqrt{\sum_{i=1}^{n}(w_i(x_i-\overline{x})^2) \sum_{i=1}^{n}(w_i(y_i-\overline{y})^2) }}" height="60">

Where

<img src="https://render.githubusercontent.com/render/math?math=\overline{x} = \frac{\sum_{i=1}^{n} (w_i*x_i)} {\sum_{i=1}^{n} w_i}" height="50">

<img src="https://render.githubusercontent.com/render/math?math=\overline{y} = \frac{\sum_{i=1}^{n} (w_i*y_i)} {\sum_{i=1}^{n} w_i}" height="50">




## Weighted Spearman rank-order correlation

First, initial ranks (_z_) are assigned to x and y. Duplicate groups of records are assigned the average rank of that group. Next the weighted rank (_rank_) is calculated for x and y separately in _n_ pairs. Such that the _j_-th _rank_ of either x or y will be:

<img src="https://render.githubusercontent.com/render/math?math=rank_j = \sum_{i=1}^n (w_i *{\bf A} (z_i, z_j)) %2B \frac{1%2B\sum_{i=1}^{n} {\bf B}(w_i, w_j)} {2} * \frac{\sum_{i=1}^{n} w_i*{\bf B}(w_i, w_j)}{\sum_{i=1}^{n} {\bf B}(w_i, w_j)}" height="60">


Where

<img src="https://render.githubusercontent.com/render/math?math={\bf A} (z_i, z_j) =\begin{cases}1 %26 \text{if } z_i %3C z_j\\0 %26\text{if } z_i \geq  z_j\end{cases}" height="60">

and

<img src="https://render.githubusercontent.com/render/math?math={\bf B} (w_i, w_j) =\begin{cases}1 %26 \text{if } w_i = w_j\\0 %26 \text{if } w_i \neq  w_j\end{cases}" height="60">

These weighted ranks are then passed to the weighted Pearson correlation function.
