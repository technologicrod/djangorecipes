Trial Project by Rodwell Matchon for Ingenuity requirement using Python Django.

Functions are found in views.py and templates are found in the "arisencode" folder.

There are two types of users: Admin and Basic users.
In the login page, you can create an account and you can choose if it can be an Admin or a Basic user.
Basic users can create, view, edit, and delete their own recipes.
Admin users can do the same thing but can also view, edit, and delete ALL recipes in the database through accessing the Admin Dashboard.
Data are not actually deleted but only changed its status from "Active" to "Inactive" to avoid data deletion completely 
but these "deleted" data can't be seen in the UI but can be seen in the /admin.

To run, use the command "python manage.py runserver" to run the server/localhost.

Sample users:
Admin accounts:
1.) email - matchon.rodwell@gmail.com
    password - 123

Basic accounts:
1.) email - abc123@gmail.com
    password - abc
2.) email - naruto@gmail.com
    password - naruto