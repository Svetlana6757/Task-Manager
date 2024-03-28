# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.done = False

    def mark_as_done(self):
        self.done = True

    def is_done(self):
        return self.done


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_as_done(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                task.mark_as_done()
                break

    def get_current_tasks(self):
        return [task for task in self.tasks if not task.is_done()]


# Демонстрация использования
task_manager = TaskManager()
task_manager.add_task(Task("Закончить проект", "2024-04-30"))
task_manager.add_task(Task("Купить продукты", "2024-03-29"))

task_manager.mark_task_as_done("Купить продукты")

# Вывод текущих задач
current_tasks = task_manager.get_current_tasks()
for task in current_tasks:
    print(f"Описание: {task.description}, Срок: {task.due_date}, Выполнено: {task.is_done()}")
