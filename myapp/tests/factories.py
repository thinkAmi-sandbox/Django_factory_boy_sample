import factory
from ..models import *

# 親から子のファクトリ
# http://factoryboy.readthedocs.org/en/latest/recipes.html#dependent-objects-foreignkey
class ParentToChild_ChildFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Child
    name = 'child1'

class ParentToChild_ParentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Parent
    name = 'parent1'
    # 第二引数には、外部キーのフィールド名をセット
    # このプロパティ名は、関連先にアクセスする際に使う(relatedparent__name)
    # http://stackoverflow.com/questions/21564878/factory-boy-add-several-dependent-objects
    relatedparent = factory.RelatedFactory(ParentToChild_ChildFactory, 'parent')
    

# 子から親のファクトリ
class ChildToParent_ParentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Parent
    name = 'parent2'
    
class ChildToParent_ChildFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Child
    name = 'child2'
    parent = factory.SubFactory(ChildToParent_ParentFactory, name='parent_value')
    
class ChildToParent_ChildWithCopyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Child
    name = 'child2'
    # `SelfAttribute(..<親のフィールド名>)`により、子のフィールド値を親のフィールド値へとコピーできる
    # http://factoryboy.readthedocs.org/en/latest/recipes.html#copying-fields-to-a-subfactory
    parent = factory.SubFactory(
        ChildToParent_ParentFactory, 
        name=factory.SelfAttribute('..name'))
    
    
class SameParent_ParentFactroy(factory.django.DjangoModelFactory):
    class Meta:
        model = Parent
    name = 'parent_same'

class SameParent_ChildFactroy(factory.django.DjangoModelFactory):
    class Meta:
        model = Child
    name = 'child_same'
    
    
class M2MSimple_PublicationFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda n: "Title #%s" % n)
    
    class Meta:
        model = Publication
        
class M2MSimple_AuthorFactory(factory.django.DjangoModelFactory):
    headline = 'm2m_simple_headline'
    
    class Meta:
        model = Author
        
    @factory.post_generation
    def publications(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            for publication in extracted:
                self.publications.add(publication)


class M2M_Through_PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person
    name = 'person_name'

class M2M_Through_GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group
    name = 'group_name'

class M2M_Through_MembershipFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Membership
    person = factory.SubFactory(M2M_Through_PersonFactory)
    group = factory.SubFactory(M2M_Through_GroupFactory)


# PersonのFactoryを継承し、1Personで1Groupを持つモデルを生成するFactory
class M2M_Through_PersonWithGroupFactory(M2M_Through_PersonFactory):
    membership = factory.RelatedFactory(
        M2M_Through_MembershipFactory, 'person')

# PersonのFactoryを継承し、1Personで2Groupを持つモデルを生成するFactory
class M2M_Through_PersonWithTwoGroupFactory(M2M_Through_PersonFactory):
    membership1 = factory.RelatedFactory(
        M2M_Through_MembershipFactory, 'person')
    membership2 = factory.RelatedFactory(
        M2M_Through_MembershipFactory, 'person')
    
# PersonのFactoryを継承し、1Personで3Groupを持つモデルを生成するFactory
class M2M_Through_PersonWithTwoGroup_Update_Factory(M2M_Through_PersonFactory):
    membership1 = factory.RelatedFactory(
        M2M_Through_MembershipFactory, 'person', group__name='Group1')
    membership2 = factory.RelatedFactory(
        M2M_Through_MembershipFactory, 'person', group__name='Group2')
    membership3 = factory.RelatedFactory(
        M2M_Through_MembershipFactory, 'person', group__name='Group3')