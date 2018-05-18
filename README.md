# HODLgather
This is a short script to simulate your strategy in a smooth growing market.
Gather the amount of bitcoins you like in the long term for HODL.


## Install
```console
git clone https://github.com/HODLinc/HODLgather.git
cd HODLgather
```


## Configure and run
1.  Switch to the ``config`` folder.
2.  Copy the ``config.py.example`` file and rename the copy to ``config.py``
3.  Change the values according to your strategy:
    * Define the months of investment.
    * Define your current holdings and related fiat investment in EUR.
    * Define your assumptions and strategy by varying in daily expected growth and your monthly investment (By the way, McAffee's bet of $1 Mio. at the end of 2020 means around 0.5 % daily growth - not too far from reality!?).
    * Let's start at the current price (add it manually, however this will be soon an online feature aswell).
4.  Run the programm from the main directory via ``python hodlgather.py``

## Watch the outcome
* You get an detail analysis of the investment development for each month including prospected price, your total investment, gathered BTC with it's that-date value and a percentage gain related to your investment.
* There will be a ``matplotlib`` plot to show you what effects future investments will have to your BTC holding. Please don't be disappointed, you know markets are mostly exponentially related growth.


## ToDo
* [ ] Use current online price and only fall back to manual start price when offline.
* [ ] Your idea! Submit and issue or even fork this script and program it yourself and make a pull request.
