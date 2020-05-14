from django.test import TestCase, RequestFactory
from django.urls import resolve
from .views import Home
from .models import Note
# Create your tests here.
class SmokeTest(TestCase):

    def test_home_view_returns_ok_response(self):
        request = RequestFactory().get('/')
        view = Home.as_view()(request)
        self.assertEquals(view.status_code, 200)

    def test_home_url_resolve_home_view(self):       
        response = resolve('/')
        # print(dir(response.func.view_class), Home)
        self.assertEquals(response.func.view_class, Home)

    def test_home_used_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_process_post_request(self):
        response = self.client.post('/',
                                    data={"text_item":"Get Chicken"})
        
        self.assertTemplateUsed('home.html')
        self.assertEqual(response.status_code, 302)


        print(response.content)
    # def test_home_view(self):
    #     request = RequestFactory.get('/')
    #     response = Home.as_view()(request)

class ModelTest(TestCase):
    
    def test_note_model(self):
        first = Note.objects.create(title='first note')
        second = Note.objects.create(title='first second')

        count = Note.objects.count()
        first_note = Note.objects.all().first()
        second_note = Note.objects.all().last()

        self.assertEquals(count, 2)
        self.assertEquals(first, first_note)
        self.assertEquals(second, second_note)