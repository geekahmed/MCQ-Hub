from dataclasses import dataclass
from typing import List
import uuid


@dataclass
class SubCategory:
    id: uuid
    name: str
    description: str

@dataclass
class Category:
    id: uuid
    name: str
    sub_categories: List[SubCategory]


@dataclass
class Question:
    id: uuid
    question_header: str
    explaination: str
    answer: str
    category_id: uuid
    subcategory_id: uuid

