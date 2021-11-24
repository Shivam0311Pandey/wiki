from django.shortcuts import render
import markdown2
import random
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
import re

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def display(request, title):
    str = util.get_entry(title)
    error = False
    if(not str):
        str = "Request Not Found!"
        error = True
    else:
        str = markdown2.markdown(str)
    return render(request, "encyclopedia/display.html", {
        "str": str,
        "title": title,
        "error": error
    })

def randompage(request):
    entries = util.list_entries()
    str = random.choice(entries)
    return redirect('display', title=str)

def search(request):
    str = request.POST.get('q')
    entries = util.list_entries()
    for entry in entries:
        comparision = str.lower() == entry.lower()
        if (comparision):
            return HttpResponseRedirect(f"wiki/{entry}")
    entries_match = re.compile(".*"+str, re.IGNORECASE)
    new_entries = list(filter(entries_match.match, entries))
    return render(request, "encyclopedia/search.html", {
        "entries": new_entries
    })

def newpage(request):
    if request.method == "POST":
        newtitle = request.POST.get('new_title')
        entries = util.list_entries()
        oldtitle = request.POST.get('old_title')
        if oldtitle:
            entries.remove(oldtitle)
        for entry in entries:
            comparision = newtitle.lower() == entry.lower()
            if (comparision):
                str = newtitle + " already exists!"
                return render(request, "encyclopedia/error.html", {
                    "str": str
                })
        content = request.POST.get('content')
        util.save_entry(newtitle, content)
        return redirect('display', title=newtitle)
    return render(request, "encyclopedia/newpage.html")

def edit(request, title):
    str = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "str": str
    })
    

