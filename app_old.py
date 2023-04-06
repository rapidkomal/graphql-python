import graphene
from mutation import CreateUser, UpdateUser, DeleteUser
from query import Query
from type import User
from graphene import Field, String, List

class MyMutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

class MyQuery(Query):
    user = Field(User)
    get_user = Field(User, id=String())
    get_users = List(User)

schema = graphene.Schema(query=MyQuery, mutation=MyMutations)
print(schema)

# create User
result = schema.execute(
'''
    mutation{
    createUser(id:"1", name:"graphene test", email:"graphene@gmail.com", password:"test@1234") {
       user {
           id
           name
           email
           password
       }
    }
}
'''
)

print(result.data)

# Update User
result = schema.execute(
'''
    mutation{
    updateUser(id:"1", name:"test", email:"graphene@gmail.com", password:"test123@1234") {
       user {
           id
           name
           email
           password
       }
    }
}
'''
)

print(result.data)


# Delte User
result = schema.execute(
'''
    mutation{
    deleteUser(id:"1") {
       user {
           id
           name
           email
           password
       }
    }
}
'''
)

print(result.data)


# Get User
result = schema.execute(
'''
query {
    getUser(id:"1") {
           id
           name
           email
           password
    }
}
'''
)

print(result)



# Get All User
result = schema.execute(
'''
query {
        getUsers {
            id
            name
            email
            password
        }
}
'''
)

# print(result)