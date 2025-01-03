import uuid

from django.db import models


# Create your models here.

class BaseMode(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)

    def __str__(self):
        return NotImplemented('str method not implemented')


class User(BaseMode):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    token = models.UUIDField(default=uuid.uuid4, editable=True, unique=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('pk',)

    def __str__(self):
        return self.name


class TodoList(BaseMode):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='Author',
    )

    class Meta:
        verbose_name = 'Todo List'
        verbose_name_plural = 'Todo Lists'
        ordering = ('pk',)

    def __str__(self):
        return self.title
