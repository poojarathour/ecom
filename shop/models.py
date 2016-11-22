from django.db import models
from django.utils import timezone

##user=models.OneToOneField(settings.AUTH_USER_MODEL,primary_key=True)
    #slug=models.UUIDField(defult=uuid.uuid4, blank=True, editable=False)
class Product(models.Model):
    title = models.CharField(max_length=200)
    size = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    quality = models.CharField(max_length=50)
    text = models.TextField()
    posted_by=models.ForeignKey('auth.user')
    picture=models.ImageField('Profile picture', upload_to='profile_pics/%Y-%m-%d/',null=True,blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
