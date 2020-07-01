from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.db.models import Count, Sum

from datetime import datetime as dt, timedelta as td

from post.models import Post
from .serializers import PostSerializer


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def post_collection(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':

        data = {'text': request.query_params['text'], 'author': request.user.username}
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET',])
@permission_classes((AllowAny,))
@authentication_classes((JSONWebTokenAuthentication,))
def post_element(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)


@api_view(["PUT", ])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def like_post(request, pk):
    import pdb
    pdb.set_trace()
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == "PUT":
        serializer = PostSerializer(post, data={"count_like":post.count_like+1, "author":post.author,
                                          "text":post.text})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)



@api_view(["PUT", ])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def unlike_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == "PUT":
        serializer = PostSerializer(post, data={"count_unlike":post.count_unlike+1, "author":post.author,
                                          "text":post.text})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)



@api_view(["GET", ])
@permission_classes((AllowAny,))
@authentication_classes((JSONWebTokenAuthentication,))
def analitics(request):
    if request.method == 'GET':
        start = request.query_params['date_from']
        end = request.query_params['date_to']

        all_posts = Post.objects.filter(date__range=[start, end])
        grouped = all_posts.values('date').annotate(all_likes=Count('count_like'))

        result = grouped.filter(date__gte=start, date__lte=end).values('date').annotate(
            likes=Sum('count_like')).order_by()

        result = {i['date'].strftime('%Y-%m-%d'): i['likes'] for i in result}
        start = dt.strptime(start, '%Y-%m-%d')
        end = dt.strptime(end, '%Y-%m-%d')
        step = td(days=1)
        while start < end:
            if start.strftime('%Y-%m-%d') not in result.keys():
                result[start.strftime('%Y-%m-%d')]=0
            start += step


        return Response(result)

