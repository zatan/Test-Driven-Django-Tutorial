from django.test import TestCase
from django.utils import timezone

from .models import Poll


class PollModelTest(TestCase):
    def test_can_create_and_save_poll_with_question_and_pub_date(self):
        poll = Poll()
        poll.question = "is it too hot in Florence?"
        poll.pub_date = timezone.now()
        poll.save()

        all_polls = Poll.objects.all()
        self.assertEquals(all_polls.count(), 1)

        our_poll_in_db = all_polls[0]

        self.assertEquals(
            our_poll_in_db.question,
            "is it too hot in Florence?"
        )

        self.assertEquals(our_poll_in_db.pub_date, poll.pub_date)
