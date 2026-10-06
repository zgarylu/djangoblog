from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm, ModelTodoForm
import datetime
import truststore
truststore.inject_into_ssl()
import requests
from django.utils import timezone
def index(request):
    todo_list = Todo.objects.order_by('-title')
    # if request.method == 'POST':
    #     form = TodoForm(request.POST)
    #     if form.is_valid():
    #         new_todo = Todo(text=request.POST['text'])
    #         new_todo.save()
    #         return redirect('index')
    # else:
    form = ModelTodoForm()
    mydate = datetime.datetime.now()
    data_weather = get_weather()
    context = {'todo_list': todo_list, 'form': form, 'mydate': mydate, 'myweather': data_weather}
    return render(request, 'appname/index.html', context)
# Create your views here.
@require_POST
def addTodo(request):
    form = ModelTodoForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('index')
def completeTodo(request, todo_id):
    completed_todo_item = Todo.objects.get(pk=todo_id)
    completed_todo_item.complete = True
    completed_todo_item.save()
    return redirect('index')
def deleteTodo(request, todo_id):
    deleted_todo_item = Todo.objects.get(pk=todo_id)
    deleted_todo_item.delete()
    return redirect('index')
def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')
def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('index')
def get_weather():
    #url = "https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
    url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={APIkey}"
    lat = 45.411427
    lon = -75.655447
    APIkey = '247e4512943e3078ee8c4fbe1e13d6a9'
    # r = requests.get(url.format(lat=lat, lon=lon))
    r = requests.get(url.format(lat=lat, lon=lon, APIkey=APIkey)).json()
    # data = []
    # for key, value in r.items():
    #     data.append({ 'key': key, 'value': value })
    data = {
        'city': r['name'],
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
        'humidity': r['main']['humidity'],
        'wind_speed': r['wind']['speed'],
    }
    return data
def weather(request):
    data_weather = get_weather()
    return render(request, 'appname/weather.html', {'data': data_weather})