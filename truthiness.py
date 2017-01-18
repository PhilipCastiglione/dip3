def test(thing):
    if thing:
        print("it's True!")
    else:
        print("it's False!")

test('') # => it's False!
test(None) # => it's False!
test(True) # => it's True!
test(False) # => it's False!
test(['']) # => it's True!
test([True]) # => it's True!
test([False]) # => it's True!
test([]) # => it's False!
test(0) # => it's False
test(1) # => it's True!

# summary: empty data structures, None, False, and 0 are falsey
# a bit loose, but more useful (just check False specifically if you want to be strict)
