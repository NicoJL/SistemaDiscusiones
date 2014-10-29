from django.test import TestCase

from django.test.client import  RequestFactory

from apps.users.models import User
from apps.home.views import IndexView

class TestHome(TestCase):

	def setUp(self):
		self.factory = RequestFactory()
		self.user = User.objects.create_user(username="nicolas",password='12345',email="njl27@hotmail.com")

	def test_view_IndexView(self):
		request = self.factory.get('/')	
		view = IndexView.as_view()
		response = view(request)
		self.assertEqual(response.status_code,200)