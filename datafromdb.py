import graphene

def get_user_by_id(id):
    users = [{
            "id" : 1,
            "name" : "komal",
            "email" : "komal@gmail.com"
            
        },
        {
            "id" : 2,
            "name" : "kumari",
            "email" : "kumari@gmail.com"
            
    }]
    return list(filter(lambda user: user["id"]==int(id), users))[0]
    
class User(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()

class Query(graphene.ObjectType):
    user = graphene.Field(User, id=graphene.ID())

    def resolve_user(self, info, id):
        # Retrieve user from database or other storage mechanism
        user_data = get_user_by_id(id)
        return User(id=user_data['id'], name=user_data['name'], email=user_data['email'])

schema = graphene.Schema(query=Query)
print(schema)
id = int(input("enter id to find data: "))
result = schema.execute(
    '''
    query {
    user(id: %d) {
        id
        name
        email
    }
    }
    '''%id
)
print(result)
