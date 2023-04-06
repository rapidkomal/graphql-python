from graphene import ObjectType, String, Schema
import json
import graphene
import os

"""
1. #Return name and age as string

class Query(graphene.ObjectType):
    name = graphene.String()
    department = graphene.String()
    
    def resolve_name(root, info):
        return "komal"
    
    def resolve_department(root, info):
        return "computer science"

schema = graphene.Schema(query=Query)
print(schema)
        
# graphql query

query_graphql = '''
query myquery {
    test_name : name
    department
}
'''
result = schema.execute(query_graphql)
print(json.dumps(result.data, indent=3))

"""

"""
2. # return with default value  
class Query(graphene.ObjectType):
    name = graphene.String(value=graphene.String(default_value="kom"))
    department = graphene.String(value=graphene.String(default_value="cs"))
    
    def resolve_name(root, info, value):
        return value
    
    def resolve_department(root, info, value):
        return value
        
schema = graphene.Schema(query=Query)
print(schema)

# graphql query

query_graphql = '''
query myquery {
    t_name: name (value:"komal test")
    t_dpt: department (value:"com sci")
}
'''
result = schema.execute(query_graphql)
print(json.dumps(result.data, indent=3))
"""

"""
# 3. List return   
DATA = [
    {
       "name" : "Komal",
       "age" : "27" 
    },
    {
        "name" : "Singh",
        "age" : "26"  
    }
]

class Person(graphene.ObjectType):
    name= graphene.String()
    age = graphene.String()

class Query(graphene.ObjectType):
    # array = graphene.List(Person)
    array = graphene.List(Person, size=graphene.Int(default_value=1))
    
    def resolve_array(root, info, size):
        # return DATA
        return DATA[:size]
    
    
schema = graphene.Schema(query=Query)
print(schema)

query_graphql = '''
query myquery {
    # array {
    #     name,
    #     age  
    # },
    
    array (size:2) {
        name,
        age  
    }
}
'''

result = schema.execute(query_graphql)
print(json.dumps(result.data, indent=3))
"""

# 4. List return   
# DATA = [
#     {
#        "name" : "Komal",
#        "age" : "27" 
#     },
#     {
#         "name" : "Singh",
#         "age" : "26"  
#     }
# ]

# class Person(graphene.ObjectType):
#     name= graphene.String()
#     age = graphene.String()

# # to create new person
# class CreatePerson(graphene.Mutation):
#     class Arguments:
#         name = graphene.String()
    
#     ok = graphene.Boolean()
#     person = graphene.Field(Person)    
    
#     def mutate(self,info, name):
#         person = Person(name=name)
#         ok = True
#         return CreatePerson(person=person, ok=ok)

# class MyMutation(graphene.ObjectType):
#     create_person = CreatePerson.Field()

# class Query(graphene.ObjectType):
#    person = graphene.Field(Person)
    
# schema = graphene.Schema(query=Query, mutation=MyMutation)
# print(schema)

# query_graphql = '''
# mutation MyFirstMutation {
#     createPerson(name:"newone") {
#        person {
#            name
#        }
#     }
# }
# '''

# result = schema.execute(query_graphql)
# # print(json.dumps(result.data, indent=3))
# if result.errors:
#     print(result.errors)
# else:
#     print(json.dumps(result.data, indent=3))


# use Inputfields and inputObjectTypes in Mutation
class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.String()

class PersonInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    age = graphene.String(required=True)


class CreatePerson(graphene.Mutation):
    class Arguments:
        person_input = PersonInput(required=True)
    
    
    ok = graphene.Boolean()
    person = graphene.Field(Person)    
    
    def mutate(self, info, person_input):
        person = Person(name=person_input.name, age=person_input.age)
        ok = True
        return CreatePerson(person=person, ok=ok)

class MyMutation(graphene.ObjectType):
    create_person = CreatePerson.Field()

class Query(graphene.ObjectType):
    person = graphene.Field(Person)
    
schema = graphene.Schema(query=Query, mutation=MyMutation)
print(schema)

query_graphql = '''
mutation MyFirstMutation {
    createPerson(personInput: {name:"newone", age: "30"}) {
       person {
           name
           age
       }
       ok
    }
}
'''

result = schema.execute(query_graphql)

if result.errors:
    print(result.errors)
else:
    print(json.dumps(result.data, indent=3))