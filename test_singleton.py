class OnlyOne:
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg

        def __str__(self):
            return repr(self) + ' ' + self.val

        def test(self):
            print 'test'
            print OnlyOne.instance

        def get_val(self):
            print 'val:', self.val

    instance = None

    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)


print 'OnlyOne:', OnlyOne
print 'OnlyOne.instance:', OnlyOne.instance

x = OnlyOne('sasuge')
print 'x:', x

print 'OnlyOne:', OnlyOne
print 'OnlyOne.instance:', OnlyOne.instance

y = OnlyOne('bob')
print 'y:', y

x.get_val()
y.get_val()

x.test()