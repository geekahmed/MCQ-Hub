import uuid

from requests.api import get
from models import Question, Category, SubCategory
from category_service import get_all_categories, get_sub_categories, get_questions
"""
sc1 = SubCategory(id=uuid.uuid4(), name="Sub Category Name 1")
c1 = Category(id=uuid.uuid4, name="Category 1", sub_categories=[sc1])
q1 = Question(id=uuid.uuid4(), question_header="Test Header", explaination="Test Explain", answer="Test Answer", category_id=c1.id, subcategory_id=sc1.id)
"""

# print(str(q1.id))

# get_all_categories("https://www.sanfoundry.com/")
# get_sub_categories('https://www.sanfoundry.com/1000-electric-circuits-questions-answers/')

get_questions('https://www.sanfoundry.com/electric-circuits-questions-answers-freshers/')