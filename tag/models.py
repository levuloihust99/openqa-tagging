from typing import Text
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, TextField
from django.db.models.fields.related import ForeignKey
from django.forms import widgets
from django import forms

from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.contrib import admin

# Create your models here.
class QASample(models.Model):
    class Meta:
        ordering = ['pk']
    
    link = 'Edit'
    positive_document = TextField(null=True, blank=True)
    positive_document_title = CharField(max_length=300, null=True, blank=True)
    question = CharField(max_length=300, null=True, blank=True)
    hard_negative_document = TextField(null=True, blank=True)
    hard_negative_document_title = CharField(max_length=300, null=True, blank=True)

    def answers(self):
        if not self.answer_set.all():
            return "-"
        item = "<li>{}</li>"
        answers = [item.format(ans) for ans in self.answer_set.all()]
        answers_html = "".join(answers)
        return mark_safe("<ul>{}</ul>".format(answers_html))

    def positive(self):
        positive_document = self.positive_document if self.positive_document else "-"
        positive_document_title = self.positive_document_title if self.positive_document_title else "-"
        if not self.positive_document and not self.positive_document_title:
            return '-'
        return format_html(
            "<ul><li><strong>{}</strong></li><li>{}</li></ul>",
            positive_document_title, positive_document
        )

    def hard_negative(self):
        hard_negative_document = self.hard_negative_document if self.hard_negative_document else "-"
        hard_negative_document_title = self.hard_negative_document_title if self.hard_negative_document_title else "-"
        if not self.hard_negative_document and not self.hard_negative_document_title:
            return '-'
        return format_html(
            "<ul><li><strong>{}</strong></li><li>{}</li></ul>",
            hard_negative_document_title, hard_negative_document
        )

    def __str__(self):
        if self.question is not None:
            return self.question
        return '---'

class Answer(models.Model):
    sample = ForeignKey(QASample, on_delete=models.CASCADE)
    answer = CharField(max_length=200)

    def __str__(self):
        if self.answer is not None:
            return self.answer
        return 'None'