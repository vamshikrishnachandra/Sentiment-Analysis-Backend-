import graphene
from graphene import ObjectType
from graphene_django.types import DjangoObjectType
from transformers import pipeline

# Load the sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")

class SentimentType(graphene.ObjectType):
    label = graphene.String()
    score = graphene.Float()

class Query(ObjectType):
    sentiment_analysis = graphene.Field(SentimentType, text=graphene.String(required=True))

    def resolve_sentiment_analysis(self, info, text):
        result = sentiment_pipeline(text)[0]
        return SentimentType(label=result["label"], score=result["score"])

class AnalyzeTextMutation(graphene.Mutation):
    class Arguments:
        text = graphene.String(required=True)

    label = graphene.String()
    score = graphene.Float()

    def mutate(self, info, text):
        result = sentiment_pipeline(text)[0]
        return AnalyzeTextMutation(label=result["label"], score=result["score"])

class Mutation(ObjectType):
    analyze_text = AnalyzeTextMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
