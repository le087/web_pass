#-*- coding: utf-8 -*-
from django.db import models

class Log(models.Model):
    date_pub = models.DateTimeField(auto_now_add=True)
    brauser = models.CharField(blank=True, null=False, max_length=200)

    def __unicode__(self):
        return self.brauser

    class Meta:
        ordering = ["-date_pub"]

class Counter(models.Model):
    pass_counter = models.IntegerField()

    def get_counter(self, num_passwords):
        count = Counter.objects.get(id=1).pass_counter        
        count += num_passwords
        count_in_db = Counter(id=1, pass_counter=count)
        count_in_db.save()
        return count
