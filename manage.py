import sys
import utils


print("This is argv:", sys.argv)
command = sys.argv[1]
print(command)
if command == "build":
    create_pages_list()
    main()
elif command == "new":
    new_content_page = '''
            <h1> New Content! <h1>
            <p> new content... </p>
        '''
    open("content/new_content_page.html", "w+").write(new_content_page)
elif command == None:
    print('''Usage:
                Rebuild site: python manage.py build
                Create new page: python manage.py new ''')
else:
    print("Please specify 'build' or 'new'")



