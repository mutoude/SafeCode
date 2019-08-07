import tushare as ts


def get_all_code():
    data = pro.stock_basic(list_status='L')
    totle = data.shape[1]
    print(totle)
    for index in data['ts_code'].index:
        code = data['symbol'].get(index)
        get_dalidy_data(code)
    mark = (count / totle) * 100
    final_result = '今日评级%f' % (mark)
    print(final_result)


def get_dalidy_data(code):
    print(code)
    data = ts.get_hist_data(code, start='2019-08-06', end='2019-08-06')
    if (data is not None and not data.empty):
        print(data)
        ma_20 = data['ma20'].get(0)
        cloase_price = data['close'].get(0)
        if (ma_20 > 0):
            dt_close_ma = ma_20 - cloase_price
            if (dt_close_ma > 0):
                rate = abs(dt_close_ma) / ma_20
                result = 'rate%f' % (rate)
                print(result)
                if (rate >= 0.05):
                    cc()


count = 0


def cc():
    global count
    count = count + 1
    print(count)


if __name__ == '__main__':
    ts.set_token('dbfa246168dbd76c0c5e1f833359f4cf26d88acdb20c55f6bbc9a772')
    pro = ts.pro_api()
    get_all_code()
