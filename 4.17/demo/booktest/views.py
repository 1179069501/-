import data as data
from django.db.models import Max
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from booktest.models import BookInfo
from datetime import date

class SaveDataView(View):

    def get(self,request):

        #保存数据到数据库
        #1,save
        # book = BookInfo(
        #     btitle = '西游记',
        #     bpub_date = date(1990,10,10),
        #     bread = 100,
        #     bcomment= 1000,
        #     is_delete = False
        # )
        # book.save()

        #2,create
        # BookInfo.objects.create(
        #     btitle = '武动乾坤',
        #     bpub_date = date(1990,10,11),
        #     bread = 100,
        #     bcomment = 1000,
        #     is_delete=False
        # )

        #简单查询
        #get查询一个数据
        # book = BookInfo.objects.get(id=1)
        # print(book.btitle)
        # print(book.bpub_date)

        #QuerySet
        # books = BookInfo.objects.all()
        # print(books)

        #count
        # count = BookInfo.objects.count()
        # print(count)

        #过滤查询
        # BookInfo.objects.filter(id_exact=1)
        # BookInfo.objects.filter(id_gt=1)
        # BookInfo.objects.exclude(id_gt=1)

        #删除：delete（）
        # book = BookInfo.objects.get(id=6)
        # book.delete()

        # BookInfo.objects.filter(id_gt=6).delete()

        # book = BookInfo.objects.get(id=1)
        # book.bread = 100
        # book.save()

        #update前面一点要是一个集合：filter,all .exclude,order_by
        # BookInfo.objects.filter(id=1).updata()

        #聚合函数
        value = BookInfo.objects.aggregate(Max('bcomment'))
        print(value)
        print(BookInfo.objects.all().oreder_by('-id'))

        return HttpResponse('保存数据')

