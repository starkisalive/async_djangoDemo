from django.http import HttpResponse
from asgiref.sync import sync_to_async
import time
import asyncio


from movies.models import Movie
from stories.models import Story

#helper functions

def get_movies():
    print("preparing to get the movies... ")
    time.sleep(2)
    qs = Movie.objects.all()
    print(qs)
    print("movies fetched")

def get_stories():
    print("prepating to get the stories...")
    time.sleep(5)
    qs = Story.objects.all()
    print(qs)
    print("stories fetched")

@sync_to_async
def get_movies_async():
    print("preparing to get the movies... ")
    #await asyncio.sleep(2)
    time.sleep(2)
    qs = Movie.objects.all()
    print(qs)
    print("movies fetched")

@sync_to_async
def get_stories_async():
    print("prepating to get the stories...")
    #await asyncio.sleep(5)
    time.sleep(5)
    qs = Story.objects.all()
    print(qs)
    print("stories fetched")



def home_view(request):
    return HttpResponse("welcome to this demo")

def main_view(request):
    start_time = time.time()
    get_movies()
    get_stories()
    total = (time.time()-start_time)
    print('total : ', total)
    total2 = str(total)
    return HttpResponse('sync total time = '+total2)


async def async_main_view(request):
    start_time = time.time()
    #task1 = asyncio.ensure_future(get_movies_async())
    #task2 = asyncio.ensure_future(get_stories_async())
    #await asyncio.wait([task1, task2])
    await asyncio.gather(get_movies_async(), get_stories_async())
    total = (time.time()-start_time)
    print('total ', total)
    total2 = str(total)
    return HttpResponse('async total time : ' + total2)
