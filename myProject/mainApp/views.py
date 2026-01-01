from django.http import HttpResponse

def post_details(request, post_id):
    return HttpResponse(f"<h1>Show main app {post_id}</h1>")

def user_profile(request, username):
    return HttpResponse(f"<h1>Profile of user {username}</h1>")

def article_by_year(request, year):
    return HttpResponse(f"<h1>Articles of year {year}</h1>")

def article_details(request, year, month):
    return HttpResponse(f"<h1>Articles from {year} - {month}</h1>")

def article_kwargs(request, **kwargs):
    return HttpResponse(f"<h1>Data : {kwargs}</h1>")