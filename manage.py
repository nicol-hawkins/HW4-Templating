import utils.py
import sys

print("This is argv:", sys.argv)
command = sys.argv[1]
print(command)
if command == "build":
    create_pages_list()
    main()
elif command == "new":
    
elif command == None:
    print('''Usage:
                Rebuild site: python manage.py build
                Create new page: python manage.py new ''')
else:
    print("Please specify 'build' or 'new'")



