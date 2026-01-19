from django.shortcuts import render

# Data from views
def index(request):
    
    dict={"u1":{"name":"Persion name","roll_no":12,"marks":{"php":99,"dsa":100,"dad":98}},
    "u2":{"name":"Persion name 2","roll_no":13,"marks":{"php":100,"dsa":97,"dad":99}}}

    return render(request,"html/index.html",dict)