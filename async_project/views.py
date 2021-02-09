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
    print("preparing to get the stories...")
    time.sleep(5)
    qs = Story.objects.all()
    print(qs)
    print("stories fetched")

#async_function1 = sync_to_async(get_movies(),thread_sensitive=False)
#async_function2 = sync_to_async(get_stories(),thread_sensitive=False)

#@sync_to_async
async def get_movies_async():
    print("preparing to get the movies... ")
    await asyncio.sleep(2)
    #time.sleep(2)
    qs = sync_to_async(Movie.objects.all())
    print(qs)
    print("movies fetched")

#@sync_to_async
async def get_stories_async():
    print("prepating to get the stories...")
    await asyncio.sleep(5)
    #time.sleep(5)
    qs = sync_to_async(Story.objects.all())
    print(qs)
    print("stories fetched")

async def async_tasker_function():
    task1 = asyncio.create_task(get_movies_async())
    task2 = asyncio.create_task(get_stories_async())
    tasks = [task1,task2]
    result = await asyncio.gather(*tasks)
    #print(result)




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


def main_view_async(request):
    start_time = time.time()
    #async_function1()
    #async_function2()
    asyncio.run(async_tasker_function())

    #await get_movies_async()
    #await get_stories_async()

    #task1 = asyncio.ensure_future(get_movies_async())
    #task2 = asyncio.ensure_future(get_stories_async())
    #await asyncio.wait([task1, task2])
    #await asyncio.gather(get_movies_async(), get_stories_async())
    total = (time.time()-start_time)
    print('total ', total)
    total2 = str(total)
    return HttpResponse('async total time : ' + total2)
