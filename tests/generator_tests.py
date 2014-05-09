from nose.tools import assert_equals, assert_raises
import wordlist


def test_generate():
    print("testing wordlist.Generator(\"ab\").generate(1, 2)")
    gen = wordlist.Generator("ab")
    c = gen.generate(1, 2)
    assert_equals(next(c), 'a')
    assert_equals(next(c), 'b')
    assert_equals(next(c), 'aa')
    assert_equals(next(c), 'ab')
    assert_equals(next(c), 'ba')
    assert_equals(next(c), 'bb')
    with assert_raises(StopIteration) as e:
        next(c)


def test_generate_2():
    print("testing wordlist.Generator(\"ab\").generate(2, 2)")
    gen = wordlist.Generator("ab")
    c = gen.generate(2, 2)
    assert_equals(next(c), 'aa')
    assert_equals(next(c), 'ab')
    assert_equals(next(c), 'ba')
    assert_equals(next(c), 'bb')
    with assert_raises(StopIteration) as e:
        next(c)
