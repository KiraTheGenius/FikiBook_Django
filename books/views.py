from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .serializers import BookSerializer
from .models import Book


@method_decorator(login_required(login_url='login'), name='dispatch')
class AddBookAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'book.html'

    def post(self, request):
        book_serializer = BookSerializer(data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return redirect('home')

        return Response({'message': book_serializer.errors})

    def get(self, request):
        book = Book()
        serializer = BookSerializer(book)
        return Response({'serializer': serializer, 'book': book})


class BooksView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'booksview.html'

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({'books':serializer.data})