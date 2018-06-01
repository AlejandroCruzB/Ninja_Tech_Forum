#!/usr/bin/env python
from handlers.base import BaseHandler
from google.appengine.api import users
from models.topic import Topic

class TopicHandler(BaseHandler):
    def get(self):
        return self.render_template("topic_add.html")

    def post(self):
        logged_user=users.get_current_user()

        if not logged_user:
            return self.write("Please login before")

        title_value = self.request.get("title")
        text_value = self.request.get("text")

        if "<script>" in text_value:
            return self.write("No Hack")

        if not text_value:
            return self.write("Required")

        if not title_value:
            return self.write("Required")

        new_topic = Topic(
            title=title_value,
            content=text_value,
            author_email=logged_user.email(),
        )

        new_topic.put()


        return self.redirect_to("topic-detail", topicid=new_topic.key.id())
