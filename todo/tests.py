from django.test import TestCase
from django.urls import reverse
from todo.models import Todo


def create_todo_item(description, done=False):
    return Todo.objects.create(description=description, done=done)


# class TodoModelTests(TestCase):
#
#     def setUp(self):
#         self.todo = create_todo_item("Math Homework")
#
#     def test_todo_description(self):
#         self.assertEqual(self.todo.description, "Math Homework")
#
#     def test_todo_done(self):
#         self.assertFalse(self.todo.done)


class IndexViewTests(TestCase):

    # def test_no_todo_item(self):
    #     response = self.client.get(reverse('todo:index'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "Nothing to do")
    #     self.assertQuerysetEqual(response.context['todo_list'], [])

    def test_have_a_todo_item(self):
        """first"""
        todo = create_todo_item("homework")
        response = self.client.get(reverse('todo:index'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Nothing to do")
        self.assertContains(response, todo.description)
        self.assertQuerysetEqual(response.context['todo_list'], ['<Todo: homework>'])


# class AddTodoViewTests(TestCase):
#
#     def test_add_todo_item(self):
#         response = self.client.get(reverse('todo:add'))
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, reverse('todo:index'))


class DoneTodoViewTests(TestCase):

    def test_done_todo_item(self):
        """second"""
        todo = create_todo_item("watch movie")
        self.assertFalse(todo.done)
        response = self.client.get(reverse('todo:done', args=(todo.id, )))
        self.assertTrue(Todo.objects.get(id=todo.id).done)
        response = self.client.get(reverse('todo:index'))
        self.assertNotContains(response, todo.description)


class UrlTests(TestCase):
    def test_when_todo_is_done_redirects_to_index(self):
        """third"""
        todo = create_todo_item("checkout room")
        response = self.client.get(reverse('todo:done', args=(todo.id, )))
        self.assertRedirects(response, reverse('todo:index'))

    def test_wrong_done_url(self):
        """fourth"""
        response = self.client.get(f'todo/100/done')
        self.assertEqual(response.status_code, 404)
