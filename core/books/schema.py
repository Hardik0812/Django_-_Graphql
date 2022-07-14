from calendar import c
from unicodedata import category
import graphene
from graphene_django import DjangoObjectType
from pkg_resources import require
from .models import *


# class BooksType(DjangoObjectType):
#     class Meta:
#         model = books
#         field = ("id","title","excerpt")


# class Query(graphene.ObjectType):
#     all_books = graphene.List(BooksType)

#     def resolve_all_books(root,info):
#         return books.objects.filter(title="Django")

# schema = graphene.Schema(query=Query)




class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id","name")

class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id","title","category","quiz")

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title","quiz")

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question","answer_text")




class CategoryMutation(graphene.Mutation):

    class Arguments:
        # name = graphene.String(required=True)
        id = graphene.ID()


    category = graphene.Field(CategoryType)


    @classmethod
    def mutate(cls,root,info,id):
        category = Category.objects.get(id=id)
        category.delete()
        #return CategoryMutation(category=category)
        return 





class Query(graphene.ObjectType):
    
    all_questions = graphene.Field(QuestionType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())

    def resolve_all_questions(root, info, id):
        return Question.objects.get(pk=id)
    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question=id)

class Mutation(graphene.ObjectType):
    update_category = CategoryMutation.Field()


schema = graphene.Schema(query=Query,mutation=Mutation)

