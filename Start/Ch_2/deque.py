# deque objects are like double-ended queues

import collections
import string


# TODO: initialize a deque with lowercase letters
d = collections.deque('abcdefg')
# TODO: deques support the len() function
print(len(d))
# TODO: deques can be iterated over
for letter in d:
    print(letter.upper())
# TODO: manipulate items from either end
d.pop()
d.popleft()
d.append("<")
d.appendleft(">")
d.rotate(1)
# TODO: use an index to get a particular item
print(d[5])