#定义一个中间件用到的闭包
def my_decorator(func):

    print('init')

    def wrapper(request):

        print('视图函数执行之前,调用的区域')

        response = func(request)
        print('视图函数调用之后,调用的函数')
        return response

    return wrapper

def my_decorator1(func):

    print('init2')

    def wrapper(request):

        print('视图函数执行之前,调用的区域2')

        response = func(request)
        print('视图函数调用之后,调用的函数2')
        return response

    return wrapper