from django.db import models
import uuid
import json


class project(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField(null=True, blank=True)
    source_link = models.CharField(max_length=2000 ,null= True , blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null = True , blank=True)
    vote_ratio = models.IntegerField(default=0, null = True , blank=True)
    demo_link = models.CharField(max_length=2000,null= True , blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True , primary_key=True, editable=False)

    def __str__(self):
        return self.title
    
class review(models.Model):
    VOTE_TYPE = (
        ('Up' , 'Up Vote'),
        ('down', 'Down Vote')
    )
    project = models.ForeignKey(project , on_delete=models.CASCADE)
    value = models.CharField(max_length = 200 , null=True, blank=True , choices=VOTE_TYPE)
    body= models.TextField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True , primary_key=True, editable=False)

    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length =200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True , primary_key=True, editable=False)

    def __str__(self):
        return self.name


class amazon_links_list(models.Model):
    product_name = models.CharField(max_length=200)
    projuct_link = models.TextField(max_length=2000)

    def get_name(self):
        return json.loads(self.product_name)

    def set_name(self, items):
        self.product_name = json.dumps(items)

    def get_items(self):
        return json.loads(self.projuct_link)

    def set_items(self, items):
        self.projuct_link = json.dumps(items)



