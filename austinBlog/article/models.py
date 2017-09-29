from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length = 100) # Blog's title
	category = models.CharField(max_length = 50,blank = True) # Blog's label
	date_time = models.DateTimeField(auto_now_add = True) # Blog's date
	content = models.TextField(blank = True,null = True) # Blog's article body

	def __unicode__(self):
		return self.title

	class Meta: # 按时间下降排序
		ordering = ['-date_time']