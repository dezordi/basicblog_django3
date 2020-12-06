# BasicBlog with Django3

This repository store all files emcompassing the Django framework for basic blog application, the basic structure was retrivied following the tutorial of [nETSETOS](https://www.youtube.com/channel/UC7dD1bOWXiJH3lJLsTInxOQ). 

## Web application
How the blog works can be seen in this [video](https://www.youtube.com/watch?v=a55qXRkWlug&ab_channel=filipezimmer).

## Dependencies

This blog was created in a conda enviroment with the following dependencies:
- [asgiref==3.3.1](https://pypi.org/project/asgiref/)
- [sqlparse==0.4.1](https://pypi.org/project/sqlparse/)
- [certifi==2020.11.8](https://pypi.org/project/certifi/)
- [pytz==2020.4](https://pypi.org/project/pytz/)
- [Django==3.0](https://www.djangoproject.com/)
- [django-taggit==1.2.0](https://pypi.org/project/django-taggit/)
- [django-widget-tweaks==1.4.8](https://pypi.org/project/django-widget-tweaks/)
- [django-autoslug==1.9.8](https://pypi.org/project/django-autoslug/)
- [django-allauth==0.44.0](https://pypi.org/project/django-allauth/)

## Disclaimer
The base code of general blog structure (posts fields, comment and tag functions) was originally create by netsetos and the complete code with complementary functions were present [here](https://github.com/netsetos/blog_site). I had picked some structures, modified them when it was necessary, studied the code, implemented a bootstrap template and the functions to work with multi users and with navbar conditional menus based on user authentication as well as an add_post section that only works if the user is logged on blog.
