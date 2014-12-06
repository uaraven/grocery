import datetime
import json

from django.http.request import HttpRequest
from django.test.testcases import TestCase

from grocery_list import api_views
from grocery_list.models import List


class ApiTest(TestCase):
    """
    High-level API tests
    """

    def setUp(self):
        List.add('List item 1', datetime.date.today())
        List.add('List item 2', datetime.date.today() + datetime.timedelta(days=1))

    def test_get_list_should_respond_with_json(self):
        response = api_views.get_list(None)

        # May be Django version specific
        self.assertEqual(response._headers['content-type'][1], 'application/json')
        self.assertEqual(response.status_code, 200, "get_list should execute successfully")

    def test_get_list_should_respond_with_correct_list_of_items(self):
        response = api_views.get_list(None)

        result = json.loads(response.content.decode('utf-8'))

        self.assertEqual(len(result), 2, "Should contain two elements")
        self.assertEqual(result[0]['title'], 'List item 1', "Should contain correct first element")
        self.assertEqual(result[1]['title'], 'List item 2', "Should contain correct second element")

    def test_add_list_item_should_add_item_to_db(self):
        request = self._create_request(b'[{"title": "List item 3", "due": "2014-12-22"}]')

        response = api_views.add_list_item(request)

        self.assertEqual(response.status_code, 200, "add_list_item should execute successfully")
        List.objects.get(title__record_name='List item 3')

    def test_set_done_to_true_should_be_reflected_in_db(self):
        id = str(List.objects.get(title__record_name='List item 1').id)

        request = self._create_request('{"id":%s, "checked":true}' % id)

        response = api_views.set_done(request)

        self.assertEqual(response.status_code, 200, "add_list_item should execute successfully")
        self.assertTrue(List.objects.get(title__record_name='List item 1').is_done, 'Should be set to completed')

    def test_set_done_to_false_should_be_reflected_in_db(self):
        item = List.objects.get(title__record_name='List item 1')
        item.is_done = True
        item.save()

        request = self._create_request('{"id":%s, "checked":false}' % item.id)

        response = api_views.set_done(request)

        self.assertEqual(response.status_code, 200, "add_list_item should execute successfully")
        self.assertFalse(List.objects.get(title__record_name='List item 1').is_done, 'Should be set to completed')

    def test_add_should_fail_when_no_json_request(self):
        request = HttpRequest()

        response = api_views.add_list_item(request)

        self.assertEqual(response.status_code, 400, "Response should be 'Bad request'")

    def test_set_done_should_fail_when_no_json_request(self):
        request = HttpRequest()

        response = api_views.set_done(request)

        self.assertEqual(response.status_code, 400, "Response should be 'Bad request'")

    def _create_request(self, json):
        request = HttpRequest()
        request.method = 'POST'
        request.META['HTTP_X_REQUESTED_WITH'] = 'XMLHttpRequest'
        request._body = json
        return request