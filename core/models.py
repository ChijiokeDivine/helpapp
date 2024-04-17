from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.conf import settings
import cloudinary
from cloudinary.models import CloudinaryField
          
cloudinary.config( 
  cloud_name = getattr(settings, 'CLOUD_NAME', None), 
  api_key = getattr(settings, 'API_KEY', None), 
  api_secret = getattr(settings, 'API_SECRET', None)
)

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class WaitlistEmail(models.Model):
    email = models.CharField(max_length=130, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Waitlist Emails"

    def __str__(self):
        return self.email
    

class Contact(models.Model):
    full_name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    message = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name_plural = "Users that Contacted"
    def __str__(self):
        return self.email
    
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bid = ShortUUIDField(unique=True, length=10, max_length=45, prefix="", alphabet="abcdefgh12345") 
    blog_title = models.CharField(max_length=100, default="blog")
    blog_page_image = CloudinaryField(folder="blog-images")
    description = models.TextField(null=True, blank=True, default="Case study ")
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    featured = models.BooleanField(default=False)
    def blog_image(self):
        return mark_safe('<img src="%s" width="50" height="50" style="border-radius: 5px;" />' % (self.blog_page_image.url))

        
    def save(self, *args, **kwargs):
        # Generate a shorter version of the blog title
        shortened_title = self.blog_title[:40]  # You can adjust the length as needed
        # Convert the shortened title to a slug
        slug = slugify(shortened_title)
        # Set the bid to the slug
        self.bid = f"{slug}"
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        # Delete the image from Cloudinary before deleting the Blog object
        if self.blog_page_image:
            # Get the public ID of the image from Cloudinary
            public_id = self.blog_page_image.public_id
            # Delete the image from Cloudinary
            cloudinary.uploader.destroy(public_id)
        # Call the parent class delete method to delete the Blog object
        super().delete(*args, **kwargs)
    def __str__(self):
        return self.blog_title
    def get_absolute_url(self):
        return f'/blog/{self.bid}/'