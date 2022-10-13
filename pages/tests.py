from django.test import TestCase
from django.urls import reverse


class HOmePageTests(TestCase):
    def test_home_page_url_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_home_page_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Home Page")

    def test_home_page_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_template_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")














