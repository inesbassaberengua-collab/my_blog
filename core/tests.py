from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="testpass123")

    def test_creacion_post(self):
        post = Post.objects.create(
            title="Mi primer post",
            content="Este es el contenido de prueba del post.",
            author=self.user,
        )
        self.assertEqual(str(post), "Mi primer post")
        self.assertEqual(post.author.username, "tester")

