# wordcount

Cannonical mapreduce wordcount tutorial, implemented in python.

## Dependencies

- Python 3

## Running

```bash
$ git clone git@github.com:thehackerati/wordcount.git
$ cd wordcount
$ echo "foo foo quux labs foo bar quux" | ./mapper.py | sort -k1,1 | ./reducer.py
bar	1
foo	3
labs	1
quux	2
```

Checkout the 'iterators' branch to see a wordcount implementation using Python iterators and generators.

```bash
$ git checkout iterators
```

You can run it and see that it behaves the same as the first implementation in master.

Now, try downloading [James Joyce's Ulysses](https://www.gutenberg.org/files/4300/4300-0.txt) to use as a larger data set for testing.

```bash
$ cat ulysses.txt | ./mapper.py | sort -k1,1 | ./reducer.py
!               1
"Come           1
"Defects,"      1
"I              1
"Information    1
...
```

Notice that we're considering words with adjacent punctuation as unique. To get a better count of words, we need to strip out this punctuation. Checkout the 'strip-nonalpha' branch to see a version that uses a compiled regular expression to remove non-alphanumeric characters.

```bash
$ git checkout strip-nonalpha
$ cat ulysses.txt | ./mapper.py | sort -k1,1 | ./reducer.py
...
Dub     3
Dubedat 3
Dubedatandshedidbedad   1
Dublin  122
Dubliner        2
Dubliners       1
...
```

Notice now that we're much cleaner, but there are still some suspicious results, like 'Dubedatandshedidbedad' above.

## Exercises

- Count different capitalizations of the same word as the same.
- Address any remaining data quality issues exist in this implementation.
- Add unit tests.
- Deploy this code locally on Hadoop.
- Implement continuous integration.
- Deploy this code to AWS (EMR).

## Resources

- https://en.wikipedia.org/wiki/MapReduce
- http://wiki.apache.org/hadoop/HadoopMapReduce

## Credits

This code was inspired by an [awesome tutorial by Michael Noll](http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/).
