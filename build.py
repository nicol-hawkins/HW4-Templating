
top = open('templates/top.html').read()
bottom = open('templates/bottom.html').read()


content = open('content/index.html').read()
index_html = top + content + bottom
open('docs/index.html', 'w+').write(index_html)


content = open('content/about.html').read()
about_html = top + content + bottom
open('docs/about.html', 'w+').write(about_html)


content = open('content/resume.html').read()
resume_html = top + content + bottom
open('docs/resume.html', 'w+').write(resume_html)

