# Analyzing the Relationship of Cryptocurrencies with Foriegn Exchange Rates and Global Stock Market Indices

[![Check Report](https://github.com/cybertraining-dsc/fa20-523-332/workflows/Check%20Report/badge.svg)](https://github.com/cybertraining-dsc/fa20-523-332/actions)
[![Status](https://github.com/cybertraining-dsc/fa20-523-332/workflows/Status/badge.svg)](https://github.com/cybertraining-dsc/fa20-523-332/actions)
Status: in progress, Type: Project

* Krish Hemant Mhatre

* [fa20-523-332](https://github.com/cybertraining-dsc/fa20-523-332/)
* [Edit](https://github.com/cybertraining-dsc/fa20-523-332/blob/main/project/project.md)
* <krishmhatre@icloud.com>

{{% pageinfo %}}

## Abstract

The project involves analyzing the relationships of various cryptocurrencies with Foreign Exchange Rates and Stock Market Indices. Apart from analyzing the relationships, the objective of the project is also to estimate the trend of the cryptocurrencies based on Foreign Exchange Rates and Stock Market Indices. We will be using historical data of 6 different cryptocurrencies, 25 Stock Market Indices and 22 Foreign Exchange Rates for this project. The project will use various machine learning tools for analysis. The project also uses a fully connected deep neural network for prediction and estimation. Apart from analysis and prediction of prices of cryptocurrencies, the project also involves building its own database and giving access to the database using a prototype API. The historical data and recent predictions can be accessed through the public API. 

Contents
{{< table_of_contents >}}
{{% /pageinfo %}}

Keywords: cryptocurrency, stocks, foreign exchange rates


## 1. Introduction

The latest type of investment in the finance world and one of the latest global medium of exchange is Cryptocurrency. The total market capitalizations of all cryptocurrencies added up to $237.1 Billion as of 2019[^1], making it one of the fastest growing industries in the world. Cryptocurrency systems do not require a central authority as its state is maintained through distributed consensus[^2]. Therefore, determining the factors affecting the prices of cryptocurrencies becomes extremely difficult. There are several factors affecting the prices of cryptocurrency like transaction cost, reward system, hash rate, coins circulation, forks, popularity of cryptomarket, speculations, stock markets, exchange rates, gold price, interest rate, legalization and restriction[^3]. This project involves studying and analysing the relationships of various cryptocurrencies with Foreign Exchange Rates and Stock Market Indices. Furthermore, the project also involves predicting the cryptocurrency price based on stock market indices and foreign exchange rates of the previous day. The project also involves development of a public API to access the database of the historical data and the predictions. 


## 2. Resources

**Table 2.1:** Resources
| **No.** | **Name** | **Version** | **Type** |     **Notes**     |
| :---  |    :----:    |    :----:    |    :----:    |  ---:  |
| 1. |  Python  | 3.6.9 | Programming language  |Python is a high-level interpreted programming language. |
| 2. |  MongoDB |  4.4.2 |  Database  | MongoDB is a NoSQL Database program that uses JSON-like documents.  | 
| 3. |  Heroku  | 0.1.4 |  Cloud Platform| Heroku is a cloud platform used for deploying applications. It uses a Git server to handle application repositories. |
| 4. |  Gunicorn  | 20.0.4  | Server Gateway Interface  | Gunicorn is a python web server gateway interface . It is mainly used in the project for running python applications on Heroku. |
| 5. |  Tensorflow  | 2.3.1 |  Python Library|  Tensorflow is an open-source machine learning library. It is mainly used in the project for training models and predicting results.|
| 6. |  Keras | 2.4.3|Python Library|Keras is an open-source python library used for interfacing with artificial neural networks. It is an interface for the Tensorflow library. |
| 7. | Scikit-Learn|0.22.2|Python Library|Scikit-learn is an open-source machine learning library featuring various algorithms for classification, regression and clustering problems.|
| 8. |Numpy|1.16.0|Python Library|Numpy is a python library used for handling and performing various operations on large multi-dimensional arrays.|
| 9. |Scipy|1.5.4|Python Library|Scipy is a python library used for scientific and technical computing. It is not directly used in the project but serves as a dependency for tensorflow.|
| 10.|Pandas|1.1.4|Python Library|Pandas is a python library used mainly for large scale data manipulation and analysis. |
|11.|Matplotlib|3.2.2|Python Library|Matplotlib is a python library used for graphing and plotting. |
|12.|Pickle|1.0.2|Python Library|Pickle-mixin is a python library used for saving and loading python variables.|
|13.|Pymongo|3.11.2|Python Library|Pymongo is a python library containing tools for working with MongoDB.|
|14.|Flask|1.1.2|Python Library|Flask is a micro web framework for python. It is used in the project for creating the API.|
|15.|Datetime|4.3|Python Library|Datetime is a python library used for handling dates as date objects.|
|16.|Pytz|2020.4|Python Library|Pytz is a python library used for accurate timezone calculations.|
|17|Yahoo Financials|1.6|Python Library|Yahoo Financials is an unofficial python library used for extracting data from Yahoo Finance website by web scraping.|
|18|Dns Python|2.0.0|Python Library|DNS python is a necessary dependency of Pymongo.|



## 3. Dataset

The project builds its own dataset by extracting the data from Yahoo Finance website using Yahoo Financial python library [^4]. The data includes cryptocurrency prices, stock market indices and foreign exchange rates from September 30 2015 to December 5 2020. The project uses historical data of 6 cryptocurrencies - Bitcoin (BTC), Ethereum (ETH), Dash (DASH), Litecoin (LTC), Monero (XMR) and Ripple (XRP), 25 stock market indices - S&P 500 (USA), Dow 30 (USA), NASDAQ (USA), Russell 2000 (USA), S&P/TSX (Canada), IBOVESPA (Brazil), IPC MEXICO (Mexico), Nikkei 225 (Japan), HANG SENG INDEX (Hong Kong), SSE (China), Shenzhen Component (China), TSEC (Taiwan), KOSPI (South Korea), STI (Singapore), Jakarta Composite Index (Indonesia), FTSE Bursa Malaysia KLCI (Malaysia), S&P/ASX 200 (Australia), S&P/NZX 50 (New Zealand), S&P BSE (India), FTSE 100 (UK), DAX (Germany), CAC 40 (France), ESTX 50 (Europe), EURONEXT 100 (Europe), BEL 20 (Belgium), and 22 foreign exchange rates - Australian Dollar, Euro, New Zealand Dollar, British Pound, Brazilian Real, Canadian Dollar, Chinese Yuan, Hong Kong Dollar, Indian Rupee, Korean Won, Mexican Peso, South African Rand, Singapore Dollar, Danish Krone, Japanese Yen, Malaysian Ringgit, Norwegian Krone, Swedish Krona, Sri Lankan Rupee, Swiss Franc, New Taiwan Dollar, Thai Baht. This data is, then, posted to MongoDB Database. The three databases are created for each of the data types - Cryptocurrency prices, Stock Market Indices and Foreign Exchange Rates. The three databases each contain one collection for every currency, index and rate respectively. These collections have a uniform structure containing 6 columns - “id”, “formatted_date”, “low”, “high”, “open” and “close”. The tickers used to extract data from Yahoo Finance [^4] are stated in Figure .

**Figure 3.1:** Ticker Information 

The data is, then, preprocessed to get only one column per date (“close” price) and to add missing information by replicating previous day’s values, which is used to make a large dataset including the prices of all indices and rates for all the dates within the given range. This data is saved in a different MongoDB Database and collection, both, called nn_data. This collection has 54 columns containing closing prices for each cryptocurrency price, stock market index and foreign exchange rate and the date. The rows represent different dates. 

One additional database is also created - Predictions - which contain the predictions of cryptocurrency prices for each day and it’s true value. The collection has 13 columns containing a date column and 2 columns for each cryptocurrency (prediction value and true value). New rows are inserted everyday for all collections except the “nn_data” collection. Figure ## represents the overview of the MongoDB Cluster. Figure ## shows the structure of the nn_data collection.

**Figure 3.2:** MongoDB Cluster Overview

**Figure 3.3:** Short Structure of NN_data Collection

## 4. Analysis

### 4.1 Principal Component Analysis
Principal Component Analysis uses Singular Value Decomposition (SVD) for dimensionality reduction, exploratory data analysis and making predictive models. PCA helps understand a linear relationship in the data [^5]. In this project, PCA is used for the preliminary analysis to find a pattern between the target and the features. Here we have tried to make some observations by performing PCA on various cryptocurrencies with stocks and forex data. In this analysis, we reduced the dimension of the dataset to 3D, represented in Figure ##. The first and second dimension is on x-axis and y-axis respectively whereas the third dimension is used in the color. On observing the scatter plots in Figure ##, we can clearly see the patterns formed by various relationships. Therefore, it can be stated that the target and features are related in some way based on the principal component analysis. 

**Figure 4.1:** Principal Component Analysis

### 4.2 TSNE Analysis
T-Distributed Stochastic Neighbour Embedding is mainly used for non-linear dimensionality reduction. TSNE uses local relationships between points to create a low-dimensional mapping. TSNE uses Gaussian distribution to  create a probability distribution. In this project, TSNE is used to analyze non-linear relationships between cryptocurrencies and the features (stock indices and forex rates), which were not visible in the principal component analysis. It can be observed in Figure ##, that there are visible patterns in the data i.e. same colored data points are in some pattern, proving a non linear relationship. The t-SNE plots in Figure ## are not like the typical t-SNE plots i.e. they do not have any clusters. This might be because of the size of the dataset. 

**Figure 4.2:** t-SNE Analysis

### 4.3 Weighted Features Analysis
Layers of neural networks have weights assigned to each feature column. These weights are updated continuously while training. Analyzing the weights of the model which is trained for this project, can give us a picture of the important features. To perform such an analysis, the top five feature weights are noted for each layer. The number of times a feature is present in the top five of a layer, is also noted. This is represented in Figure ##, where we can observe that the New Zealand Dollar and the Canadian Dollar are repeated most number of times in the top five weights of layers. 

**Figure 4.3:** No. of repetitions in top five weights

## 5. Methodology

The project uses all of its historic data to train a machine learning model for each cryptocurrency. In order to predict and estimate, all the models will use the opening rates of the selected cryptocurrency and related stock indices and foreign exchange. The models will be able to predict the closing rate for that day for the respective cryptocurrency.

To be updated with details.

## 6. Conclusion

TBD

## Plan

Nov 3 - Nov 7: Building final dataset and development of web-app to update the database daily.

Nov 8 - Nov 15: Development of Machine Learning Models.

## References

[^1]: Szmigiera, M. "Cryptocurrency Market Value 2013-2019." Statista, 20 Jan. 2020, <https://www.statista.com/statistics/730876/cryptocurrency-maket-value>. 

[^2]: Lansky, Jan. "Possible State Approaches to Cryptocurrencies." Journal of Systems Integration, University of Finance and Administration in Prague Czech Republic, <http://www.si-journal.org/index.php/JSI/article/view/335>. 

[^3]: Sovbetov, Yhlas. "Factors Influencing Cryptocurrency Prices: Evidence from Bitcoin, Ethereum, Dash, Litcoin, and Monero." Journal of Economics and Financial Analysis, London School of Commerce, 26 Feb. 2018, <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3125347>. 

[^4]: "Cryptocurrency Historical Prices." Kaggle, 21 Feb. 2018, <https://www.kaggle.com/sudalairajkumar/cryptocurrencypricehistory?select=bitconnect_price.csv>. 

[^5]: "Foreign Exchange Rates 2000-2019." Kaggle, 3 Mar. 2020, <https://www.kaggle.com/brunotly/foreign-exchange-rates-per-dollar-20002019>. 

