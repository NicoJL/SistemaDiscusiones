from django.test import TestCase

from apps.users.models import User
from apps.disqus.models import Question

class SimpleTest(TesCase):

	def test_save_slug(self):
		user = User.objects.create_user(username='nicolas',email="njl27@hotmail.com")
		question = Question.objects.create(user=user,
				title="pregunta no 1",
				description='esta es la descripcion')
		self.assertEqual(question.slug,'pregunta-no-1')
