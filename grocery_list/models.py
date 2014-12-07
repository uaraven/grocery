from django.db import models


class History(models.Model):
    record_name = models.CharField(max_length=200)


class List(models.Model):
    is_done = models.BooleanField(default=False)
    title = models.ForeignKey(to=History)
    due_date = models.DateTimeField()

    def name(self):
        return self.title.record_name

    def __str__(self):
        return "{Title: %s, Due: %s, Done: %s}" % (self.title.record_name, str(self.due_date), str(self.is_done))

    @staticmethod
    def add(title, due_date):
        """
        Utility method to add new list item.

        Will look through history to find if such title was used before and will create new title in history otherwise.
        :param title: Grocery list title
        :param due_date: Due date for an item
        :return: newly created list item
        """
        history = History.objects.filter(record_name=title)
        if len(history) == 0:
            history_item = History.objects.create(record_name=title)
            history_item.save()
        else:
            history_item = history[0]

        list_item = List.objects.create(title=history_item, is_done=False, due_date=due_date)
        list_item.save()

        return list_item