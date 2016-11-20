#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: models.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-11-20
"""


from termask.constants import QuestionType


class BaseQuestion(object):
    """
    An Abstract implementation for Question
    """

    def __init__(self, question_type=QuestionType.UNKNOWN):
        self.question_type = question_type

    def options(options):
        raise NotImplementedError()

    def ask():
        raise NotImplementedError()


class MultipleChoiceQuestion(BaseQuestion):
    def __init__(self):
        super(MultipleChoiceQuestion, self).__init__(
            QuestionType.MULTIPLE_CHOICE)


class ChoiceQuestion(MultipleChoiceQuestion):
    def __init__(self):
        super(ChoiceQuestion, self).__init__(QuestionType.CHOICE)


class BooleanQuestion(ChoiceQuestion):
    def __init__(self):
        super(BooleanQuestion, self).__init__(QuestionType.BOOLEAN)


class TextQuestion(BaseQuestion):
    def __init__(self):
        super(TextQuestion, self).__init__(QuestionType.TEXT)


class Question(BaseQuestion):
    def __init__(self):
        super(Question, self).__init__(QuestionType.UNKNOWN)
