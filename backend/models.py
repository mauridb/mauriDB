from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=256, blank=False, null=False)
    project_description = models.TextField()
    project_status = models.CharField(max_length=10) # TODO: enum field
    project_likes = models.IntegerField()
    project_level = models.CharField(max_length=10) # TODO: enum field
    author = models.ForeignKey(User)

class Skill(models.Model):
    skill_name = models.CharField(max_length=55, blank=False, null=False)
    skill_status = models.CharField(max_length=10)
    skill_description = models.TextField()
    skill_type = models.CharField(max_length=10) # TODO: better if enum type field BE|FE allow null
    skill_area = models.CharField(max_length=10) # TODO: better if enum type field not null VCS|DOCKER|SCRIPTING|VIEW ...
    skill_level = models.CharField(max_length=10) # TODO: better if enum type field BASIC|INTERMEDIATE|ADVANCED|MASTER|DOMAIN
    skill_value = models.DecimalField(max_digits=3, decimal_places=1)
    skill_likes = models.IntegerField()
    project = models.ForeignKey(Project, blank=True, null=True)
    owner = models.ForeignKey(User)