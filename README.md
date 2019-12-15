# Comment generator

When passed a word, this piece of code transforms the text into a B I G hashtag style word.

Great for printing little pieces of code when running long pieces of code.

Example:

```python
# pip install comment-creator==0.0.5

from comment_creator import comment_creator

comment_creator.generate_comment("dates started")


```

Function can output letters and white space at the moment. Will add numbers.
 
 Output:
 
 ```python                                                                                                                        
                            
####   #####  #####  #####   ###          ###   #####  #####  #####  #####  #####  #### 
##  #  #   #    #    ##     #            #        #    #   #  ##  #    #    ##     ##  #
##  #  #####    #    ####    ###          ###     #    #####  #####    #    ####   ##  #
##  #  #   #    #    ##         #            #    #    #   #  ## #     #    ##     ##  #
####   #   #    #    #####   ###          ###     #    #   #  ##  #    #    #####  #### 
                                                                                              
```
 
## Improvement since 0.0.5
1) Added numbers to the character dictionary

2) You can pass an optional second string argument: "warn"(yellow), "success"(green) or "fail"(red) and the output will be in the respective color. Default color is the default print color statement of your IDE.


