# Working with Adobe XD files

### python script for transferring color palettes between Adobe experience design files

the syntax for transferring palettes between adobe xd files...

```python <path to importer.py> <path to target> <path to source> -a/--append(optional)```

the default behavior of the script is to replace the color palette of the target file. Use the optional ```-a/--append``` flag to append the colors to the existing colors in the file.

### Example

appends palette from source.xd to target.xd

```python importer.py path/to/target.xd path/to/source.xd -a```   