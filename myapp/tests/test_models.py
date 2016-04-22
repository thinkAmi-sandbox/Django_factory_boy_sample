from django.test import TestCase

from .factories import *
from ..models import *

class Test_ParentToChild(TestCase):
    def test_親を作った時に子も作る(self):
        print('\n---親から子(RelatedFactory)---')

        p1 = ParentToChild_ParentFactory()
        print(p1.name)
        print(p1.child_set.all()[0].name)
        
        print(p1.child_set.__class__.__name__)
        print(p1.child_set)
        print(p1.child_set.all())

        p2 = ParentToChild_ParentFactory(
            name='parent_factory', relatedparent__name='child_factory')
        print(p2.name)
        print(p2.child_set.all()[0].name)
        
        assert True
        
        
class Test_ChildToParent(TestCase):
    def test_子を作った時に親も作る(self):
        print('\n---子から親(SubFactory)---')
        
        c1 = ChildToParent_ChildFactory()
        print(c1.parent.name)
        print(c1.name)
        
        c2 = ChildToParent_ChildWithCopyFactory()
        print(c2.parent.name)
        print(c2.name)
        
        assert True
        
        
class Test_SameParent(TestCase):
    def test_同じ親を持つ子を作る(self):
        print('\n---同じ親---')
        p = SameParent_ParentFactroy()
        c1 = SameParent_ChildFactroy(name='child1', parent=p)
        c2 = SameParent_ChildFactroy(name='child2', parent=p)
        
        print('child_pk:{pk} - child_name:{name}, parent_pk:{p_pk}'
                .format(pk=c1.pk, name=c1.name, p_pk=c1.parent.pk))
        print('child_pk:{pk} - child_name:{name}, parent_pk:{p_pk}'
                .format(pk=c2.pk, name=c2.name, p_pk=c2.parent.pk))
                
        assert True
        
        
class Test_ManyToMany_throughなし(TestCase):
    def test_ManyToManyを作る(self):
        print('\n---M2M simple---')
        pub1 = M2MSimple_PublicationFactory.create()
        pub2 = M2MSimple_PublicationFactory.create()
        pub3 = M2MSimple_PublicationFactory.create()
        
        a = M2MSimple_AuthorFactory.create(publications=(pub1, pub2, pub3))        
        print('pk:{pk}, headline:{headline}'.format(pk=a.pk, headline=a.headline))

        print(a.publications.__class__.__name__)
        print('all()なし: {}'.format(a.publications))
        print('all()あり: {}'.format(a.publications.all()))
        print(a.publications.all()[0].title)

        assert True
        
        
class Test_ManyToMany_throughあり(TestCase):
    def test_ManyToManyを作る_1Person1Group(self):
        print('\n---M2M through 1:1---')
        
        p = M2M_Through_PersonWithGroupFactory.create()
        print(p.membership_set.all()[0].person.name)
        print(p.membership_set.all()[0].group.name)
        
        assert True
    
    
    def test_ManyToManyを作る_1Person2Group(self):
        print('\n---M2M through 1:2---')
        
        p = M2M_Through_PersonWithTwoGroupFactory.create()
        print(p.membership_set.all()[0].person.name)
        print(p.membership_set.all()[0].group.name)
        print(p.membership_set.all()[1].person.name)
        print(p.membership_set.all()[1].group.name)
        
        
    def test_ManyToManyを作る_1Person2Group_with_update(self):
        print('\n---M2M through 1:2 with update---')
        
        g = M2M_Through_GroupFactory.create(name='g-1')
        p = M2M_Through_PersonWithTwoGroup_Update_Factory.create(
            name='re_person_name',
            membership1__group=g,
            membership2__group__name='g-2',
        )
        print(p.membership_set.all()[0].person.name)
        print(p.membership_set.all()[0].group.name)
        print(p.membership_set.all()[1].person.name)
        print(p.membership_set.all()[1].group.name)
        print(p.membership_set.all()[2].person.name)
        print(p.membership_set.all()[2].group.name)

        assert True
        