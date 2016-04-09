# -*- coding: utf-8 -*-

#  Creation Date: 07.04.2015

from __future__ import absolute_import

from celery import Celery


app = Celery("kumpel",
                broker="redis://localhost",
                include=["kumpel.tasks"])

app.config_from_object("kumpel.celeryconfig")

if __name__ == "__main__":
    app.start()
