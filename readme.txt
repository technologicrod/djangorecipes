Trial Project by Rodwell Matchon for Ingenuity requirement using Python Django.

Functions are found in views.py. Templates, views.py, and other essential files are found in the "arisencode" folder.

There are two types of users: Admin and Basic users.
In the login page, you can create an account and you can choose if it can be an Admin or a Basic user.
Basic users can create, view, edit, and delete their own recipes.
Admin users can do the same thing but can also view, edit, and delete ALL recipes in the database through accessing the Admin Dashboard.
Data are not actually deleted but only changed its status from "Active" to "Inactive" to avoid data deletion completely.
However, these "deleted" data can't be seen in the UI but can be seen in the /admin.

To run the server/localhost:8000, use the command "python manage.py runserver".

Sample users:
Admin accounts:
1.) email - matchon.rodwell@gmail.com
    password - 123

Basic accounts:
1.) email - abc123@gmail.com
    password - abc
2.) email - naruto@gmail.com
    password - naruto

Super User for accessing the /admin to check the database:
1.) username - admin123
    password - 123