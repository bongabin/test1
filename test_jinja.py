from jinja2 import Environment, PackageLoader, Template


def test_hello():
    env = Environment(loader=PackageLoader('test_jinja', 'templates'))
    template = env.get_template('mytemplate.html')
    print template.render(the='variables', go='here')


def test_module():
    env = Environment(loader=PackageLoader('test_jinja', 'templates'))
    template = env.get_template('module.html')
    m = template.module
    if m.info['pk_field']:
        print m.info['pk_field']

    if m.info['query']:
        for query in m.info['query']:
            print query

    m.info['param'] = 'param'
    m.info['name'] = 'starfsd.MaxLockTimeout'
    m.info['value'] = 3600

    print '========================'
    print template.render(data=m.info)
    print '========================'


def test_module2():
    env = Environment(loader=PackageLoader('test_jinja', 'templates'))
    template = env.get_template('module.html')
    m = template.module

    template = Template(m.html)

    data = {}
    data['params'] = {}
    data.params['name'] = 'brwon'
    data.params['value'] = 'hahaha'


    print '========================'
    print template.render(data=data)
    print '========================'


def main():
    #test_hello()
    #test_module()

    test_module2()





if __name__ == '__main__':
    main()
