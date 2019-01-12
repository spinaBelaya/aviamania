from django.shortcuts import render
import json
import sys
import string 
import os


def open_file(name):
    file = r"\aviasearch\{0}.json".format(name)
    path = os.getcwd() + file
    with open(path, "r", encoding='utf-8') as fh:
        data = json.load(fh)
    return data


def write_in_file(name, data):
    file = r"\aviasearch\{0}.json".format(name)
    path = os.getcwd() + file
    with open(path, "w", encoding='utf-8') as fh:
        fh.write(data)
    pass


def aviacompany_list(request):
    aviacompanies = open_file("Aviacompanies")
    return render(request, 'aviasearch/aviacompany_list.html', {'aviacompanies': aviacompanies})


def get_aviacompany(request):
    i = 0
    all_aviacompanies = open_file("Aviacompanies")
    for aviacompany in all_aviacompanies:
        if aviacompany["company_name"] == request.POST.get("search_by_name"):
            i = 1
            return render(request, 'aviasearch/searched_aviacompany_list.html', {'aviacompany': aviacompany})
    if i == 0:
        return render(request, 'aviasearch/aviacompany_list.html', {'aviacompanies': all_aviacompanies, 'message': 'Вы ищете несуществующую авакомпанию'})


def admin_panel(request):
    data = {
        "login": "admin",
        "password": "1234"
    }
    if request.POST:
        if data['login'] == request.POST.get('login') and data['password'] == request.POST.get('password'):
            return render(request, 'aviasearch/admin.html', {})
        else:
            aviacompanies = open_file("Aviacompanies")
            return render(request, 'aviasearch/if_error.html', {'aviacompanies': aviacompanies})



def add_company(request):
    all_aviacompanies = open_file("Aviacompanies")
    new_company = {
        "id": request.POST.get("id"),
        "company_name": request.POST.get("company_name"),
        "country": request.POST.get("country"),
        "director": request.POST.get("director"),
        "date": request.POST.get("date"),
        "description": request.POST.get("description"),
        "plains": [
            {
                "id_plain": request.POST.get("id_plain"),
                "plain_name": request.POST.get("plain_name"),
                "length": request.POST.get("length"),
                "numof_seats": request.POST.get("numof_seats"),
                "wingspan": request.POST.get("wingspan"),
                "max_height": request.POST.get("max_height"),
                "max_weight": request.POST.get("max_weight"),
                "speed": request.POST.get("speed"),
            }
        ]
    }
    if new_company['id'] and new_company['company_name'] and new_company['plains'][0]['id_plain'] and new_company['plains'][0]['plain_name']:
        all_aviacompanies.append(new_company)
        write_in_file("Aviacompanies", str(all_aviacompanies).replace("\'", "\""))
    else:
        return render(request, 'aviasearch/add_aviacompany_page.html', {'message': 'Вы не ввели нужные данные'})


    return render(request, 'aviasearch/add_aviacompany_page.html', {})

def add_new_plain(request):
    i=-1
    j = 0
    all_aviacompanies = open_file("Aviacompanies")

    for aviacompany in all_aviacompanies:
        i+=1
        if request.POST.get("aviacompany_name") == aviacompany['company_name']:
            j = 1
            break
    if j == 0:
        return render(request, 'aviasearch/add_if_no_matches.html', {})

    new_plain = {
        "id_plain": request.POST.get("id_plain"),
        "plain_name": request.POST.get("plain_name"),
        "length": request.POST.get("length"),
        "numof_seats": request.POST.get("numof_seats"),
        "wingspan": request.POST.get("wingspan"),
        "max_height": request.POST.get("max_height"),
        "max_weight": request.POST.get("max_weight"),
        "speed": request.POST.get("speed"),
    }

    if new_plain['id_plain'] and new_plain['plain_name']:
        all_aviacompanies[i]['plains'].append(new_plain)
        write_in_file("Aviacompanies", str(all_aviacompanies).replace("\'", "\""))
    else:
        return render(request, 'aviasearch/add_plain_page.html', {'message': 'Вы не ввели нужные данные'})

    return render(request, 'aviasearch/add_plain_page.html', {})


def add_aviacompany_page(request):
    return render(request, 'aviasearch/add_aviacompany_page.html', {})


def add_plain_page(request):
    return render(request, 'aviasearch/add_plain_page.html', {})

def delete_company_page(request):
    return render(request, 'aviasearch/delete_company_page.html', {})

def delete_plain_page(request):
    return render(request, 'aviasearch/delete_plain_page.html', {})

def remove_company(request):
    j = 0
    all_aviacompanies = open_file("Aviacompanies")

    for aviacompany in all_aviacompanies:
        if request.POST.get("aviacompany_name") == aviacompany['company_name']:
            all_aviacompanies.remove(aviacompany)
            j = 1
    if j == 0:
        return render(request, 'aviasearch/delete_company_if_no_matches.html', {})


    write_in_file("Aviacompanies", str(all_aviacompanies).replace("\'", "\""))
    return render(request, 'aviasearch/delete_company_page.html', {})

def fleet(request, id):
    plains = []
    aviacompanies = open_file("Aviacompanies")
    for plain in aviacompanies[id]['plains']:
        plains.append(plain)
    return render(request, 'aviasearch/fleet.html', {'plains': plains, 'aviacompany': aviacompanies[id]})

def plain(request, id_plain):
    id = id_plain
    aviacompanies = open_file("Aviacompanies")
    for aviacompany in aviacompanies:
        for plain in aviacompany['plains']:
            if int(plain['id_plain']) == int(id):
                pl = plain
    return render(request, 'aviasearch/plain.html', {'plain': pl})


def remove_plain(request):
    i = -1
    j = 0
    all_aviacompanies = open_file("Aviacompanies")

    for aviacompany in all_aviacompanies:
        i += 1
        if request.POST.get("aviacompany_name") == aviacompany['company_name']:
            j = 1
            break

    for plain in all_aviacompanies[i]['plains']:
        if request.POST.get("plain_name") == plain['plain_name']:
            all_aviacompanies[i]['plains'].remove(plain)
            j = 2

    if j == 0:
        return render(request, 'aviasearch/delete_plain_if_no_matches.html', {'message': 'Вы указали несуществующую авиакомпанию'})
    elif j == 1:
        return render(request, 'aviasearch/delete_plain_if_no_matches.html', {'message': 'Вы указали несуществующий самолет'})



    write_in_file("Aviacompanies", str(all_aviacompanies).replace("\'", "\""))
    return render(request, 'aviasearch/delete_plain_page.html', {})









