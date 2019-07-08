from django.urls import path
from  todo_app.views import home_page,create_todo,update_view,delete_view,show_view,search_view

urlpatterns = [

    path('',home_page,name="home"),
    path('create/',create_todo,name="create_todo"),
    path('update/<int:id>',update_view,name="update-todo"),
    path('delete/<int:id>',delete_view,name="delete-todo"),
    path('show/<int:id>',show_view,name="show-todo"),
    path('search/<int:id>',search_view,name="search-todo")
]
