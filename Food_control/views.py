import datetime

from django.shortcuts import render
from django.shortcuts import redirect
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


@csrf_exempt
@login_required(login_url="login")
def index(request):
    username = request.user.get_username()
    create_form = CreateForm()
    c_food_list = None

    if len(request.POST) > 1:
        name = User.objects.get(username=username)
        food = Food.objects.get(name=request.POST.get('food', False))
        date = request.POST['date']
        User_table.objects.create(name=name, food=food, date=date)
    elif len(request.POST) == 1:
        try:
            user = User.objects.get(username=username)
            search_date = request.POST.get('search_date', False)
            c_food_list = User_table.objects.filter(name=user, date=search_date)
        except TypeError:
            pass

        try:
            import Food_control
            delete_id = request.POST.get('delete', False)
            User_table.objects.get(id=delete_id).delete()
        except Food_control.models.User_table.DoesNotExist:
            pass
    food_list = Food.objects.all()
    t_calorie = 0
    if c_food_list:

        for i in c_food_list:
            t_calorie += i.food.calorie

    context = {
        'username': username,
        'create_form': create_form,
        'food_list': food_list,
        'search_form': SearchForm(),
        'c_food_list': c_food_list,
        'total_calorie': t_calorie,
    }

    return render(request, 'index.html', context)


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            context = {
                'form': form
            }
            return render(request, 'registration/signup.html', context)
    else:
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'registration/signup.html', context)


@csrf_exempt
def signin(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            # Todo: 提示報錯
            pass
    context = {
        'form': form
    }
    return render(request, 'registration/signin.html', context)


def kkk(request):
    from write2db import write
    write()
    return redirect('/')


def sign_out(request):
    logout(request)
    return redirect('/')

@csrf_exempt
def auto_food(request):
    import random
    A = [['糙粳米平均值', 1], ['白飯', 1], ['乾麵條', 2], ['芋頭', 220], ['冰心地瓜', 220], ['馬鈴薯', 360], ['糯玉米', 340], ['白饅頭', 120]]
    B = [['豆漿', 1], ['雞蛋平均值', 1], ['傳統豆腐', 80], ['嫩豆腐', 140], ['小方豆干', 40], ['紅色吳郭魚', 35], ['白帶魚', 35], ['白對蝦平均值', 50],
         ['文蛤', 160], ['真牡蠣平均值', 65], ['里肌肉平均值', 35], ['鵝肉', 35], ['櫻桃鴨胸肉片', 35], ['沙朗牛排', 35], ['腓力牛排', 35],
         ['法式羊排', 35], ['豬小里肌', 35]]
    C = [['全脂鮮乳平均值', 1], ['全脂保久乳', 1], ['切片乾酪', 45], ['全脂凝態發酵乳', 210]]
    D = [['花椰菜', 1], ['冬瓜', 1], ['胡蘿蔔', 1], ['白蘿蔔', 1], ['桂竹筍片', 1], ['白洋蔥', 1], ['菠菜', 1], ['台灣南瓜', 1], ['牛番茄', 1]]
    E = [['北蕉平均值', 1], ['木瓜平均值', 1], ['芭樂平均值(白肉)', 1], ['芒果平均值(西洋種)', 1], ['甜瓜平均值(網紋洋香瓜)', 1], ['蓮霧平均值(粉紅色種)', 1],
         ['西洋梨平均值', 1], ['蘋果平均值(混色)', 1], ['甜橙平均值(普遍系)', 1]]
    F = ['開心果', 10], ['原味腰果', 10], ['生鮮花生仁', 10]

    ca = 2000
    A_l, B_l, C_l, D_l, E_l, F_l = {}, {}, {}, {}, {}, {}
    def get_list(a, b, c, d, e, f):

        A_c = random.choices(A, None, k=a)
        for i in A_c:
            if i[0] not in A_l:
                A_l[i[0]] = i[1]
            else:
                A_l[i[0]] += 1

        B_c = random.choices(B, None, k=b)
        for i in B_c:
            if i[0] not in B_l:
                B_l[i[0]] = i[1]
            else:
                B_l[i[0]] += 1

        C_c = random.choices(C, None, k=1)
        C_l[C_c[0][0]] = C_c[0][1] * 1.5

        D_c = random.choices(D, None, k=d)
        for i in D_c:
            if i[0] not in D_l:
                D_l[i[0]] = i[1]
            else:
                D_l[i[0]] += 1

        E_c = random.choices(E, None, k=e)
        for i in E_c:
            if i[0] not in E_l:
                E_l[i[0]] = i[1]
            else:
                E_l[i[0]] += 1

        F_c = random.choices(F, None, k=f)
        for i in F_c:
            if i[0] not in F_l:
                F_l[i[0]] = i[1]
            else:
                F_l[i[0]] += 1


    if request.POST:
        if request.POST.get('q', False) == 'low':
            get_list(3, 4, 1, 3, 2, 4)
        elif request.POST.get('q', False) == 'mid':
            get_list(3, 6, 1, 4, 3, 6)
        elif request.POST.get('q', False) == 'high':
            get_list(4, 7, 1, 5, 4, 7)



    for i in A_l.items():
        if i[1] >= 10:
            A_l[i[0]] = f'{i[1]}克/毫升'
        else:
            A_l[i[0]] = f'{i[1]}份/碗/杯'
    for i in B_l.items():
        if i[1] >= 10:
            B_l[i[0]] = f'{i[1]}克/毫升'
        else:
            B_l[i[0]] = f'{i[1]}份/碗/杯'
    for i in C_l.items():
        if i[1] >= 10:
            C_l[i[0]] = f'{i[1]}克/毫升'
        else:
            C_l[i[0]] = f'{i[1]}份/碗/杯'
    for i in D_l.items():
        if i[1] >= 10:
            D_l[i[0]] = f'{i[1]}克/毫升'
        else:
            D_l[i[0]] = f'{i[1]}份/碗/杯'
    for i in E_l.items():
        if i[1] >= 10:
            E_l[i[0]] = f'{i[1]}克/毫升'
        else:
            E_l[i[0]] = f'{i[1]}份/碗/杯'
    for i in F_l.items():
        if i[1] >= 10:
            F_l[i[0]] = f'{i[1]}克/毫升'
        else:
            F_l[i[0]] = f'{i[1]}份/碗/杯'
    context = {
        'A': A_l,
        'B': B_l,
        'C': C_l,
        'D': D_l,
        'E': E_l,
        'F': F_l,
        'username': request.user.get_username(),
    }
    if request.POST:
        return render(request, 'autofood.html', context)
    else:
        return render(request, 'autofood.html', {'username': request.user.get_username()})


def meditation(request):
    context = {
        'username': request.user.get_username()
    }
    return render(request, 'meditation.html', context)

