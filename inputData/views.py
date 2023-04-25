import sqlparse.tokens
from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.shortcuts import render
from .models import inputData
import vk_api
import time


def index(request):
    return render(request, "inputData/index.html")

def input(request):

    id = request.POST.get("id")
    photos = {}
    names = {}
    root_friends = []
    dict_friends = {}

    # work with root user
    link = f"https://api.vk.com/method/users.get?user_ids={id}&fields=photo_100&access_token={TOKEN}&v=5.131"
    try:
        root_user = requests.get(link).json()['response'][0]
    except IndexError:
        print("jkfdjkdsffffffffffffffffffffffffDJJJJJJJJJJJJJJJJJJJJJJJJJJJ")
        return render(request, "inputData/No_search.html")
    #print(root_user)
    root_id = root_user["id"]
    root_name = root_user["last_name"] + " " + root_user["first_name"]
    root_photo = root_user["photo_100"]

    photos[root_id] = root_photo
    names[root_id] = root_name
    # work with  friends root user

    link_getfriends = f"https://api.vk.com/method/friends.get?user_id={root_id}&fields=photo_100&access_token={TOKEN}&v=5.131"
    answer_getfriends = requests.get(link_getfriends).json()
    if "error" in answer_getfriends:
        answer_getfriends = {"count": 0, "items": 0}
    else:
        answer_getfriends = answer_getfriends["response"]
    count_getfriends = answer_getfriends["count"]
    items_getfriends = answer_getfriends["items"]

    for i in range(count_getfriends):
        gf_id = items_getfriends[i]["id"]
        gf_photo = items_getfriends[i]["photo_100"]
        gf_name = items_getfriends[i]["last_name"] + " " + items_getfriends[i]["first_name"]
        link_friendsMutual = f"https://api.vk.com/method/friends.getMutual?source_uid={root_id}&target_uid={gf_id}&access_token={TOKEN}&v=5.131"
        gf_list_friend = requests.get(link_friendsMutual).json()

        if "response" in gf_list_friend:
            gf_list_friend = gf_list_friend['response']
        else:
            gf_list_friend = []

        photos[gf_id] = gf_photo
        names[gf_id] = gf_name
        root_friends.append(gf_id)
        dict_friends[gf_id] = gf_list_friend


    dict_friends[root_id] = root_friends
    
    return render(request, "inputData/graph.html", context={"dict_friends": dict_friends,
                                                            "name": names,
                                                            "photos": photos,
                                                            "root_friends": root_friends,
                                                            "search_id": root_id,
                                                            "rn" : root_name
                                                            })
