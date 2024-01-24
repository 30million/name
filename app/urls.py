from django.urls import path
from .views import *

urlpatterns = [
    
    #------------------------------------------ start ->POST -> path:
    # urls get all date
    path('', get_all_postes),

    # urls app create new 
    path('create_post/', create_post),

    # urls app get one id = pk
    path('get_one/<int:pk>/', get_one_post),

    # urls app update post one id = pk
    path('update_post/<int:pk>/', update_post),

    # urls app delete id = pk
    path('delete_post/<int:pk>/', delete_post),
    ############################################

    #------------------------------------------ start -> CATEGROY -> path:
    # urls to get all the categroy data
    path('categroy/',categroy_get_all),

    # urls create new categroy
    path('create_categroy/',create_categroy),

    # urls get one categroy id = pk
    path('get_one_categroy/<int:pk>/',get_one_categroy),

    # urls update one categroy id = pk
    path('update_categroy/<int:pk>/',update_categroy),
    
    # urls delete one categroy id = pk
    path('delete_categroy/<int:pk>/',delete_categroy),
    #################################################

    #----------------------------------------- start -> COMMENT -> path:
    # urls create comment
    path('create_comment/<int:pk>/',create_comment),

    # urls get all comment
    path('comment_get_all',comment_get_all),

    # urls get one comment id = pk
    path('get_one_comment/<int:pk>/',get_one_comment),

    # urls update one comment id = pk
    path('update_coment/<int:pk>/',update_coment),

    # urls delete comment id = pk
    path('delete_comment/<int:pk>/',delete_comment),
    #################################################

    # ------------------------------------------ start -> LIKE -> path: 
    # urls like post id = pk
    path('like_dislike_post/<int:pk>/',like_dislike_post),
    ######################################################
   
]