# Copyref

The plugin For **Sublime Text 3** that just copies a reference to current line of file to clipboard.
It was inspired by behaviour of IntelliJ IDEA.

## How it works?
The plugin copies to clipboard a reference to the current line which consists of `path_to_file:line_number`:
```
/home/user/project/copyref/README.md:9
```

If you're working on the project, it will use relative (to project root) path to the file instead:
```
project/copyref/README.md:9
```

## Installation

TBD. Too lazy to prepare proper package for PackageControl. Please send a suggestion if you think it should be done :)

## License

MIT