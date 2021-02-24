from django.http import HttpResponse

from asgiref.sync import sync_to_async

import time
import asyncio
import requests

from aiohttp import ClientSession
import pathlib

from movies.models import Movie
from stories.models import Story


#helper functions for movies and stories
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


async def get_movies_async():
    print("preparing to get the movies... ")
    await asyncio.sleep(2)
    #time.sleep(2)
    qs = sync_to_async(Movie.objects.all())
    print(qs)
    print("movies fetched")


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

##helper functions for webscraping
async def fetch(url, session, year):
    async with session.get(url) as response:
        html_body = await response.read()
        print("fetched year", year)
        return {"body": html_body, "year": year}

async def fetch_helper(start_year=2020, years_ago=5):
    html_body = ""
    tasks = []
    async with ClientSession() as session:
        for i in range(0, years_ago):
            year = start_year - i
            url = f'https://www.boxofficemojo.com/year/{year}/'
            print("year", year, url)
            tasks.append(
                asyncio.create_task(
                    fetch(url, session, year)
                )
            )

        pages_content = await asyncio.gather(*tasks)


def fetch_sync(url,year):
    html = requests.get(url).content
    return (html)


def fetch_helper_sync(start_year=2020, years_ago=5):
    html_body = ""
    tasks = []
    for i in range(0,years_ago):
            year = start_year - i
            url= ('https://www.boxofficemojo.com/year/{}/'.format(year))
            print('scraping year', year, url)
            result = fetch_sync(url,year)
            #task1 = asyncio.create_task(fetch_sync(url, year))
            #tasks.append(task1)
            #pages_content = await asyncio.gather(*tasks)
            print("fetched year", year)



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

def scrape_view_async(request):
    start_time = time.time()
    results = asyncio.run(fetch_helper())
    total = (time.time()-start_time)
    print('total ', total)
    total2 = str(total)
    return HttpResponse('async webscraping total time : ' + total2)

def scrape_view_sync(request):
    start_time = time.time()

    results = fetch_helper_sync()
    total = (time.time()-start_time)
    print('total ', total)
    total2 = str(total)
    return HttpResponse('sync webscraping total time : ' + total2)
