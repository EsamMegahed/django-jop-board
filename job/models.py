from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.


job_Type = (
    ("Full Time", "Full Time"),
    ("Part Time", "Part Time"),
)


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


def image_Upload(instance, filename):
    image_name, extenion = filename.split(".")
    return "jobs/%s.%s" % (instance.id, extenion)


class Job(models.Model):
    owner = models.ForeignKey(User, related_name="job_owner", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    # location =
    job_type = models.CharField(max_length=100, choices=job_Type)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experiences = models.IntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="jobs/", null=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class Apply(models.Model):
    job = models.ForeignKey(Job, related_name="apply_job", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to="apply/")
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
