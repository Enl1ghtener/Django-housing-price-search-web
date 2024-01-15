from django.http import HttpResponse
import pandas as pd
from django.shortcuts import render,redirect
from django.http import JsonResponse
# Create your views here.

def index_view(request):
    return render(request, 'login.html')

def login_view(request):

    uname = request.GET.get('uname', '')
    pwd = request.GET.get('pwd', '')

    if uname == 'zhangsan' and pwd == '123':
        return HttpResponse('登录成功')
    return HttpResponse('登录失败')

def search_view(request):
    if request.method == 'POST':
        city_name = request.POST.get('uname', '')
        if city_name:
            return redirect('search_results', city_name=city_name)
    return render(request, 'search.html')

def search_results(request, city_name):
    df = pd.read_excel('crwal/price.xlsx')

    city_name_list = df.columns[1:].tolist()

    city_data_list = []

    for city in city_name_list:
        # 包括一个城市的全部信息
        city_dict = {'city': city, 'data': {}}

        # 完成每年的月度价格数据添加
        for i in range(0, 10):
            # 获取年份信息，df.loc[]中的i表示哪一行，每年+12
            original_date_str = df.loc[12 * i]['date']
            original_timestamp = pd.to_datetime(original_date_str)
            year_only = original_timestamp.year
            year_only_str = str(year_only)
            # 某年个月数据，df.loc[0+i:11+i],每年+12(12i)
            price_list = df.loc[0 + 12 * i:11 + 12 * i][city].tolist()

            # 将字符串类型的价格数据转换为数值类型
            price_list = pd.to_numeric(price_list, errors='coerce').tolist()
            city_dict['data'][year_only_str] = price_list

        # 将城市字典添加到city_data_list中，完成一个城市的数据添加
        city_data_list.append(city_dict)

    """
    city_data_list = [
        {
            'city': '南京',
            'data': {
                '2014': [12123, 12345, 15674, 16777, 17778, 18890,
                        19891, 19892, 19893, 19894, 19895, 19896],
                # Add more years as needed
            }
        },
        # Add more cities as needed
    ]
    """

    for city_data in city_data_list:
        if city_data['city'] == city_name:

            all_price_list=[]
            for i in range(2014,2024):
                all_price_list.append(city_data['data']['{}'.format(i)])

            return render(request, 'search_results.html',
                          {'fontdata': JsonResponse(city_data),
                           'city_name': city_name,
                           'price': all_price_list})

    return render(request, 'search_results.html', {'fontdata': None, 'city_name': None})


