import os
import uuid

from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=1000)
    uuid = models.UUIDField(unique=True, blank=True)
    commands = models.TextField()

    def __str__(self):
        return "{} ({})".format(self.name, self.id)

    def save(self, *args, **kwargs):

        if not os.path.exists(self.path):
            raise ValueError("Path does not exists.")

        if self.uuid is None:
            self.uuid = uuid.uuid1()

        return super().save(*args, **kwargs)


class Hook(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    header = models.TextField()
    body = models.TextField()
    commands_result = models.TextField()

    def __str__(self):
        return "{} {} ({})".format(self.project.name, self.created_at.date().isoformat(), self.id)
