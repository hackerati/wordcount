# wordcount

Cannonical mapreduce wordcount example, implemented in python.

## Dependencies

- Python 3

## Running

```bash
$ git clone ...
$ cd wordcount
$ echo "foo foo quux labs foo bar quux" | ./mapper.py | sort | ./reducer.py
bar	1
foo	3
labs	1
quux	2
```

## Deploying

Left as an exercise, but you can deploy this code on Hadoop.

## Resources

- https://en.wikipedia.org/wiki/MapReduce
- http://wiki.apache.org/hadoop/HadoopMapReduce

## Credits

This code was inspired by an (awesome tutorial by Michael Noll)[http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/].
