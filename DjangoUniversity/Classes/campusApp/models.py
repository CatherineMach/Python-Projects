from django.db import models


class UniversityCampus(models.Model):
    name = models.CharField(max_length=60, blank=True, null=False)
    state = models.TextField(max_length="2", blank=True)
    campusID = models.IntegerField(default="", blank=True, null=False)

    object = models.Manager()

    def __str__(self):
        # Returns the input value of the title and instructor name
        # field as a tuple to display in the browser instead of the default titles
        display_campus = '{0.name}: {0.state}'
        return display_campus.format(self)

    class Meta:
        verbose_name_plural = "University Campus"