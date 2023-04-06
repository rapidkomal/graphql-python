from graphene import ObjectType, String

class User(ObjectType):
    id = String()
    name = String()
    email = String()
    password = String()
    