# Market_Analysis_and_HFT_Trading_Strategy_Design
MVA_try.py ---supervised machine learning script, it will help develop the best trading strategy, multithreading enabled 

Buy_sell_mva.py-- The trading bot, runs every 30 second to capture market opportunities 

Creatlist.py -- capture market data though gdax api, Circumvent GDAX API limit automatically, handle error automatically

Trade.py --- Trade though gdax api and return the actual service fee


比特币机器学习自动交易系统
A, 机器学习
1.历史数据抓取
2.建立模型以及理论基础
3.基于ARM处理器的机器学习node
4.模型调试与可视化数据分析
5. 模型验证

B,自动交易
1.行情数据抓取
2.基于机器学习的自动交易策略运行, ARM 架构低功耗单片机
3.错误处理
4.交易状态可视化

######################################################

比特币交易市场24/7 不间断交易，另外几乎所有的交易市场都免费开放了行情API和交易API， 这就极大方便了自动交易系统的开发.

1.历史数据抓取

利用Python 的Gdax 开源工具包， 我做了一个python的module， 输入指定日期后，可以通过gadx api 抓取从指定日期时间段内所有秒级市场数据， 包括time，low，high，open，close，volume. 这个抓取过程全程自动，遇上断网，数据源缺失等情况，程序也能自动处理。



Unfortunely, I can not upload my trading algorithm at this time. 
Feel free to contact me at jaysun1990@gmail.com
