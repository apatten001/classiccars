import datetime

from django.core.management.base import BaseCommand

from pastebin.models import Paste


class Command(BaseCommand):

    help = """deletes pastes not updated within 24 hrs.
                
                use this subcommand to clear all older pastes      
            """

    def handle(self, *args, **options):

        now = datetime.datetime.now()
        yesterday = now - datetime.timedelta(1)
        old_paste = Paste.objects.filter(updated_on__lte=yesterday)
        old_paste.delete()


