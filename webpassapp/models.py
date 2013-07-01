#-*- coding: utf-8 -*-
from django.db import models

class Log(models.Model):
    date_pub = models.DateTimeField(auto_now_add=True)
    brauser = models.CharField(blank=True, null=False, max_length=200)
    ip = models.CharField(blank=True, null=False, max_length=100)

    def __unicode__(self):
        return self.brauser

    def save_log_note(self, user_agent, ip):
        """
        save user-agent, date_pub, ip to database
        """
        log_note = Log(brauser=user_agent, ip=ip)
        log_note.save()
        return True

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
