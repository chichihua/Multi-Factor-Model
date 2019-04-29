# Final Project: Multi-Factor Model (Regression Method)

### Objectives:
Use Multi-Factor Model to build an enhanced indexing strategy for CSI 500 Index;
Capture a relatively high active return.

### Outlines:
1. Get data of CSI 500 constituent stocks from Chinese local information server, Wind, and preprocess the data;
2. Select factors such as size (market cap), value (P/E, P/B, P/S, P/CF, EV/EBITDA), profitability (net profit margin, ROE, ROIC), growth (year-on-year revenue growth rate, year-on-year net income growth rate), trade (turnover rate);
3. Use OLS (or LASSO which might be more optimal) to define factor's sensitivity, test each factor’s effectiveness and eliminate redundant factors with multicollinearity and low r-square;
4. Build an algo to allocate active weights on different constituent stocks on the basis of the expected next month's return predicted by the regression model (give more weights on stocks with relatively higher expected return and vice versa);
5. Backtesting: test the effectiveness of the model and check the portfolio’s alpha over the benchmark.

### Division:
Jiahua Jiang: 1, 2, 4; Bo Sun: 3; Baowen Cao: 5
