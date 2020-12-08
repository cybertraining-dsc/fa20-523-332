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

**Table 1:** Resources
| **No.** | **Name** | **Version** | **Type** |     **Notes**     |
| :---  |    :----:    |    :----:    |    :----:    |  ---:  |
| 1. |  Python  | 3.6.9 | Programming language  |Python is a high-level interpreted programming language. |
| 2. |  MongoDB |  4.4.2 |  Database  | MongoDB is a NoSQL Database program that uses JSON-like documents.  | 
| 3. |  Heroku  | 0.1.4 |  Cloud Platform| Heroku is a cloud platform used for deploying applications. It uses a Git server to handle application repositories. |
| 4. |  Gunicorn  | 20.0.4  | Server Gateway Interface  | Gunicorn is a python web server gateway interface . It is mainly used in the project for running python applications on Heroku. |
| 5. |  Tensorflow  | 2.3.1 |  Python Library|  Tensorflow is an open-source machine learning library. It is mainly used in the project for training models and predicting results.|
| 6. |  Keras | 2.4.3|Python Library|Keras is an open-source python library used for interfacing with artificial neural networks. It is an interface for the Tensorflow library.
7
Scikit-Learn
0.22.2
Python Library
Scikit-learn is an open-source machine learning library featuring various algorithms for classification, regression and clustering problems.
8
Numpy
1.16.0
Python Library
Numpy is a python library used for handling and performing various operations on large multi-dimensional arrays.
9
Scipy
1.5.4
Python Library
Scipy is a python library used for scientific and technical computing. It is not directly used in the project but serves as a dependency for tensorflow.


## 3. Dataset

The project will use the historic data of Stock Market Indices - NASDAQ 100, S&P 500, Dow Jones, DAX, BEL 20, AEX, `S&P/TSX 60`, IGPA, Merval 25, SMI, IBEX 35, FTSE Italia A, CAC 40, EURO STOXX 50, FTSE 100, RTS, Shanghai Comp, NIKKEI 225, Hang Seng, S&P ASX 20 and Foreign Exhange Rates with USD of currencies - Australian Dollar, Euro, New Zealand Dollar, British Pound, Brazilian Real, Canadian Dollar, Chinese Yuan, Hong Kong Dollar, Indian Rupee, Korean Won, Mexican Peso, South African Rand, Singapore Dollar, Danish Krone, Japanese Yen, Malaysian Ringgit, Norwegian Krone, Swedish Krona, Sri Lankan Rupee, Swiss Franc, New Taiwan Dollar and Thai Baht. This data will be used to analyze its relationships with various cryptocurrencies - Bitcoin, Bitcoin Cash, Bitconnect, Dash, Ethereum, Ethereum Classic, Iota, Litecoin, Monero, Nem, Neo, Numeraire, Omisego, Qtum, Ripple, Stratis and Waves.

Cryptocurrency dataset [^4] and Foriegn Exchange Rate dataset[^5], both, available on Kaggle will be used for this project. The historic data for various stock market indices will be taken from multiple sources and are still to be decided. All the datasets will be updated daily using a web app on Heroku.

## 4. Data Storage

The project stores all of its data in NoSQL databases using MongoDB. There are total 3 databases used in the project - crypto, forex and stock. Crypto database contains 17 collections whereas forex database contains only 1 collection. The third database - stock - is yet to be built. 

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

