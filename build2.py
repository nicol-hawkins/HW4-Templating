
def main():

    pages = [
    {
        "filename": "content/about.html",
        "output": "docs/about.html",
        "title": "About Me",
    },
     {
        "filename": "content/index.html",
        "output": "docs/index.html",
        "title": "My Blog",
    },
     {
        "filename": "content/resume.html",
        "output": "docs/resume.html",
        "title": "My Resume",
    },
]
    
    for page in pages:
        print(page['filename'])

    template = open("./templates/base.html").read()
    content = open(page['filename']).read()

    finished_doc = template.replace("{{content}}", content)
    open(page['output'], "w+").write(finished_doc)


    # content = open('content/index.html').read()
    # index_html = top + content + bottom
    # open('docs/index.html', 'w+').write(index_html)


    # content = open('content/about.html').read()
    # about_html = top + content + bottom
    # open('docs/about.html', 'w+').write(about_html)


    # content = open('content/resume.html').read()
    # resume_html = top + content + bottom
    # open('docs/resume.html', 'w+').write(resume_html)

if __name__ == "__main__":
    main()

