# Python script for transferring color palettes between Adobe experience design files

The syntax for transferring palettes between adobe xd files...

```python <path to importer.py> <path to target> <path to source> -a/--append(optional)```

The default behavior of the script is to replace the color palette of the target file. Use the optional ```-a/--append``` flag to append the colors to the existing colors in the file.

### Example

Appends palette from source.xd to target.xd

```python importer.py path/to/target.xd path/to/source.xd -a```   
