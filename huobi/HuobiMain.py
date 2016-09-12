#coding=utf-8

'''
本程序在 Python 3.3.0 环境下测试成功
使用方法：python HuobiMain.py
'''

from Util import *
import HuobiService

if __name__ == "__main__":
    #print ("获取账号详情") # okay
    #print (HuobiService.getAccountInfo(ACCOUNT_INFO))
    """
    {"total":"1357.22","net_asset":"1357.22","available_cny_display":"0.01","available_btc_display":"0.0000","available_ltc_display":"0.5048","frozen_cny_display":"458.20","frozen_btc_display":"0.1816","frozen_ltc_display":"5.9870","loan_cny_display":"0.00","loan_btc_display":"0.0000","loan_ltc_display":"0.0000"}
    """

    #print ("获取所有正在进行的委托")
    #print (HuobiService.getOrders(2,GET_ORDERS))
    """

    type: 1. 买入
          2. 卖出


cointype:1 btc
[{"id":2039121950,"type":2,"order_price":"4500.00","order_amount":"0.0658","processed_amount":"0.0000","order_time":1473660408},{"id":2039121134,"type":2,"order_price":"4300.00","order_amount":"0.0658","processed_amount":"0.0000","order_time":1473660401},{"id":2039119401,"type":2,"order_price":"4210.00","order_amount":"0.0500","processed_amount":"0.0000","order_time":1473660386},{"id":2037569197,"type":1,"order_price":"3900.00","order_amount":"0.0662","processed_amount":"0.0000","order_time":1473644600},{"id":2004519601,"type":1,"order_price":"1.00","order_amount":"0.0100","processed_amount":"0.0000","order_time":1473326757},{"id":2004436151,"type":1,"order_price":"1.00","order_amount":"0.0100","processed_amount":"0.0000","order_time":1473325979}]

cointype=2 ltc
[{"id":276303776,"type":2,"order_price":"100.00","order_amount":"0.2000","processed_amount":"0.0000","order_time":1473660647},{"id":273469058,"type":2,"order_price":"100.00","order_amount":"0.2000","processed_amount":"0.0000","order_time":1473326757},{"id":271741252,"type":2,"order_price":"28.00","order_amount":"4.5950","processed_amount":"0.0000","order_time":1473131020},{"id":270895435,"type":2,"order_price":"27.20","order_amount":"0.4960","processed_amount":"0.0000","order_time":1473041629},{"id":270895421,"type":2,"order_price":"27.10","order_amount":"0.4960","processed_amount":"0.0000","order_time":1473041624},{"id":270204055,"type":1,"order_price":"25.00","order_amount":"8.0000","processed_amount":"0.0000","order_time":1472970619}]

    """

    #print ("获取订单详情")
    #print (HuobiService.getOrderInfo(2,68278313,ORDER_INFO))
    print (HuobiService.getOrderInfo(1,2039121950,ORDER_INFO))
    """

    {"code":26,"msg":"该委托不存在","message":"该委托不存在"}

    {"id":2039121950,"type":2,"order_price":"4500.00","order_amount":"0.0658","processed_price":"0.00","processed_amount":"0.0000","vot":"0.00","fee":"0.00","total":"0.00","status":0}

    """

    #print ("限价买入")
    #print (HuobiService.buy(1,"1","0.01",None,None,BUY))

    #print ("限价卖出") # okay
    ## 1:btc 2:ltc
    #print (HuobiService.sell(2,"100","0.2",None,None,SELL))

#    print ("市价买入")
#    print (HuobiService.buyMarket(2,"30",None,None,BUY_MARKET))
#
#    print ("市价卖出")
#    print (HuobiService.sellMarket(2,"1.3452",None,None,SELL_MARKET))
#
#    print ("查询个人最新10条成交订单")
#    print (HuobiService.getNewDealOrders(1,NEW_DEAL_ORDERS))
#
#    print ("根据trade_id查询order_id")
#    print (HuobiService.getOrderIdByTradeId(1,274424,ORDER_ID_BY_TRADE_ID))
#
#    print ("取消订单接口")
#    print (HuobiService.cancelOrder(1,68278313,CANCEL_ORDER))
#
#
