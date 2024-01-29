from django.shortcuts import render

from . import util

import markdown

#Converts markdown to HTML
def markdown_to_html(title):
    content =  util.get_entry(title)
    markdowner = markdown.Markdown()

    if content == None:
        return None
    else: 
        return markdowner.convert(content)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request,title):
    
    
    html_content = markdown_to_html(title)

    if html_content == None:
        return render(request, "encyclopedia/error.html")
    else:
        return render(request, "encyclopedia/wiki.html", {'html_content': html_content}, {'title':title})




