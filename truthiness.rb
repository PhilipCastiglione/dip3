def test(thing)
  if thing
    puts "it's true!"
  else
    puts "it's false!"
  end
end

test('') # => it's true!
test(nil) # => it's false!
test(true) # => it's true!
test(false) # => it's false!
test(['']) # => it's true!
test([true]) # => it's true!
test([false]) # => it's true!
test([]) # => it's true!
test(0) # => it's true!
test(1) # => it's true!

# summary: nil and false are falsey
# not unreasonable but kind of annoying, you still need to check
# false specifically to be strict, but you also need to compare
# a bunch of presence or numerical things if you want "falsiness"
