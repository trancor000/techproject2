from django.db import models


class djangoSchool(models.Model):
    academy = models.CharField(max_length=60)
    type = models.CharField(max_length=60)
    tuition = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)


class djangoClasses(models.Model):
    title = models.CharField(max_length=60)
    course_number = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)
    instructor_name = models.CharField(max_length=60, default="", blank=True)
    duration = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)


class djangoAide(models.Model):
    address = models.CharField(max_length=100)
    duration = models.DecimalField(max_digits=1000, decimal_places=2)


class djangoGraduation(models.Model):
    years = models.DecimalField(max_digits=100, decimal_places=2)
    date = models.CharField(max_length=60)


    SUBJECTS = {
        ('math', 'math'),
        ('science', 'science'),
        ('spanish', 'spanish'),
    }

    objects = models.Manager()

    def __str__(self):
        return self.name