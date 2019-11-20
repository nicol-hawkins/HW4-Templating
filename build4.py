def main():
    for page in pages:
        file_name = page["filename"]
        output = page["output"]
        title = page["title"]

        # Read in the content which
        # is located is now stored in file_name
        content = open(file_name).read()
        template = page_builder(content, title)
        
        # write page by opening the output(docs)
        # by accessing it within the dictionary.
        # write it to template cause templates
        # contains the function page_builder,
        # which actually constructs the pages.
        open(page["output"], "w+").write(template)
       

# This function constructs the webpage by replacing
# empty braces with actual content and titles within
# the newly constructed base template.
def page_builder(content, title):
    template = open("templates/base.html").read()
    template_plus_content = template.replace("{{content}}", content)
    finished_page = template_plus_content.replace("{{title}}", title)
    return finished_page


import glob
all_html_files = glob.glob("content/*.html")
print(all_html_files)

import os
file_path = "content/.html"
file_name = os.path.basename(file_path)
print(file_name)
name_only, extension = os.path.splitext(file_name)
print(name_only)

for file_path in glob.glob("content/*.html"):
    print(file_path)



pages = []
pages.append({
    "filename": "content/index.html",
    "title": "Index",
    "output": "docs/index.html"
    })

pages.append({
    "filename": "content/about.html",
    "title": "About",
    "output": "docs/about.html"
    })

pages.append({
    "filename": "content/resume.html",
    "title": "Resume",
    "output": "docs/resume.html"
    })

print(pages)
   
if __name__ == "__main__":
    main()



