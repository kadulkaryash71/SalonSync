from django.core.management.base import BaseCommand 
from django.db.models import Count 
from app.models import Article, Comment 
from datetime import timedelta, datetime 
from django.utils.timezone import utc 


def now(): 
	return datetime.utcnow().replace(tzinfo=utc) 

class Command(BaseCommand): 
	help = 'Displays stats related to Article and Comment models'

	def add_arguments(self, parser): 
		parser.add_argument('-t', '--time', type=int, help='Articles published in last t hours') 

	def handle(self, *args, **kwargs): 
		t = kwargs['time'] 
		if not t: 
			t=5
		From = now() - timedelta(hours=t)
		To = now() 

		articles_published_in_last_t_hour = Article.objects.filter( 
			created_on__gt=From, created_on__lte=To).count() 
		
		comments_published_per_article = Comment.objects.filter( 
			created_on__gt=From, created_on__lte=To).values( 
			'article').annotate(count=Count('article')).order_by() 

		print(f"Articles Published in last {t} hours = ", 
			articles_published_in_last_t_hour) 

		print(f"Comments per Article in last {t} hours") 
		for data in comments_published_per_article: 
			print(data)
