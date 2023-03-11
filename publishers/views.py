from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required, permission_required
from .serializers import PublisherSerializer
from .models import Publisher


@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(permission_required('is_publisher', raise_exception=True), name='dispatch')
class AddPublisherAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'publisher.html'

    def post(self, request):
        publisher_serializer = PublisherSerializer(data=request.data)
        if publisher_serializer.is_valid():
            publisher_serializer.save()
            return redirect('home')

        return Response({'message': publisher_serializer.errors})

    def get(self, request):
        publisher = Publisher()
        serializer = PublisherSerializer(publisher)
        return Response({'serializer': serializer, 'publisher': publisher})
