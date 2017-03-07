from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def main_page(request):
    page = """
    <html>
    <head>
        <title>PP Application</title>
    </head>
    <body>

    </body>
    </html>
    """
    return HttpResponse(page)