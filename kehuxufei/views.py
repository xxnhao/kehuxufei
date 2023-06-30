from django.shortcuts import render
from django.http import HttpResponse
from kehuxufei.models import khxx


# Create your views here.
def index(request):
    e = kh_db_xinzeng('品优1','http://8.141.82.239:8899/',"1",'gyljcgtdcpb@acewill.cn')
    return HttpResponse(e)

# 新增客户方法
def kh_db_xinzeng(name,url,username,password):

    # 判断客户是否存在，如果存在不可以添加
    if len(khxx.objects.filter(kh_name=name)) <= 0:
        db = khxx()
        db.kh_name = name  # '品优'
        db.kh_url = url  # 'http://8.141.82.239:8899/'
        db.kh_username = username  # '1'
        db.kh_password = password  # 'gyljcgtdcpb@acewill.cn'
        db.save()
        return "数据添加成功"
    else:
        return "客户已经存在，添加失败"

#修改客户方法
def kh_db_xiugai(name):
    db = khxx.objects.filter(kh_name=name)