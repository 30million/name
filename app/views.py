from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *

# create post model
# Create get all data in:------- start the get -> function 
@api_view(['GET'])
def get_all_postes(request):
    try:
      postes = Post.objects.all()
    except Post.DesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer = PostSerializer(postes,many=True)
    return Response(serializer.data)
#        ---end get all post--- 

# Create new post data :-----start the post -> function 
@api_view(['POST'])
def create_post(request):
    if request.method == 'POST':
       try:
        serializer = PostSerializer(data=request.data)
       except PostSerializer.DesNotExist:
           return Response(status=status.HTTP_400_BAD_REQUEST) 
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#           ---end the post new function---

#create get one by id:--- start the get one date -> function
@api_view(['GET'])
def get_one_post(request, pk):
    try:
        post =Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)   
    serializer = PostSerializer(post)
    return Response(serializer.data, status=status.HTTP_200_OK)     
#       --- end the get one date function ---

#create update the opst:-- start the put -> function
@api_view(['PUT'])
def update_post(request,pk):
    try:
        post = Post.objects.get(pk=pk)

    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
       serializer = PostSerializer(post,data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_200_OK)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#             --- end the update date ---    
    

#create update the opst:--- start the delete -> function    
@api_view(['DELETE'])
def delete_post(request,pk):
    try:
        post = Post.objects.get(pk=pk)

    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
#            --- end the delete date ---
#--------------------------------------------------------------- end the post

# crete categroy get all:---------------------------------- start the categroy
@api_view(['GET'])
def categroy_get_all(request):
    try: 
     categroy = Category.objects.all()
    except Category.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer = CategorySerializer(categroy, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
#      --- end get all categroy date ---

#create get one categroy
@api_view(['GET'])
def get_one_categroy(request,pk):
    try:
        categroy_one = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(categroy_one)
    return Response(serializer.data, status=status.HTTP_200_OK)
#       --- end get one categroy date ---

# create post new categroy:
@api_view(['POST'])
def create_categroy(request):
     if request.method == 'POST':
            try:
                serializer = CategorySerializer(data=request.data)
            except CategorySerializer.DesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST) 
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED) 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#      --- end post new categroy date ---     
     

# update categroy
@api_view(['PUT'])
def update_categroy(request,pk):
    if request.method == 'PUT':
        try:
            categry = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = CategorySerializer(categry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)    
#        --- end the update one categroy date --- 

# create delete categroy:  
@api_view(['DELETE'])
def delete_categroy(request,pk):
    try:
        categroy = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        categroy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
#          --- end delete catgroy ---
#--------------------------------------------------------------- end the categroy


# creat get all commet:--------------------------------------- start the comment
@api_view(['GET'])
def comment_get_all(request):
    try: 
     categroy = PostComment.objects.all()
    except Category.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer = PostCommentSerializer(categroy, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
#       --- end the get all comment date ---

# create get one comment
@api_view(['GET'])
def get_one_comment(request,pk):
    try:
        coment_one = Post.objects.get(pk=pk)

    except PostComment.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    comment = PostComment.objects.filter(post=coment_one)
    serializer = PostCommentSerializer(comment, many=True)
    return Response(serializer.data , status=status.HTTP_200_OK)
#       --- end the get one comment date ---  
    
             
# creat new post commet            
@api_view(['POST'])
def create_comment(request,pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        serializer = PostCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post)
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
#         --- end the post new comment date ---

# create update one comment
@api_view(['PUT'])
def update_coment(request,pk):
    if request.method == 'PUT':
        try:
            postComment = PostComment.objects.get(pk=pk)
        except PostComment.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = PostCommentSerializer(postComment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
#         --- end the update comment ---
    
# create delete one comment
@api_view(['DELETE'])
def delete_comment(request,pk):
    try:
        deletComment = PostComment.objects.get(pk=pk)
    except PostComment.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        deletComment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
#         --- end the delete one  comment --- 
#--------------------------------------------------------------- end the comment


# create the like:-------------------------------------- start the like    
@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def like_dislike_post(request,pk):
    try:
        blog = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    user = request.user
    if user not in blog.likes.all(): 
        blog.likes.add(user)
    else:   
        blog.likes.remove(user)
    blog.update_like_counts()
    serializer = PostSerializer(blog)
    return Response(serializer.data)
                
#--------------------------------------------------------------- end the like