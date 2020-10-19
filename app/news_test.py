import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test the behaviour of the news class
    '''
    def setUp(self):
        '''
        Run before every test
        '''
        self.new_article = News(1234,'This is very wild', 'Shocking news of what happened last night','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assert(isinstance(self.new_article,News))

if __name__ == '__main__':
    unittest.main()