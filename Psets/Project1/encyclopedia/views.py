from django.shortcuts import render
import markdown
from . import util
import random

def md_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)


def index(request):
   
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    html_content = md_to_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html", {"message":"Entry Not Found"})
    return render(request, "encyclopedia/entry.html", {"html_content" : html_content, "title":title})

def search(request):
    if request.method == 'POST':
        entry_search = request.POST['q']
        html_content = md_to_html(entry_search)
        if html_content != None:
            return render(request, "encyclopedia/entry.html", {
               "title": entry_search,
                "html_content": html_content
            })
        else:
            list_of_entries = util.list_entries()
            substring_entries = []
            for entry in list_of_entries:
                if entry_search.lower() in entry.lower():
                    substring_entries.append(entry)
            return render(request, "encyclopedia/subqueries.html", {
                "substring_entries" : substring_entries
            })


def new_entry(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new_entry.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        titleExist = util.get_entry(title)
        if titleExist is not None:
            return render(request, "encyclopedia/error.html", {
                "message":"Entry page already exists"
            })
        else:
            util.save_entry(title, content)
            html_content = md_to_html(title)
            return render(request, "encyclopedia/entry.html", {
                "title" : title,
                "html_content": html_content
            })


def edit(request):
    if request.method == "POST":
        title = request.POST["entry_title"]
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html",{
            "title":title,
            "content": content
        })

def save_edit(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        util.save_entry(title, content)
        html_content = md_to_html(title)
        return render(request, "encyclopedia/entry.html", {
                "title" : title,
                "html_content": html_content
            })
        

def random_page(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    html_content = md_to_html(random_entry)
    return render(request, "encyclopedia/entry.html",
                  {
                      "title":random_entry,
                      "html_content": html_content
                  })
