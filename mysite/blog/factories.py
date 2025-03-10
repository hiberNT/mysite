import factory#
from faker import Factory as FakerFactory

from django.contrib.auth.models import User
from django.utils.timezone import now

from blog.models import Post

faker = FakerFactory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User #o django ja da modelos ja predefinido no caso aqui estamos pegando do user

    email = factory.Faker("safe_email")#esses 2 campos aqui geram um email falso e ussername falso para o teste
    username = factory.LazyAttribute(lambda x: faker.name())


    @classmethod
    def _prepare(cls, create, **kwargs):#salva esses fakes para o teste
        password = kwargs.pop("password", None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
            return user
        
class PostFactory(factory.django.DjangoModelFactory):#aqui esta sendo passado as class criada no post.py na pasta modelss
    title = factory.LazyAttribute(lambda x: faker.sentence())
    created_on = factory.LazyAttribute(lambda x: now())
    author = factory.SubFactory(UserFactory)
    status = 0


    class Meta:
        model = Post