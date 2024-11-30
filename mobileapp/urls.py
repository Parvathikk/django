from django.urls import path
from mobileapp import views
urlpatterns = [
   path('index/', views.index_page, name="index"),
   path('add_categories/', views.add_categories, name="add_categories"),
   path('add_products/', views.add_products, name="add_products"),
   path('save_category/', views.save_category, name="save_category"),
   path('display_category/',views.display_category, name="display_category"),
   path('edit_category/<int:cat_id>',views.edit_category, name="edit_category"),
   path('update_category/<int:cat_id>', views.update_category, name="update_category"),
   path('login_page/', views.login_page, name="login_page"),
   path('admin_login/', views.admin_login, name="admin_login")
]