import test_singleton

class OnlyOne(object):
    class __OnlyOne:
        def __init__(self):
            self.val = None

        def __str__(self):
            return repr(self) + ' ' + self.val

    instance = None

    def __new__(cls):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne()
        return OnlyOne.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)

print 'OnlyOne:', OnlyOne
print 'OnlyOne.instance:', OnlyOne.instance

x = OnlyOne()
x.val = 'sasuge'
print 'x:', x

print 'OnlyOne:', OnlyOne
print 'OnlyOne.instance:', OnlyOne.instance

y = OnlyOne()
y.val = 'bob'
print 'y:', y
print 'x:', x

print 'test_singleton.OnlyOne.instance:', test_singleton.OnlyOne.instance