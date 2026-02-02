from django.shortcuts import render

students = {
    "01": {"name": "a1","cgpa":8.9},
    "02": {"name": "a2","cgpa":9.9},
    "03": {"name": "a3","cgpa":7.9},
    "04": {"name": "a4","cgpa":8.3},
}

def result(req):
    result = None  # Initialize to None or empty
    if req.method == "POST":
        id = req.POST.get("id")
        for key, val in students.items():
            if key == id:
                result = val    
                break
    return render(req, "login.html", context={"students": students, "result": result})