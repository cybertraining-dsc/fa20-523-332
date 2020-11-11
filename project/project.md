# Analyzing the Relationship of Cryptocurrencies with Foriegn Exchange Rates and Global Stock Market Indices

[![Check Report](https://github.com/cybertraining-dsc/fa20-523-332/workflows/Check%20Report/badge.svg)](https://github.com/cybertraining-dsc/fa20-523-332/actions)

Krish Hemant Mhatre

[fa20-523-332](https://github.com/cybertraining-dsc/fa20-523-332/), [Edit](https://github.com/cybertraining-dsc/fa20-523-332/blob/master/project/project.md)

<krishmhatre@icloud.com>

{{% pageinfo %}}

## Abstract

The project involves analyzing the relationships of various cryptocurrencies with Foreign Exchange Rates and Stock Market Indices. Apart from analyzing the relationships, the objective of the project is also to estimate the trend of the cryptocurrencies based on Foreign Exchange Rates and Stock Market Indices. We will be using historic data of 17 different cryptocurrencies, 21 Stock Market Indices and 22 Foreign Exchange Rates for this project. The project will use various Machine Learning models for analysis and prediction. The project might also use Neural Networks for prediction and estimation. 

Contents

{{< table_of_contents >}}

{{% /pageinfo %}}

**Keywords:** cryptocurrency, stocks, foreign exchange rates

## 1. Introduction

One of the latest global medium of exchange is Cryptocurrency. The total market capitalizations of all cryptocurrencies added up to $237.1 Billion as of 2019[^1]. Cryptocurrency systems do not require a central authority, its state is maintained through distributed consensus[^2]. Therefore, determine the factors affecting the prices of cryptocurrencies becomes difficult. There are many factors affecting cryptocurrency like transaction cost, reward system, hash rate, coins circulation, forks, popularity of cryptomarket, speculations, stock markets, exchange rates, gold price, interest rate, legalization and restriction[^3]. This project involves analysis of relationships of various cryptocurrencies with Foreign Exchange Rates and Stock Market Indices.

## 2. Background

TBD

## 3. Dataset

The project will use the historic data of Stock Market Indices - NASDAQ 100, S&P 500, Dow Jones, DAX, BEL 20, AEX, S&P/TSX 60, IGPA, Merval 25, SMI, IBEX 35, FTSE Italia A, CAC 40, EURO STOXX 50, FTSE 100, RTS, Shanghai Comp, NIKKEI 225, Hang Seng, S&P ASX 20 and Foreign Exhange Rates with USD of currencies - Australian Dollar, Euro, New Zealand Dollar, British Pound, Brazilian Real, Canadian Dollar, Chinese Yuan, Hong Kong Dollar, Indian Rupee, Korean Won, Mexican Peso, South African Rand, Singapore Dollar, Danish Krone, Japanese Yen, Malaysian Ringgit, Norwegian Krone, Swedish Krona, Sri Lankan Rupee, Swiss Franc, New Taiwan Dollar and Thai Baht. This data will be used to analyze its relationships with various cryptocurrencies - Bitcoin, Bitcoin Cash, Bitconnect, Dash, Ethereum, Ethereum Classic, Iota, Litecoin, Monero, Nem, Neo, Numeraire, Omisego, Qtum, Ripple, Stratis and Waves.

Cryptocurrency dataset [^4] and Foriegn Exchange Rate dataset[^5], both, available on Kaggle will be used for this project. The historic data for various stock market indices will be taken from multiple sources and are still to be decided. All the datasets will be updated daily using a web app on Heroku.

## 4. Data Storage

The project stores all of its data in NoSQL databases using MongoDB. There are total 3 databases used in the project - crypto, forex and stock. Crypto database contains 17 collections whereas forex database contains only 1 collection. The third database - stock - is yet to be built. 

## 5. Methodology

The project uses all of its historic data to train a machine learning model for each cryptocurrency. In order to predict/estimate, all the models will use the opening rates of the selected cryptocurrency and related stock indices and foreign exchange. The models will be able to predict the closing rate for that day for the respective cryptocurrency.

To be updated with details.

## 6. Conclusion

TBD

## Plan
Nov 3 - Nov 7: Building final dataset and development of web-app to update the database daily.
Nov 8 - Nov 15: Development of Machine Learning Models.

## References

[^1]: Szmigiera, M. "Cryptocurrency Market Value 2013-2019." Statista, 20 Jan. 2020, <https://www.statista.com/statistics/730876/cryptocurrency-maket-value/>. 

[^2]: Lansky, Jan. "Possible State Approaches to Cryptocurrencies." Journal of Systems Integration, University of Finance and Administration in Prague Czech Republic, <http://www.si-journal.org/index.php/JSI/article/view/335>. 

[^3]: Sovbetov, Yhlas. "Factors Influencing Cryptocurrency Prices: Evidence from Bitcoin, Ethereum, Dash, Litcoin, and Monero. " Journal of Economics and Financial Analysis, London School of Commerce, 26 Feb. 2018, <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3125347>. 

[^4]: "Cryptocurrency Historical Prices." Kaggle, 21 Feb. 2018, <https://www.kaggle.com/sudalairajkumar/cryptocurrencypricehistory?select=bitconnect_price.csv>. 

[^5]: "Foreign Exchange Rates 2000-2019." Kaggle, 3 Mar. 2020, <https://www.kaggle.com/brunotly/foreign-exchange-rates-per-dollar-20002019>. 

