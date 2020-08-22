import random
import factory
from users.models import Address, User


class AddressFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Address
    
    street = factory.Faker('first_name')
    city = factory.Faker('first_name')
    state = factory.Faker('first_name')
    zip_code = factory.Faker('first_name')


class UserFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('first_name')
    user_type = random.choice(['PARENT', 'CHILD'])
    addresses = factory.SubFactory(AddressFactory)