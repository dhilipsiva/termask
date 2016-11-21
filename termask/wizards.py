#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: mizards.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-11-20
"""


class BaseWizard(object):
    """
    Abstract class to be used by other method
    """
    def __init__(self, questions):
        super(BaseWizard, self).__init__()
        self.questions = questions

    def next(self, value):
        """
        Get the previous question
        """
        raise NotImplementedError()

    def previous(self, value):
        """
        Get the next question based on value selected
        """
        raise NotImplementedError()


class DynamicWizard(BaseWizard):
    """
    This is for Dynamic Questions.
    `static` as in the answers are
    """
    def __init__(self, questions):
        super(DynamicWizard, self).__init__(questions)


class StaticWizard(DynamicWizard):
    """
    This is for static Questions.
    `static` as in questions and answers are provided as sequence,
    and is asked to the user sequentially
    """
    def __init__(self, questions):
        super(StaticWizard, self).__init__(questions)
