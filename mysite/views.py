from django.shortcuts import redirect

def index(request):
    """redirect to todo app"""
    return redirect( 'todo:index' )
