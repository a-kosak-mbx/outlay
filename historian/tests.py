from django.test import TestCase
from django.urls import reverse

from historian.models import Tag


class TagModelTest(TestCase):
    @staticmethod
    def create_tag(name='test', description='some test description', color=0xf00ff0, parent=None):
        tag = Tag.objects.create(name=name, description=description, color=color)
        if parent is not None:
            tag.parent.set(parent)
        return tag

    def test_tag_creation(self):
        tag = self.create_tag()
        self.assertTrue(isinstance(tag, Tag))
        self.assertEqual(tag.name, 'test')


class HistorianViewTest(TestCase):
    def test_view_url_forbidden(self):
        response = self.client.get('/historian/')
        self.assertEqual(response.status_code, 403)


class TagListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_tags = 15

        for author_id in range(number_of_tags):
            Tag.objects.create(
                name=f'tag{author_id}',
                description=f'some description text',
                color=0xf00ff0
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/historian/tags/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('tags'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('tags'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'historian/tag_list.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('tags'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['tag_list']), 10)

    def test_lists_all_tags(self):
        response = self.client.get(reverse('tags') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['tag_list']), 5)
