from django.test import TestCase
from apps.models import Profile, User

class ProfileTestCase(TestCase):
    def setUp(self):
        # user = User.objects.get(username='superuser')
        Profile.objects.create(title='hello', email='abc@gmail.com', start_year=1999, owner_id=1)
        # Profile.objects.create(title='hey', email='def@gmail.com')

    def test_profile_have_start_year(self):
        prof1 = Profile.objects.get(title='hello')
        # prof2 = Profile.objects.get(title='hey')
        self.assertIs(prof1.start_year, 1999)
        # self.assertEquals(prof2.start_year, '1456')
