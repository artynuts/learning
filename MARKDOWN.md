# Markdown
*Italics* **Bold**
This is the first paragraph. The next para is become of 2 spaces  
This is the second paragraph. The next para is because this line ends with a backslash \
This is the third paragraph. The next para is because of 2 newlines  
~Strikethrough~

This is the fourth paragraph
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
####### Heading 7 does not exist  
> First line blockquote. Then 2 spaces for next line  
> Second line blockquote. The next line is with an empty > sign
>
> Third line blockquote
>
> > Nested line blockquote has 2 > >
>
> Last line

* unordered list 1
* unordered list 2
* unordered list 3

1. ordered list 1
1. ordered list 2
1. ordered list 3

* Nested Main List
    1. sub list 1a
    1. sub list 1b
* Nested Main list 2
    + sub list 2a
        * sub sub list 2a1
    + sub list 2b
* Nested Main list 3

Inline `code`. The next code block starts with newline and 4 spaces.

    indent 4 spaces
    second line with indent 4 spaces

```
Or use 3 backticks
```
[link to bing.com](www.bing.com)  
[cross reference to google.com][id]  
#### Cat image as inline reference
![cat image](images/cat.jpg)  
#### Dog image as a cross reference
![dog image][dogid]

[id]: www.google.com "Google"
[dogid]: images/dog.jpg "Dog"

#### Tables

| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Row 1 Col 1 | Row 1 Col 2 | Row 1 Col 3 |
| Row 2 Col 1 | Row 2 Col 2 | Row 2 Col 3 |

##### Table With alignment

| Name       | Age | Occupation   |
|:-----------|:---:|-------------:|
| Alice      |  30 |     Engineer |
| Bob        |  25 |     Designer |
| Charlie    |  35 |      Teacher |

##### Spanning rows

| Alice | Reddit   | Twitter     |
| ----- | -------- | ----------- |
| Alice | u/alice  | @alice      |
|       | /r/pizza | @ilovepizza |


