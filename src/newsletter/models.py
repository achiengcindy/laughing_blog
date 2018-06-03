from django.db import models
class NewsUsers(models.Model):
	name = models.CharField(max_length = 30)
	email = models.EmailField()
	date_added = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name = "NewsUser"
		verbose_name_plural = "NewsUsers"

		def __str__(self):
			return self.email
