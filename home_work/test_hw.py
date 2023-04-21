def test_passing():
    assert ('home', 'work') == ('home', 'work')


def test_passing1():
    assert 'QA' == 'QC'


def test_passing2():
    assert not(1, 1, 2, 3, 5) == (2, 3, 5)


def test_passing3():
    assert 'QA' == 'QA'