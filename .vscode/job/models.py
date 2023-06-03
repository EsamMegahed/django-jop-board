from django.db import models

# Create your models here.


job_Type = (
    ("Full Time", "Full Time"),
    ("Part Time", "Part Time"),
)


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=100)
    # location =
    job_type = models.CharField(max_length=100, choices=job_Type)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experiences = models.IntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.title
