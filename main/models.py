from django.db import models

# Create your models here.


class TimiStampModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(TimiStampModel):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Tag(TimiStampModel):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Author(TimiStampModel):
    title = models.CharField(max_length=212)
    description = models.TextField()
    images = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.title


class Post(TimiStampModel):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='image/')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class About(TimiStampModel):
    title = models.CharField(max_length=212)
    body = models.TextField()
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.title


class HappyClients(TimiStampModel):
    name = models.CharField(max_length=212)
    profession = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='happy/')

    def __str__(self):
        return self.name


class Comment(TimiStampModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=212)
    email = models.EmailField()
    website = models.URLField()
    message = models.TextField()
    image = models.ImageField(upload_to='image', null=True, blank=True)

    def __str__(self):
        return self.name
