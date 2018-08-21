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
    with assert_raises(StopIteration):
        next(c)


def test_generate_2():
    print("testing wordlist.Generator(\"ab\").generate(2, 2)")
    gen = wordlist.Generator("ab")
    c = gen.generate(2, 2)
    assert_equals(next(c), 'aa')
    assert_equals(next(c), 'ab')
    assert_equals(next(c), 'ba')
    assert_equals(next(c), 'bb')
    with assert_raises(StopIteration):
        next(c)


def test_generate_3():
    print("testing wordlist.Generator(\"ab\").generate(0, 0)")
    gen = wordlist.Generator("ab")
    with assert_raises(ValueError) as e:
        c = gen.generate(0, 0)
        next(c)
        assert_equals(e.mess, "minlen must be > 0")

    with assert_raises(ValueError):
        c = gen.generate(0, 0)
        next(c)

def test_generate_4():
    print("testing wordlist.Generator(\"ab\").generate(1, 2)")
    gen = wordlist.Generator("a-b")
    c = gen.generate(1, 2)
    assert_equals(next(c), 'a')
    assert_equals(next(c), 'b')
    assert_equals(next(c), 'aa')
    assert_equals(next(c), 'ab')
    assert_equals(next(c), 'ba')
    assert_equals(next(c), 'bb')
    with assert_raises(StopIteration):
        next(c)


def test_generate_with_pattern():
    print("testing wordlist.Generator(\"ab\").generate_with_pattern(\"@@\")")
    gen = wordlist.Generator("ab")
    c = gen.generate_with_pattern('@@')
    assert_equals(next(c), 'aa')
    assert_equals(next(c), 'ab')
    assert_equals(next(c), 'ba')
    assert_equals(next(c), 'bb')
    with assert_raises(StopIteration):
        next(c)


def test_generate_with_pattern_2():
    print("testing wordlist.Generator(\"ab\").generate_with_pattern(\"@a\")")
    gen = wordlist.Generator("ab")
    c = gen.generate_with_pattern('@a')
    assert_equals(next(c), 'aa')
    assert_equals(next(c), 'ba')
    with assert_raises(StopIteration):
        next(c)


def test_generate_with_pattern_3():
    print("testing wordlist.Generator(\"ab\").generate_with_pattern(\"a@\")")
    gen = wordlist.Generator("ab")
    c = gen.generate_with_pattern('a@')
    assert_equals(next(c), 'aa')
    assert_equals(next(c), 'ab')
    with assert_raises(StopIteration):
        next(c)


def test_generate_with_pattern_4():
    print("testing wordlist.Generator(\"ab\").generate_with_pattern(\"a@b\")")
    gen = wordlist.Generator("ab")
    c = gen.generate_with_pattern('a@b')
    assert_equals(next(c), 'aab')
    assert_equals(next(c), 'abb')
    with assert_raises(StopIteration):
        next(c)


def test_generate_with_pattern_5():
    print("testing wordlist.Generator(\"ab\").generate_with_pattern(\"\")")
    gen = wordlist.Generator("ab")
    c = gen.generate_with_pattern('')
    with assert_raises(StopIteration):
        next(c)
