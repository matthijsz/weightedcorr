# WeightedCorr
Weighted correlation in Python. Pandas based implementation of weighted Pearson and Spearman correlations.

I thought it was strange that I couldn't easily find a way to get both these weighted correlations with a single class/function in Python. So I made it myself.

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

The weighted Pearson r is calculated as

<img src="https://render.githubusercontent.com/render/math?math=\overline{x} = \frac{\sum_{i=1}^{n} (w_i*x_i)} {\sum_{i=1}^{n} w_i}" height="50">

<img src="https://render.githubusercontent.com/render/math?math=\overline{y} = \frac{\sum_{i=1}^{n} (w_i*y_i)} {\sum_{i=1}^{n} y_i}" height="50">

<img src="https://render.githubusercontent.com/render/math?math=r_{pearson} = \frac{\sum_{i=1}^{n} (w_i(x_i - \overline{x})(y_i - \overline{y}))}  {\sqrt{\sum_{i=1}^{n}(w_i(x_i-\overline{x})^2) \sum_{i=1}^{n}(w_i(y_i-\overline{y})^2) }}" height="60">

Where n is the number of pairs in the data.





<img src="https://render.githubusercontent.com/render/math?math=">

