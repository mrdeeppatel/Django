from django.shortcuts import render,redirect


student = {
    "students": [
        {
            "id": 101,
            "name": "Deep",
            "password": "111"
        },
        {
            "id": 102,
            "name": "Sujal",
            "password": "123@123"
        },
        {
            "id": 103,
            "name": "Soham",
            "password": "123#123"
        }
    ]
}
def login(req):
    if(req.method=="POST"):
        name=req.POST.get("name")
        password=req.POST.get("password")
        print(name)
        for val in student['students']:
            if val["name"]==name and val["password"]==password:
                return render(req,"html/home.html",{
                    "name":name
                })
        return render(req,"html/login.html")

    else:
          return render(req,"html/login.html")


def error(req):
    return render(req,"html/error.html")
def home(req):
    return render(req,"html/home.html")