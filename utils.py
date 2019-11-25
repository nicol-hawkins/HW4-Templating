import os
import glob
from jinja2 import Template

pages = []

def create_pages_list():
    all_html_files = glob.glob('content/*.html')

    for content_file_path in all_html_files:
        file_path = content_file_path
        file_name = os.path.basename(file_path)
        name_only, extension = os.path.splitext(file_name)
        name_only_title = name_only.title()
        output_file = os.path.join('docs', file_name)

        pages.append({
                "file_path": file_path,
                "title": name_only,
                "output": output_file,
                "file_name": file_name,
            })
        

def main():
    create_pages_list()
    content_of_template = open('templates/base.html', 'r').read()
    template = Template(content_of_template)

    for page in pages:
        content = open(page['file_path'], 'r').read()
        html_full_result = template.render (
                            title = page['title'],
                            content = content,
                            pages = pages,
                        )
        open(page['output'], 'w+').write(html_full_result)

if __name__ == "__main__":
    main()



