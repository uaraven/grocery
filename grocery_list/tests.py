from django.test.testcases import TestCase

from datetime import date

from grocery_list.models import History
from grocery_list.models import List


class ListTest(TestCase):
    def test_add_item_should_add_to_history(self):
        List.add("Item title", date.today())

        history = History.objects.all()

        self.assertEqual(len(history), 1, "Should store title for history")
        self.assertEqual(history[0].record_name, "Item title", "Should store title")

    def test_add_item_should_not_new_history_record(self):
        History.objects.create(record_name='Other item')

        List.add("Other item", date.today())

        history = History.objects.all()

        self.assertEqual(len(history), 1, "Should note add another history record")
        self.assertEqual(history[0].record_name, "Other item", "Should not update history record")
