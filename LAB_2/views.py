from django.shortcuts import render

def showlist(request):
    fruits=["Mango","Apple","Bananan","Jackfruits"]
    student_names=["Tony","Mony","Sony","Bob"]
    return render(request, 'showlist.html', {"fruits":fruits,"student_names":student_names}
    )
