from django.db import models

# Create your models here.

class Task(models.Model):
    task_id = models.AutoField(db_column='task_id', primary_key=True, null=False)
    title = models.CharField(db_column='title', max_length=200)
    description = models.CharField(db_column='description', max_length=255)
    completed = models.BooleanField(db_column='completed', default=False)
    created_at = models.DateTimeField(db_column='created_at', auto_now_add=True)
    completed_at = models.DateTimeField(db_column='completed_at', null=True, blank=True)

    def __str__(self):
        return f"{self.title} {self.description}"
    
    def __as_dict(self):
        return {
            'task_id': self.task_id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at,
            'completed_at': self.completed_at
        }
    
    class Meta:
        db_table = 'tasks'