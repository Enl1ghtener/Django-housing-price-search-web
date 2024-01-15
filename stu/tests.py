import pandas as pd

df=pd.read_excel('D:/作业/毕业实习/4.爬虫/price.xlsx')


city_name_list = []
for i in range(1,len(df.columns)):
    city_name_list.append(df.columns.values[i])

city_data_list=[]

for city in city_name_list:
    # 包括一个城市的全部信息
    city_list_dic = dict()
    price_list = []

    #完成第二层字典中城市的添加
    city_list_dic.update({'city': city})
    #完成第二次字典中所有年份的月度价格数据添加
    for i in range(0, 10):
        # 获取年份信息，df.loc[]中的i表示哪一行，每年+12
        original_date_str = df.loc[12*i]['date']
        original_timestamp = pd.to_datetime(original_date_str)
        year_only = original_timestamp.year
        year_only_str = str(year_only)
        # 某年个月数据，df.loc[0+i:11+i],每年+12(12i)
        price_list = df.loc[0+12*i:11+12*i]['{}'.format(city)]
        city_list_dic.update({'{}'.format(year_only_str):price_list})
    #即,数据保存在city_list_dic字典中
    #将字典添加到city_data_list中,完成一个城市的数据添加
    city_data_list.append(city_list_dic)


"""
city_data_list = [
        {
            'city': '南京',
            '2014': [
            12123,12345,15674,
            16777,17778,18890,
            19891,19892,19893,
            19894,19895,19896
            ],
            #Add more monthly price as needed  
        },
# Add more cities as needed
]
"""